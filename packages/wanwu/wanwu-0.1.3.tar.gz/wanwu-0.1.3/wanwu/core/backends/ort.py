import numpy as np
from alfred.utils.log import logger
from wanwu.core.backends.base import TensorInfo
import os

try:
    import onnxruntime as rt
    import onnxruntime
except ImportError:
    onnxruntime = None
from alfred.utils.log import logger
from .base import WrapperBase


def ort_dtype_to_numpy(od):
    if "float" in od: 
        return np.float32
    elif "int" in od:
        return np.int64


class ORTWrapper(WrapperBase):
    def __init__(self, onnx_f) -> None:
        self.onnx_f = onnx_f
        so = onnxruntime.SessionOptions()
        so.intra_op_num_threads = 5
        so.execution_mode = onnxruntime.ExecutionMode.ORT_PARALLEL
        so.inter_op_num_threads = 5
        so.graph_optimization_level = onnxruntime.GraphOptimizationLevel.ORT_ENABLE_ALL
        os.environ["OMP_NUM_THREADS"] = "5"
        self.ort_session = onnxruntime.InferenceSession(onnx_f, sess_options=so)
        self.input_names = [input.name for input in self.ort_session.get_inputs()]
        # todo: extract possible input hw for vision models

    def infer(self, inputs, return_dict=True):
        if isinstance(inputs, dict):
            ort_inputs = inputs
        else:
            if not isinstance(inputs, list):
                # incase users may input single img
                inputs = [inputs]
            assert len(inputs) == len(
                self.ort_session.get_inputs()
            ), "inputs must same with model."
            ort_inputs = dict(
                (self.ort_session.get_inputs()[i].name, inpt)
                for i, inpt in enumerate(inputs)
            )
        ort_outs = self.ort_session.run(None, ort_inputs)

        if return_dict:
            outs_dict = dict()
            for i, oo in enumerate(self.ort_session.get_outputs()):
                n = oo.name
                outs_dict[n] = ort_outs[i]
            return outs_dict
        else:
            return ort_outs

    def get_inputs_dict(self):
        input_tensor_dict = {}
        inputs_node = self.ort_session.get_inputs()
        for inode in inputs_node:
            sh = inode.shape
            # handle dynamic shapes
            sh_replaced = []
            for i in sh:
                if isinstance(i, str):
                    sh_replaced.append(-1)
                else:
                    sh_replaced.append(i)
            input_tensor_dict[inode.name] = TensorInfo(
                sh_replaced, ort_dtype_to_numpy(inode.type)
            )
        return input_tensor_dict

    def get_outputs_dict(self):
        output_tensor_dict = {}
        inputs_node = self.ort_session.get_outputs()
        for inode in inputs_node:
            sh = inode.shape
            sh_replaced = []
            for i in sh:
                if isinstance(i, str):
                    sh_replaced.append(-1)
                else:
                    sh_replaced.append(i)
            output_tensor_dict[inode.name] = TensorInfo(sh_replaced, "float")
        return output_tensor_dict
