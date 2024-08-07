import numpy as np
from alfred.utils.log import logger
from wanwu.core.backends.base import TensorInfo
import os

try:
    from openvino import runtime
except ImportError:
    runtime = None
from alfred.utils.log import logger
from .base import WrapperBase

try:
    import onnxruntime as rt
    import onnxruntime
except ImportError:
    onnxruntime = None


def ort_dtype_to_numpy(od):
    if "float" in od:
        return np.float32
    elif "int" in od:
        return np.int64


class OpenVINOWrapper(WrapperBase):
    def __init__(self, onnx_f) -> None:
        self.onnx_f = onnx_f
        os.environ["OMP_NUM_THREADS"] = "5"

        self.openvino_executor = runtime.Core()
        self.model = self.openvino_executor.compile_model(
            model=self.openvino_executor.read_model(model=self.onnx_f),
            device_name="CPU",
        )

        ort_session = onnxruntime.InferenceSession(onnx_f)

        self.inputs_dict = {}
        self.outputs_dict = {}

        # OpenVINO can not get dynamic shape
        # infer_request = self.model.create_infer_request()
        # for output in infer_request.model_outputs:
        #     sh = output.shape
        #     dt = output.dtype
        #     self.outputs_dict[output.any_name] = TensorInfo(sh, dt)

        # for inp in infer_request.model_inputs:
        #     sh = inp.shape
        #     dt = inp.dtype
        #     self.inputs_dict[inp.any_name] = TensorInfo(sh, dt)

        inputs_node = ort_session.get_inputs()
        for inode in inputs_node:
            sh = inode.shape
            # handle dynamic shapes
            sh_replaced = []
            for i in sh:
                if isinstance(i, str):
                    sh_replaced.append(-1)
                else:
                    sh_replaced.append(i)
            self.inputs_dict[inode.name] = TensorInfo(
                sh_replaced, ort_dtype_to_numpy(inode.type)
            )

        inputs_node = ort_session.get_outputs()
        for inode in inputs_node:
            sh = inode.shape
            sh_replaced = []
            for i in sh:
                if isinstance(i, str):
                    sh_replaced.append(-1)
                else:
                    sh_replaced.append(i)
            self.outputs_dict[inode.name] = TensorInfo(sh_replaced, "float")

        del ort_session

        logger.info(
            f"inputnames: {self.inputs_dict.keys()}, outputnames: {self.outputs_dict.keys()}"
        )
        # todo: extract possible input hw for vision models

    def infer(self, inputs, return_dict=False):
        if isinstance(inputs, dict):
            ort_inputs = inputs
        else:
            if not isinstance(inputs, list):
                # incase users may input single img
                inputs = [inputs]
            assert len(inputs) == len(
                self.ort_session.get_inputs()
            ), "inputs must same with model."
            ort_inputs = inputs

        self.infer_request = self.model.create_infer_request()
        ort_outs = self.infer_request.infer(ort_inputs)
        return ort_outs

    def get_inputs_dict(self):
        return self.inputs_dict

    def get_outputs_dict(self):
        return self.outputs_dict
