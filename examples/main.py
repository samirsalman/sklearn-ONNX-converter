from sklearn_onnx_converter import convert

if __name__ == "__main__":
    convert(
        # your sklearn model path
        model_path="model_path",
        # feature config YAML file
        feature_config="features_example.yaml",
        # output path
        output_path="out",
    )
