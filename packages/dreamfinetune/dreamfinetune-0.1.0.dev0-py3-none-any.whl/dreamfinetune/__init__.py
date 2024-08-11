__version__ = "0.1"

from transformers import _LazyModule

from .trainings import StableDiffusionInpaintingFineTune
from .trainings import StableDiffusionTextToImageFineTune

from .utils import (
    DreamBoothDataset, PromptDataset
)

_import_structure = {
    "configuration_utils": ["ConfigMixin"],
    "loaders": ["FromOriginalModelMixin"],
    "models": [],
    "pipelines": [],
    "schedulers": [],
    "utils": [
        "DreamBoothDataset",
        "PromptDataset"
    ],
    "training": [
        "StableDiffusionInpaintingFineTune",
        "StableDiffusionTextToImageFineTune"
    ]
}

import sys

sys.modules[__name__] = _LazyModule(
    __name__,
    globals()["__file__"],
    _import_structure,
    extra_objects={"__version__": __version__},
)
