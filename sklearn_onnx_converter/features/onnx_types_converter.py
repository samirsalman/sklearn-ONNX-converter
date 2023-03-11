from skl2onnx.common.data_types import (
    StringTensorType,
    FloatTensorType,
    BooleanTensorType,
    Float16TensorType,
    Int32TensorType,
    Int16TensorType,
    Int8TensorType,
    DataType,
)

from sklearn_onnx_converter.features import FeatureType

TYPE_MAPPING = {
    FeatureType.INT32.value: Int32TensorType,
    FeatureType.INT16.value: Int16TensorType,
    FeatureType.INT8.value: Int8TensorType,
    FeatureType.FLOAT32.value: FloatTensorType,
    FeatureType.FLOAT16.value: Float16TensorType,
    FeatureType.STRING.value: StringTensorType,
    FeatureType.BOOL.value: BooleanTensorType,
}


def convert_type(feature_type: FeatureType) -> DataType:
    """
    Converts a feature type to the corresponding ONNX tensor type.

    Args:
        feature_type (FeatureType): The feature type to convert.

    Returns:
        Type[ONNXType]: The ONNX tensor type that corresponds to the feature type.

    Raises:
        KeyError: If the given feature type is not supported.

    Examples:
        >>> convert_type(FeatureType.INT32)
        skl2onnx.common.data_types.Int32TensorType

        >>> convert_type(FeatureType.STRING)
        skl2onnx.common.data_types.StringTensorType
    """
    feature_type = TYPE_MAPPING.get(feature_type.value)
    if not feature_type:
        raise KeyError(f"Unsupported feature type: {feature_type.value}")
    return feature_type
