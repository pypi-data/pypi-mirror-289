import numpy as np
from alfred.utils.log import logger
import os

try:
    import MNN
except Exception as e:
    MNN = None

from .base import TensorInfo, WrapperBase


class MNNWrapper(WrapperBase):
    def __init__(self, onnx_f) -> None:
        """
        mnn not support convert in JIT
        """

        if os.path.basename(onnx_f).split(".")[-1] != "mnn":
            logger.error("model not mnn format, convert to mnn first.")
            exit()

        self.mnn_f = onnx_f
        logger.info(f"Loading from mnn model: {self.mnn_f}")

        # online parse onnx file to mnn format?
        self.interpreter = MNN.Interpreter(self.mnn_f)
        self.session = self.interpreter.createSession()
        self.input_tensor = self.interpreter.getSessionInput(self.session)
        self.output_tensor = self.interpreter.getSessionOutput(self.session)

    def np_as_mnn(self, inp_data):
        """
        inp data with NCHW
        """
        # logger.info(inp_data.shape)
        assert len(inp_data.shape) == 4, "mnn currently only support NCHW input."
        tmp_input = MNN.Tensor(
            inp_data.shape,
            MNN.Halide_Type_Float,
            inp_data,
            MNN.Tensor_DimensionType_Caffe,
        )
        return tmp_input

    def infer_si(self, inputs):
        if isinstance(inputs, list):
            inputs = np.array(inputs)

        tmp_input = self.np_as_mnn(inputs)
        self.input_tensor.copyFrom(tmp_input)

        self.interpreter.runSession(self.session)

        # output_tensor = self.interpreter.getSessionOutput(self.session, "output")
        output_tensor_dict = self.interpreter.getSessionOutputAll(self.session)

        res = {}
        for k, v in output_tensor_dict.items():
            tmp_output = MNN.Tensor(
                v.getShape(),
                v.getDataType(),
                np.ones(v.getShape()).astype(np.float32),
                MNN.Tensor_DimensionType_Caffe,
            )
            v.copyToHostTensor(tmp_output)
            res[k] = np.array(tmp_output.getData()).reshape(v.getShape())
        return res

    def infer(self, inputs):
        if isinstance(inputs, list):
            inputs = np.array(inputs)

        tmp_input = self.np_as_mnn(inputs)
        self.input_tensor.copyFrom(tmp_input)

        self.interpreter.runSession(self.session)

        # output_tensor = self.interpreter.getSessionOutput(self.session, "output")
        output_tensor_dict = self.interpreter.getSessionOutputAll(self.session)

        res = {}
        for k, v in output_tensor_dict.items():
            tmp_output = MNN.Tensor(
                v.getShape(),
                v.getDataType(),
                np.ones(v.getShape()).astype(np.float32),
                MNN.Tensor_DimensionType_Caffe,
            )
            v.copyToHostTensor(tmp_output)
            res[k] = np.array(tmp_output.getData()).reshape(v.getShape())
        return res

    def get_inputs_dict(self):
        input_tensor_dict = self.interpreter.getSessionInputAll(self.session)

        res = {}
        for k, v in input_tensor_dict.items():
            res[k] = TensorInfo(v.getShape(), v.getDataType())
        return res

    def get_outputs_dict(self):
        output_tensor_dict = self.interpreter.getSessionInputAll(self.session)

        res = {}
        for k, v in output_tensor_dict.items():
            res[k] = TensorInfo(v.getShape(), v.getDataType())
        return res
