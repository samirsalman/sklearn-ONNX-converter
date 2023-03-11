from pathlib import Path
from joblib import load
from skl2onnx import convert_sklearn
import typer

from sklearn_onnx_converter.features import load_features_config, convert_type


def convert(
    model_path: str = typer.Option(..., "-m", "--model"),
    output_path: str = typer.Option(..., "-o", "--output"),
    feature_config: str = typer.Option(..., "-f", "--features"),
):
    """
    Converts a trained scikit-learn model to ONNX format and saves it to disk.

    Args:
        model_path (str): The path to the trained scikit-learn model file.
        output_path (str): The path to the directory where the ONNX model file should be saved.
        feature_config (str): The path to the YAML file that describes the input features of the model.

    Returns:
        None

    Raises:
        FileNotFoundError: If the given model file or feature configuration file does not exist.

    Examples:
        >>> convert(
        ...     model_path="path/to/trained/model.joblib",
        ...     output_path="path/to/output/directory",
        ...     feature_config="path/to/feature/config.yaml",
        ... )
    """
    output_path_dir = Path(output_path)
    output_path_dir.mkdir(parents=True, exist_ok=True)
    feature_config = load_features_config(feature_file=feature_config)

    model = load(model_path)

    initial_types = [
        (
            feature.name,
            convert_type(feature_type=feature.feature_type)(feature.dimensions),
        )
        for feature in feature_config
    ]
    onx = convert_sklearn(model, initial_types=initial_types)

    with open(str(output_path_dir / "model.onnx"), "wb") as f:
        f.write(onx.SerializeToString())


if __name__ == "__main__":
    typer.run(convert)
