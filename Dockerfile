FROM python:3.9.16-slim
WORKDIR /app
RUN apt update &&\
    apt install git -y 
RUN git clone --branch main https://github.com/samirsalman/sklearn-ONNX-converter.git 
WORKDIR /app/sklearn-ONNX-converter 
RUN pip install .

ENTRYPOINT [ "python", "sklearn_onnx_converter/onnx_converter.py" ]