from abc import ABC, abstractclassmethod
from turtle import back
from .cellar import model_urls, LOCAL_CACHE_FOLDER
import onnx
from alfred.utils.file_io import download
from .dispatcher import dispatcher_on_device_auto
from .enums import Backends
from alfred.utils.log import logger
import os


AVAILABLE_BACKENDS = [
    Backends.GPU_TENSORRT,
    Backends.CPU_OPENVINO,
    Backends.CPU_ORT,
    Backends.AUTO,
    Backends.CPU_MNN,
    Backends.CPU_PPLNN,
]


def get_model_name_suffix_by_backend(backend: Backends):
    if backend in [Backends.GPU_ORT]:
        return "gpu"
    elif backend == Backends.GPU_TENSORRT:
        return "trt"
    elif backend in [Backends.CPU_ORT, Backends.CPU_OPENVINO]:
        return "cpu"
    else:
        return 'cpu'


def get_model_path_by_key(model_type, backend):
    model_type = model_type + f"_{get_model_name_suffix_by_backend(backend)}"
    assert model_type in model_urls.keys(), f"{model_type} not in warehouse"
    if model_type in model_urls.keys():
        f_url = model_urls[model_type]
        f_path = os.path.join(LOCAL_CACHE_FOLDER, f_url.split("/")[-1])
        if not os.path.exists(f_path):
            logger.info(f"downloading model from: {f_url} into {LOCAL_CACHE_FOLDER}")
            f_path = download(f_url, LOCAL_CACHE_FOLDER)
        return f_path
    else:
        return None


class BaseInfer(ABC):
    def __init__(
        self,
        type: str,
        onnx_f: str,
        backend: Backends,
        batch_size=1,
        input_width=640,
        input_height=512,
    ) -> None:
        super().__init__()
        self.type = type

        self.backend = backend
        assert (
            self.backend in AVAILABLE_BACKENDS
        ), f"{self.backend} not in currently supported backends: {AVAILABLE_BACKENDS}"

        if self.backend == Backends.AUTO:
            logger.info("Backend in AUTO mode, deciding on auto device.")
            self.backend = dispatcher_on_device_auto()

        if onnx_f is not None:
            self.onnx_f = onnx_f
        else:
            if type is not None:
                # get models from type
                type = type + f"_{get_model_name_suffix_by_backend(self.backend)}"
                assert (
                    type in model_urls.keys()
                ), f"unsupported model built in: {type}, avaiable: {model_urls.keys()}"
                f_url = model_urls[type]
                f_path = os.path.join(LOCAL_CACHE_FOLDER, f_url.split("/")[-1])
                if not os.path.exists(f_path):
                    logger.info(
                        f"downloading model from: {f_url} into {LOCAL_CACHE_FOLDER}"
                    )
                    f_path = download(f_url, LOCAL_CACHE_FOLDER)
                self.onnx_f = f_path
            else:
                ValueError(
                    "Either onnx_f or type not specific, I dont know what model you want run."
                )

        assert (
            self.onnx_f is not None
        ), "Can not either get onnx file from type or onnx_f, please set at least one of them."

        self.batch_size = batch_size
        self.input_width = input_width
        self.input_height = input_height

    @abstractclassmethod
    def infer(self, inp):
        NotImplemented

    @abstractclassmethod
    def vis_res(self, res):
        NotImplemented
