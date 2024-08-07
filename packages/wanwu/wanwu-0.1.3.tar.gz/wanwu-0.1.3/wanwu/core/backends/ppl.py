from .base import TensorInfo, WrapperBase
import numpy as np
from alfred.utils.log import logger
import os
import sys

try:
    from pyppl import nn as pplnn
    from pyppl import common as pplcommon
except ImportError:
    pplnn = None


class PPLModel(object):
    def __init__(self, model_file, engine_type="x86"):
        self._engines = []
        if engine_type == "x86":
            self._create_x86_engine()
        elif engine_type == "cuda":
            self._create_cuda_engine()
        else:
            logger.error("not support engine type: ", engine_type)
            sys.exit(-1)
        self._create_runtime(model_file)

    def _create_x86_engine(self):
        x86_options = pplnn.x86.EngineOptions()
        x86_options.mm_policy = pplnn.x86.MM_COMPACT
        x86_engine = pplnn.x86.EngineFactory.Create(x86_options)
        if not x86_engine:
            logger.error("create x86 engine failed.")
            sys.exit(-1)
        self._engines.append(x86_engine)

    def _create_cuda_engine(self):
        cuda_options = pplnn.cuda.EngineOptions()
        cuda_options.device_id = 0
        cuda_engine = pplnn.cuda.EngineFactory.Create(cuda_options)
        self._engines.append(cuda_engine)

    def _create_runtime(self, model_file_name):
        runtime_builder = pplnn.onnx.RuntimeBuilderFactory.Create()
        if not runtime_builder:
            logger.error("create RuntimeBuilder failed.")
            sys.exit(-1)

        status = runtime_builder.LoadModelFromFile(model_file_name)
        if status != pplcommon.RC_SUCCESS:
            logger.error(
                "init OnnxRuntimeBuilder failed: " + pplcommon.GetRetCodeStr(status)
            )
            sys.exit(-1)

        resources = pplnn.onnx.RuntimeBuilderResources()
        resources.engines = self._engines
        status = runtime_builder.SetResources(resources)
        if status != pplcommon.RC_SUCCESS:
            logger.error(
                "OnnxRuntimeBuilder SetResources failed: "
                + pplcommon.GetRetCodeStr(status)
            )
            sys.exit(-1)

        status = runtime_builder.Preprocess()
        if status != pplcommon.RC_SUCCESS:
            logger.error(
                "OnnxRuntimeBuilder preprocess failed: "
                + pplcommon.GetRetCodeStr(status)
            )
            sys.exit(-1)

        self._runtime = runtime_builder.CreateRuntime()
        if not self._runtime:
            logger.error("create Runtime instance failed.")
            sys.exit(-1)

    def _prepare_input(self, input_file):
        """set input data"""
        tensor = self._runtime.GetInputTensor(0)
        in_data = np.fromfile(input_file, dtype=np.float32).reshape((1, 3, 800, 1200))
        status = tensor.ConvertFromHost(in_data)
        if status != pplcommon.RC_SUCCESS:
            logger.error(
                "copy data to tensor["
                + tensor.GetName()
                + "] failed: "
                + pplcommon.GetRetCodeStr(status)
            )
            sys.exit(-1)

    def prepare_input_from_numpy(self, inputs):
        """set input data"""
        if isinstance(inputs, dict):
            for i in range(self._runtime.GetInputCount()):
                tensor = self._runtime.GetInputTensor(i)
                assert (
                    tensor.GetName() in inputs.keys()
                ), f"can not find input: {tensor.GetName()}"
                in_data = np.array(inputs[tensor.GetName()], dtype=np.float32)
                status = tensor.ConvertFromHost(in_data)
                if status != pplcommon.RC_SUCCESS:
                    logger.error(
                        "copy data to tensor["
                        + tensor.GetName()
                        + "] failed: "
                        + pplcommon.GetRetCodeStr(status)
                    )
                    sys.exit(-1)
        else:
            tensor = self._runtime.GetInputTensor(0)
            in_data = np.array(inputs, dtype=np.float32)
            status = tensor.ConvertFromHost(in_data)
            if status != pplcommon.RC_SUCCESS:
                logger.error(
                    "copy data to tensor["
                    + tensor.GetName()
                    + "] failed: "
                    + pplcommon.GetRetCodeStr(status)
                )
                sys.exit(-1)

    def _prepare_output(self):
        """save output"""
        res = {}
        for i in range(self._runtime.GetOutputCount()):
            tensor = self._runtime.GetOutputTensor(i)
            tensor_data = tensor.ConvertToHost()
            if not tensor_data:
                logger.error("copy data from tensor[" + tensor.GetName() + "] failed.")
                sys.exit(-1)
            res[tensor.GetName()] = np.array(tensor_data, copy=False)
        return res

    def run(self):
        """run pplmodel

        Keyword arguments:
        engine_type -- which engine to use x86 or cuda
        model_file_name -- input model file
        input_file -- input data file (binary data)
        """

        status = self._runtime.Run()
        if status != pplcommon.RC_SUCCESS:
            logger.error("Run() failed: " + pplcommon.GetRetCodeStr(status))
            sys.exit(-1)
        return self._prepare_output()

    def get_inputs_dict(self):
        res = {}
        for i in range(self._runtime.GetInputCount()):
            tensor = self._runtime.GetInputTensor(i)
            res[tensor.GetName()] = TensorInfo(tensor.GetShape(), tensor.GetDataType())
        return res

    def get_outputs_dict(self):
        res = {}
        for i in range(self._runtime.GetOutputCount()):
            tensor = self._runtime.GetOutputTensor(i)
            res[tensor.GetName()] = TensorInfo(tensor.GetShape(), tensor.GetDataType())
        return res


class PPLCPUWrapper(WrapperBase):
    def __init__(self, onnx_f) -> None:
        """
        PPL.NN inference as backend
        """
        if pplnn is None:
            logger.error("import pyppl failed, ppl backend not available.")
        else:
            self.onnx_f = onnx_f
            logger.info(f"Loading from onnx model: {self.onnx_f}")

            # online parse onnx file to mnn format?
            self.ppl_model = PPLModel(self.onnx_f, "x86")

    def infer_si(self, inputs):
        if isinstance(inputs, list):
            inputs = np.array(inputs)

        self.ppl_model.prepare_input_from_numpy(inputs)
        res = self.ppl_model.run()
        return res

    def infer(self, inputs, return_dict=False):
        if isinstance(inputs, list):
            inputs = np.array(inputs)

        self.ppl_model.prepare_input_from_numpy(inputs)
        res = self.ppl_model.run()
        return res

    def get_inputs_dict(self):
        return self.ppl_model.get_inputs_dict()

    def get_outputs_dict(self):
        return self.ppl_model.get_outputs_dict()
