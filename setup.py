from setuptools import setup
from setuptools import find_packages


setup(
    name="sklearn_onnx_converter",
    version="0.0.1",
    description="Easy-to-use utils to convert sklearn models to ONNX format",
    url="#",
    install_requires=[
        "skl2onnx==1.14.0",
        "typer==0.7.0",
        "omegaconf==2.3.0",
    ],
    author="Samir Salman",
    author_email="samirsalman.dev@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    zip_safe=False,
)
