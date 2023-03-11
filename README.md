# ONNX sklearn converter

ONNX sklearn converter is a small python package that uses skl2onnx (ONNX official package) to convert sklearn models to ONNX format. This repo provide an easy-to-use framework to boost your sklearn models to production. 

## Getting Started

To use sklearn-onnx-converter you have to clone the repo and  install the package.

### Prerequisites

* Python >=3.8

### Installation

Before to use sklearn-onnx-converter you must install the package using pip
```
$ pip install .
```

## Usage

To convert a sklearn model to the ONNX format you can run the convert command as a bash script or using it as a Python script. (See the examples folder for more details).

### Bash script
```
$ python onnx_converter/onnx_converter.py -m PATH_TO_SKLEARN_MODEL -f PATH_TO_YOUR_FEATURE_CONFIG_FILE -o OUTPUT_FOLDER
```

### Python script

- Create a main.py:
```python
# main.py
from sklearn_onnx_converter import convert

if __name__ == "__main__":
    convert(
        # your sklearn model path
        model_path="model_path",
        # feature config YAML file
        feature_config="features.yaml",
        # output path
        output_path="output_dir",
    )

```

- run the script:
```
$ python main.py
```

## TODO

- [ ] Add docker support
- [ ] Add more examples

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request 
