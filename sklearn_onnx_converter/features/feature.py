from dataclasses import dataclass
import enum
from typing import List
from omegaconf import OmegaConf


class FeatureType(enum.Enum):
    """Feature type enum class"""

    INT32 = "int32"
    INT16 = "int16"
    INT8 = "int8"
    FLOAT32 = "int32"
    FLOAT16 = "float16"
    STRING = "str"
    BOOL = "bool"


@dataclass
class FeatureConfig:
    """
    Feature config class
    """

    name: str
    dimensions: List[int]
    feature_type: FeatureType


def load_features_config(feature_file: str) -> List[FeatureConfig]:
    """Load the features config from a YAML file and return a list of FeatureConfig

    Args:
        feature_file (str): path to the YAML file

    Returns:
        List[FeatureConfig]: list of FeatureConfig objects
    """
    conf = OmegaConf.load(feature_file)
    features = list()
    for feature in conf.features:
        features.append(
            FeatureConfig(
                dimensions=feature.dimensions,
                feature_type=FeatureType(feature.type),
                name=feature.name,
            )
        )
    assert len(features) > 0, "Features config list is empty"
    return features
