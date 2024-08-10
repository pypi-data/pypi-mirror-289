from __future__ import annotations

import logging
import typing as t
from abc import ABC, abstractmethod
from datetime import datetime

import attrs
import mitsuba as mi
import numpy as np
import pinttr
import xarray as xr
from hamilton.driver import Driver

import eradiate

from .. import converters, validators
from .. import pipelines as pl
from ..attrs import AUTO, documented, parse_docs
from ..contexts import KernelContext, MultiGenerator
from ..kernel import MitsubaObjectWrapper, mi_render, mi_traverse
from ..rng import SeedState
from ..scenes.atmosphere import AbstractHeterogeneousAtmosphere
from ..scenes.core import Scene, SceneElement, get_factory, traverse
from ..scenes.illumination import (
    AbstractDirectionalIllumination,
    ConstantIllumination,
    DirectionalIllumination,
    illumination_factory,
)
from ..scenes.integrators import Integrator, integrator_factory
from ..scenes.measure import (
    Measure,
    MultiDistantMeasure,
    measure_factory,
)
from ..spectral.ckd import BinSet, QuadSpec
from ..spectral.index import CKDSpectralIndex, MonoSpectralIndex, SpectralIndex
from ..spectral.mono import WavelengthSet
from ..units import unit_registry as ureg
from ..util.misc import deduplicate_sorted, onedict_value

logger = logging.getLogger(__name__)


def _convert_spectral_set(value):
    if value is AUTO:
        if eradiate.mode().is_ckd:
            return BinSet.default()
        elif eradiate.mode().is_mono:
            return WavelengthSet.default()
        else:
            raise NotImplementedError(f"unsupported mode: {eradiate.mode().id}")
    else:
        return value


@parse_docs
@attrs.define
class Experiment(ABC):
    """
    Abstract base class for all Eradiate experiments. An experiment consists of
    a high-level scene specification parametrized by natural user input, a
    processing and post-processing pipeline, and a result storage data
    structure.
    """

    # Internal Mitsuba scene. This member is not set by the end-user, but rather
    # by the Experiment itself during initialization.
    mi_scene: MitsubaObjectWrapper | None = attrs.field(
        default=None,
        repr=False,
        init=False,
    )

    measures: list[Measure] = documented(
        attrs.field(
            factory=lambda: [MultiDistantMeasure()],
            converter=lambda value: (
                [measure_factory.convert(x) for x in pinttr.util.always_iterable(value)]
                if not isinstance(value, dict)
                else [measure_factory.convert(value)]
            ),
            validator=attrs.validators.deep_iterable(
                member_validator=attrs.validators.instance_of(Measure)
            ),
        ),
        doc="List of measure specifications. The passed list may contain "
        "dictionaries, which will be interpreted by "
        ":data:`.measure_factory`. "
        "Optionally, a single :class:`.Measure` or dictionary specification "
        "may be passed and will automatically be wrapped into a list.",
        type="list of :class:`.Measure`",
        init_type="list of :class:`.Measure` or list of dict or "
        ":class:`.Measure` or dict",
        default=":class:`MultiDistantMeasure() <.MultiDistantMeasure>`",
    )

    integrator: Integrator = documented(
        attrs.field(
            default=AUTO,
            converter=converters.auto_or(integrator_factory.convert),
            validator=validators.auto_or(
                attrs.validators.instance_of(Integrator),
            ),
        ),
        doc="Monte Carlo integration algorithm specification. "
        "This parameter can be specified as a dictionary which will be "
        "interpreted by :data:`.integrator_factory`."
        "The integrator defaults to :data:`AUTO`, which will choose the appropriate "
        "integrator depending on the experiment's configuration. ",
        type=":class:`.Integrator` or AUTO",
        init_type=":class:`.Integrator` or dict or AUTO",
        default="AUTO",
    )

    _results: dict[str, xr.Dataset] = attrs.field(factory=dict, repr=False)

    @property
    def results(self) -> dict[str, xr.Dataset]:
        """
        Post-processed simulation results.

        Returns
        -------
        dict[str, Dataset]
            Dictionary mapping measure IDs to xarray datasets.
        """
        return self._results

    default_spectral_set: BinSet | WavelengthSet = documented(
        attrs.field(
            default=AUTO,
            validator=validators.auto_or(
                attrs.validators.instance_of((BinSet, WavelengthSet))
            ),
            converter=_convert_spectral_set,
            repr=False,
        ),
        doc="Default spectral set. This attribute is used to set the "
        "default value for :attr:`spectral_set`."
        "If the value is :data:`AUTO`, the default spectral set is selected "
        "based on the active mode. Otherwise, the value must be a "
        ":class:`.BinSet` or :class:`.WavelengthSet` instance.",
        type=":class:`.BinSet` or :class:`.WavelengthSet`",
        init_type=":class:`.BinSet` or :class:`.WavelengthSet` or :data:`AUTO`",
        default=":data:`AUTO`",
    )

    # Mapping of measure index and WavelengthSet or BinSet depending on active
    # mode. This attribute is set by the '_normalize_spectral()' method.
    _spectral_set = attrs.field(init=False, repr=False)

    @property
    def spectral_set(self) -> dict[int, WavelengthSet | BinSet]:
        """
        A dictionary mapping measure index to the associated spectral set.
        """
        return self._spectral_set

    quad_spec: QuadSpec = attrs.field(
        factory=QuadSpec.default,
        converter=QuadSpec.convert,
        validator=attrs.validators.instance_of(QuadSpec),
    )

    def __attrs_post_init__(self):
        self._normalize_spectral()

    def _normalize_spectral(self) -> None:
        """
        Setup spectral set based on active mode.
        """
        # default value for spectral set
        spectral_set = self.default_spectral_set

        # if the atmosphere provides a spectral set, use it
        atmosphere = getattr(self, "atmosphere", None)
        if atmosphere and isinstance(atmosphere, AbstractHeterogeneousAtmosphere):
            atmosphere_spectral_set = atmosphere.spectral_set(quad_spec=self.quad_spec)
            if atmosphere_spectral_set is not None:
                spectral_set = atmosphere_spectral_set

        # finally, the spectral set is filtered by the SRF
        self._spectral_set = {
            i: measure.srf.select_in(spectral_set)
            for i, measure in enumerate(self.measures)
        }

    def clear(self) -> None:
        """
        Clear previous experiment results and reset internal state.
        """
        self.results.clear()

        for measure in self.measures:
            measure.mi_results.clear()

    @abstractmethod
    def init(self) -> None:
        """
        Generate kernel dictionary and initialise Mitsuba scene.
        """
        pass

    @abstractmethod
    def process(
        self,
        spp: int = 0,
        seed_state: SeedState | None = None,
    ) -> None:
        """
        Run simulation and collect raw results.

        Parameters
        ----------
        spp : int, optional
            Sample count. If set to 0, the value set in the original scene
            definition takes precedence.

        seed_state : :class:`.SeedState`, optional
            Seed state used to generate seeds to initialize Mitsuba's RNG at
            every iteration of the parametric loop. If unset, Eradiate's
            :attr:`root seed state <.root_seed_state>` is used.
        """
        pass

    @abstractmethod
    def postprocess(self) -> None:
        """
        Post-process raw results and store them in :attr:`results`.
        """
        pass

    @abstractmethod
    def pipeline(self, measure: Measure | int) -> Driver:
        """
        Return the post-processing pipeline for a given measure.

        Parameters
        ----------
        measure : .Measure or int
            Measure for which the pipeline is generated.

        Returns
        -------
        hamilton.driver.Driver
        """
        pass

    @property
    @abstractmethod
    def context_init(self) -> KernelContext:
        """
        Return a single context used for scene initialization.
        """
        pass

    @property
    @abstractmethod
    def contexts(self) -> list[KernelContext]:
        """
        Return a list of contexts used for processing.
        """
        pass


def _extra_objects_converter(value: dict | None) -> dict:
    if not value:
        return {}

    result = {}

    for key, element_spec in value.items():
        if isinstance(element_spec, dict):
            element_spec = element_spec.copy()
            element_type = element_spec.pop("factory")
            factory = get_factory(element_type)
            result[key] = factory.convert(element_spec)

        else:
            result[key] = element_spec

    return result


@parse_docs
@attrs.define
class EarthObservationExperiment(Experiment, ABC):
    """
    Abstract based class for experiments illuminated by a distant directional
    emitter.
    """

    extra_objects: dict[str, SceneElement] = documented(
        attrs.field(
            default=None,
            converter=_extra_objects_converter,
            validator=attrs.validators.deep_mapping(
                key_validator=attrs.validators.instance_of(str),
                value_validator=attrs.validators.instance_of(SceneElement),
            ),
        ),
        doc="Dictionary of extra objects to be added to the scene. "
        "The keys of this dictionary are used to identify the objects "
        "in the kernel dictionary.",
        type="dict",
        init_type="dict or None",
        default="None",
    )

    illumination: AbstractDirectionalIllumination | ConstantIllumination = documented(
        attrs.field(
            factory=DirectionalIllumination,
            converter=illumination_factory.convert,
            validator=attrs.validators.instance_of(
                (AbstractDirectionalIllumination, ConstantIllumination)
            ),
        ),
        doc="Illumination specification. "
        "This parameter can be specified as a dictionary which will be "
        "interpreted by :data:`.illumination_factory`.",
        type=":class:`.AbstractDirectionalIllumination` or "
        ":class:`.ConstantIllumination`",
        init_type=":class:`.DirectionalIllumination` or "
        ":class:`.ConstantIllumination` or dict",
        default=":class:`DirectionalIllumination() <.DirectionalIllumination>`",
    )

    def _dataset_metadata(self, measure: Measure) -> dict[str, str]:
        """
        Generate additional metadata applied to dataset after post-processing.

        Parameters
        ----------
        measure : :class:`.Measure`
            Measure for which the metadata is created.

        Returns
        -------
        dict[str, str]
            Metadata to be attached to the produced dataset.
        """

        return {
            "convention": "CF-1.10",
            "source": f"eradiate, version {eradiate.__version__}",
            "history": f"{datetime.utcnow().replace(microsecond=0).isoformat()}"
            f" - data creation - {self.__class__.__name__}.postprocess()",
            "references": "",
        }

    def spectral_indices(self, measure_index: int) -> t.Generator[SpectralIndex]:
        """
        Generate spectral indices for a given measure.

        Parameters
        ----------
        measure_index : int
            Measure index for which spectral indices are generated.

        Yields
        ------
        :class:`.SpectralIndex`
            Spectral index.
        """
        if eradiate.mode().is_mono:
            generator = self.spectral_indices_mono
        elif eradiate.mode().is_ckd:
            generator = self.spectral_indices_ckd
        else:
            raise RuntimeError(f"unsupported mode '{eradiate.mode().id}'")

        yield from generator(measure_index)

    def spectral_indices_mono(
        self, measure_index: int
    ) -> t.Generator[MonoSpectralIndex]:
        yield from self.spectral_set[measure_index].spectral_indices()

    def spectral_indices_ckd(self, measure_index: int) -> t.Generator[CKDSpectralIndex]:
        yield from self.spectral_set[measure_index].spectral_indices()

    def _spectral_index_generator(self):
        return MultiGenerator(
            [self.spectral_indices(i) for i in range(len(self.measures))]
        )

    @property
    def context_init(self):
        return KernelContext(
            si=self._spectral_index_generator().__next__(), kwargs=self._context_kwargs
        )

    @property
    @abstractmethod
    def _context_kwargs(self) -> dict[str, t.Any]:
        pass

    @property
    def contexts(self) -> list[KernelContext]:
        # Inherit docstring

        # Collect contexts from all measures
        sis = []

        for measure_index, _ in enumerate(self.measures):
            _si = list(self.spectral_indices(measure_index))
            sis.extend(_si)

        # Sort and remove duplicates
        key = {
            MonoSpectralIndex: lambda si: si.w.m,
            CKDSpectralIndex: lambda si: (si.w.m, si.g),
        }[type(sis[0])]

        sis = deduplicate_sorted(
            sorted(sis, key=key), cmp=lambda x, y: key(x) == key(y)
        )
        kwargs = self._context_kwargs

        return [KernelContext(si, kwargs=kwargs) for si in sis]

    @property
    @abstractmethod
    def scene_objects(self) -> dict[str, SceneElement]:
        pass

    @property
    def scene(self) -> Scene:
        """
        Return a scene object used for kernel dictionary template and parameter
        table generation.
        """
        return Scene(objects={**self.scene_objects, **self.extra_objects})

    def init(self):
        # Inherit docstring

        logger.info("Initializing kernel scene")

        kdict_template, umap_template = traverse(self.scene)
        try:
            self.mi_scene = mi_traverse(
                mi.load_dict(kdict_template.render(ctx=self.context_init)),
                umap_template=umap_template,
            )
        except RuntimeError as e:
            raise RuntimeError(f"(while loading kernel scene dictionary){e}") from e

        # Remove unused elements from Mitsuba scene parameter table
        self.mi_scene.drop_parameters()

    def process(
        self,
        spp: int = 0,
        seed_state: SeedState | None = None,
    ) -> None:
        # Inherit docstring

        # Set up Mitsuba scene
        if self.mi_scene is None:
            self.init()

        # Run Mitsuba for each context
        logger.info("Launching simulation")

        mi_results = mi_render(
            self.mi_scene,
            self.contexts,
            seed_state=seed_state,
            spp=spp,
        )

        # Assign collected results to the appropriate measure
        sensor_to_measure: dict[str, Measure] = {
            measure.sensor_id: measure for measure in self.measures
        }

        for ctx_index, spectral_group_dict in mi_results.items():
            for sensor_id, mi_bitmap in spectral_group_dict.items():
                if self.integrator.moment:
                    split = mi_bitmap.split()
                    m2 = split[1][1]
                    m2_np = np.array(m2, copy=False)[:, :, [0]]
                    m2 = mi.Bitmap(m2_np, mi.Bitmap.PixelFormat.Y)

                    measure = sensor_to_measure[sensor_id]
                    measure.mi_results[ctx_index] = {
                        "bitmap": split[0][1],
                        "m2": m2,
                        "spp": spp if spp > 0 else measure.spp,
                    }

                else:
                    measure = sensor_to_measure[sensor_id]
                    measure.mi_results[ctx_index] = {
                        "bitmap": mi_bitmap,
                        "spp": spp if spp > 0 else measure.spp,
                    }

    def postprocess(self) -> None:
        # Inherit docstring
        logger.info("Post-processing results")
        measures = self.measures

        # Run pipelines
        for i, measure in enumerate(measures):
            drv: Driver = self.pipeline(measure)
            inputs = self._pipeline_inputs(i)
            outputs = pl.outputs(drv)
            result = drv.execute(final_vars=outputs, inputs=inputs)
            self.results[measure.id] = xr.Dataset({var: result[var] for var in outputs})

    def pipeline(self, measure: Measure | int) -> Driver:
        # Inherit docstring
        if isinstance(measure, int):
            measure = self.measures[measure]
        config = pl.config(measure, integrator=self.integrator)
        return eradiate.pipelines.driver(config)

    def _pipeline_inputs(self, i_measure: int):
        # This convenience function collects pipeline inputs for a specific measure

        measure = self.measures[i_measure]
        result = {
            "bitmaps": measure.mi_results,
            "spectral_set": self.spectral_set[i_measure],
            "illumination": self.illumination,
            "srf": measure.srf,
        }

        config = pl.config(measure)
        if config.get("add_viewing_angles", False):
            result["angles"] = measure.viewing_angles.m_as(ureg.deg)
        else:
            result["viewing_angles"] = None

        return result


# ------------------------------------------------------------------------------
#                              Experiment runner
# ------------------------------------------------------------------------------


def run(
    exp: Experiment,
    spp: int = 0,
    seed_state: SeedState | None = None,
) -> xr.Dataset | dict[str, xr.Dataset]:
    """
    Run an Eradiate experiment. This function performs kernel scene assembly,
    runs the computation and post-processes the raw results. The output consists
    of one or several xarray datasets.

    Parameters
    ----------
    exp : Experiment
        Reference to the experiment object which will be processed.

    spp : int, optional, default: 0
        Optional parameter to override the number of samples per pixel for all
        computed measures. If set to 0, the configured value for each measure
        takes precedence.

    seed_state : :class:`.SeedState`, optional
            Seed state used to generate seeds to initialize Mitsuba's RNG at
            every iteration of the parametric loop. If unset, Eradiate's
            :attr:`root seed state <.root_seed_state>` is used.

    Returns
    -------
    Dataset or dict[str, Dataset]
        If a single measure is defined, a single xarray dataset is returned.
        If several measures are defined, a dictionary mapping measure IDs to
        the corresponding result dataset is returned.
    """
    exp.process(spp=spp, seed_state=seed_state)
    exp.postprocess()
    return exp.results if len(exp.results) > 1 else onedict_value(exp.results)
