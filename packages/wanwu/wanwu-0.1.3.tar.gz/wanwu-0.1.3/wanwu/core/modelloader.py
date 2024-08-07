from enum import Enum
from numpy import log
from wanwu.core.backends.openvino import OpenVINOWrapper

from wanwu.core.backends.ort import ORTWrapper
from wanwu.core.backends.mnn import MNNWrapper
from .graphsurgeon import OnnxModelSurgeonOperationer
from .infer import Backends
from alfred.utils.log import logger

try:
    from .backends.trt import TensorRTInferencer
    from alfred.deploy.tensorrt.common import build_engine_onnx_v2

    HAS_TRT = True
except ImportError as e:
    logger.warning(f'No TensorRT env found, disable TensorRT backend. {e}')
    HAS_TRT = False
import os


class TaskType(Enum):

    DET = 0
    SEG = 1
    KPS = 2
    CLS = 3
    BASE = 4

    @staticmethod
    def from_str(s: str):
        if s.lower() == "det":
            return TaskType.DET
        elif s.lower() == "seg":
            return TaskType.SEG
        elif s.lower() == "kps":
            return TaskType.KPS
        elif s.lower() == "cls":
            return TaskType.CLS
        elif s.lower() == "base":
            return TaskType.BASE
        else:
            return TaskType.CLS


class ModelLoader:
    """
    Loading model from onnx, then decide by backend how to construct
    an inference engine:

    if det model:
        if TensorRT:
            load model, inject batchedNMS plugin
        elif CPU:
            do normal load
    if seg model:
        normal
    """

    def __init__(
        self,
        onnx_f,
        backend: Backends,
        task_type: TaskType = TaskType.DET,
        fp16=False,
        int8=False,
        num_classes=80,
        batch_size=1,
        input_width=640,
        input_height=512,
        score_thr=0.2,
        nms_thr=0.6,
        keep_to_topk=100,
        nms_plugin_name="efficient_nms",
    ) -> None:
        self.onnx_f = onnx_f
        self.backend = backend      
        if os.path.basename(self.onnx_f).split(".")[-1] == "onnx":
            if task_type == TaskType.DET:
                if backend == Backends.GPU_TENSORRT:
                    self.save_p = self.get_trt_engine_save_f(onnx_f, fp16=fp16)

                    if not os.path.exists(self.save_p):
                        logger.info("Applying NMSPlugin to onnx for TensorRT deploy...")
                        self.onnx_model_gs = OnnxModelSurgeonOperationer(
                            self.onnx_f, num_classes=num_classes, batch_size=batch_size
                        )
                        self.onnx_model_gs.update_inputs_dims(
                            batch_size, input_height, input_width
                        )
                        if nms_plugin_name == "batched_nms":
                            logger.info(
                                "using BatchedNMSPlugin, this will be replaced in the future."
                            )
                            self.onnx_model_gs.register_trt_batched_nms(
                                score_thr, nms_thr, keep_to_topk
                            )
                        else:
                            self.onnx_model_gs.register_trt_efficient_nms(
                                score_thr, nms_thr, keep_to_topk
                            )
                        # BatchedNMS doesn't support dynamic HW input now, fix input in ONNX model
                        output_onnx_f, self.onnx_model = self.onnx_model_gs.save()
                        logger.info(
                            "An onnx model with nms op saved into: {}".format(
                                output_onnx_f
                            )
                        )

                        if self.onnx_model_gs.is_dynamic_on_hw:
                            opt_params = {
                                "images": [
                                    [
                                        batch_size,
                                        3,
                                        input_height,
                                        input_width,
                                    ],  # min shape
                                    [
                                        batch_size,
                                        3,
                                        input_height,
                                        input_width,
                                    ],  # opt shape
                                    [
                                        batch_size,
                                        3,
                                        input_height,
                                        input_width,
                                    ],  # max shape
                                ]
                            }
                        else:
                            opt_params = None

                        logger.info(
                            "Start build TensorRT engine, this will only run once."
                        )
                        e = build_engine_onnx_v2(
                            onnx_file_path=output_onnx_f,
                            engine_file_path=self.save_p,
                            fp16_mode=fp16,
                            save_engine=True,
                            opt_params=opt_params,
                        )
                        if e is not None:
                            logger.info("engine saved into: {}".format(self.save_p))
                        else:
                            RuntimeError("Failed to build engine, aborted.")

                else:
                    logger.info(
                        f"Determine ONNX input with specified: {input_height}x{input_width}"
                    )
                    self.onnx_model_gs = OnnxModelSurgeonOperationer(
                        self.onnx_f, num_classes=num_classes
                    )
                    if (
                        not self.onnx_model_gs.is_dynamic_on_hw
                        and self.onnx_model_gs.ok
                    ):
                        self.onnx_model_gs.update_inputs_dims(
                            batch_size, input_height, input_width
                        )
                        self.onnx_model_gs.save(self.onnx_f)
                        logger.info("New input dimension ONNX saved.")
                    # normally load onnx model
                    self.onnx_model = None
            elif task_type == TaskType.CLS or task_type == TaskType.KPS:
                if backend == Backends.GPU_TENSORRT:
                    self.save_p = self.get_trt_engine_save_f(onnx_f, fp16=fp16)

                    if not os.path.exists(self.save_p):
                        logger.info("Surgeon on ONNX model for TensorRT deploy...")
                        self.onnx_model_gs = OnnxModelSurgeonOperationer(
                            self.onnx_f, num_classes=num_classes
                        )
                        self.onnx_model_gs.update_inputs_dims(
                            batch_size, input_height, input_width
                        )
                        output_onnx_f, self.onnx_model = self.onnx_model_gs.save(
                            output_path=self.onnx_f
                        )
                        logger.info(
                            "An onnx model saved into: {}".format(output_onnx_f)
                        )
                        if self.onnx_model_gs.is_dynamic_on_hw:
                            opt_params = {
                                "images": [
                                    [
                                        batch_size,
                                        3,
                                        input_height,
                                        input_width,
                                    ],  # min shape
                                    [
                                        batch_size,
                                        3,
                                        input_height,
                                        input_width,
                                    ],  # opt shape
                                    [
                                        batch_size,
                                        3,
                                        input_height,
                                        input_width,
                                    ],  # max shape
                                ]
                            }
                        elif self.onnx_model_gs.is_dynamic_on_batch:
                            input_specs = self.onnx_model_gs.inputs_dict
                            logger.info(
                                f"model is dynamic on batch, try adding opt params for trt: {input_specs}"
                            )
                            ss = list(input_specs.values())[0][1:]
                            # TODO: this is hard coded
                            opt_params = {
                                list(input_specs.keys())[0]: [
                                    [1, ss[0], ss[1], ss[2]],  # min shape
                                    [16, ss[0], ss[1], ss[2]],  # opt shape
                                    [32, ss[0], ss[1], ss[2]],  # max shape
                                ]
                            }
                        else:
                            opt_params = None
                            logger.info(
                                "onnx model is not dynamic, directly convert to trt engine."
                            )

                        logger.info(
                            "Start build TensorRT engine, this will only run once."
                        )
                        e = build_engine_onnx_v2(
                            onnx_file_path=self.onnx_f,
                            engine_file_path=self.save_p,
                            fp16_mode=fp16,
                            save_engine=True,
                            opt_params=opt_params,
                        )
                        if e is not None:
                            logger.info("engine saved into: {}".format(self.save_p))
                        else:
                            RuntimeError("Failed to build engine, aborted.")
                else:
                    logger.info(
                        f"Determine ONNX input with specified: {input_height}x{input_width}"
                    )
                    self.onnx_model_gs = OnnxModelSurgeonOperationer(
                        self.onnx_f, num_classes=num_classes
                    )
                    if (
                        not self.onnx_model_gs.is_dynamic_on_hw
                        and self.onnx_model_gs.ok
                    ):
                        self.onnx_model_gs.update_inputs_dims(
                            batch_size, input_height, input_width
                        )
                        self.onnx_model_gs.save(self.onnx_f)
                        logger.info("New input dimension ONNX saved.")
                    # normally load onnx model
                    self.onnx_model = None
            elif task_type == TaskType.SEG:
                self.onnx_model_gs = OnnxModelSurgeonOperationer(
                    self.onnx_f, num_classes=num_classes
                )
                self.is_dynamic_on_hw = self.onnx_model_gs.is_dynamic_on_hw
                if (
                    self.onnx_model_gs.is_dynamic_on_hw
                    and input_width != None
                    and input_height != None
                ):
                    self.onnx_model_gs.update_inputs_dims(
                        batch_size, input_height, input_width
                    )
                    self.onnx_model_gs.save(self.onnx_f)
                    logger.info("New input dimension ONNX saved.")
                # normally load onnx model
                self.onnx_model = None
            elif task_type == TaskType.BASE:
                logger.info("TaskBase will pass onnx graph surgeon.")
                if backend == Backends.GPU_TENSORRT:
                    self.save_p = self.get_trt_engine_save_f(onnx_f, fp16=fp16)
                    logger.info(f'will save engine to: {self.save_p}')
                    if not os.path.exists(self.save_p):
                        logger.info("Surgeon on ONNX model for TensorRT deploy...")
                        self.onnx_model_gs = OnnxModelSurgeonOperationer(
                            self.onnx_f, num_classes=num_classes
                        )
                        self.onnx_model_gs.update_inputs_dims(
                            batch_size, input_height, input_width
                        )
                        output_onnx_f, self.onnx_model = self.onnx_model_gs.save(
                            output_path=self.onnx_f
                        )
                        logger.info(
                            "An onnx model saved into: {}".format(output_onnx_f)
                        )
                        if self.onnx_model_gs.is_dynamic_on_hw:
                            opt_params = {
                                "images": [
                                    [
                                        batch_size,
                                        3,
                                        input_height,
                                        input_width,
                                    ],  # min shape
                                    [
                                        batch_size,
                                        3,
                                        input_height,
                                        input_width,
                                    ],  # opt shape
                                    [
                                        batch_size,
                                        3,
                                        input_height,
                                        input_width,
                                    ],  # max shape
                                ]
                            }
                        elif self.onnx_model_gs.is_dynamic_on_batch:
                            input_specs = self.onnx_model_gs.inputs_dict
                            logger.info(
                                f"model is dynamic on batch, try adding opt params for trt: {input_specs}"
                            )
                            ss = list(input_specs.values())[0][1:]
                            # TODO: this is hard coded
                            opt_params = {
                                list(input_specs.keys())[0]: [
                                    [1, ss[0], ss[1], ss[2]],  # min shape
                                    [16, ss[0], ss[1], ss[2]],  # opt shape
                                    [32, ss[0], ss[1], ss[2]],  # max shape
                                ]
                            }
                        else:
                            opt_params = None
                            logger.info(
                                "onnx model is not dynamic, directly convert to trt engine."
                            )
                        logger.info(
                            "Start build TensorRT engine, this will only run once."
                        )
                        e = build_engine_onnx_v2(
                            onnx_file_path=self.onnx_f,
                            engine_file_path=self.save_p,
                            fp16_mode=fp16,
                            save_engine=True,
                            opt_params=opt_params,
                        )
                        if e is not None:
                            logger.info("engine saved into: {}".format(self.save_p))
                        else:
                            RuntimeError("Failed to build engine, aborted.")
            else:
                logger.info(f"unsupported task now: {task_type}")
        else:
            logger.info("model not in onnx format, pass preprocess onnx step.")

    def get_trt_engine_save_f(self, onnx_f, fp16=False, int8=False):
        if fp16:
            save_p = os.path.join(
                os.path.dirname(onnx_f),
                os.path.basename(onnx_f).replace(".onnx", "_fp16.engine"),
            )
        elif int8:
            save_p = os.path.join(
                os.path.dirname(onnx_f),
                os.path.basename(onnx_f).replace(".onnx", "_int8.engine"),
            )
        else:
            save_p = os.path.join(
                os.path.dirname(onnx_f),
                os.path.basename(onnx_f).replace(".onnx", ".engine"),
            )
        return save_p

    def get_infer_wrapper(self):
        if (
            os.path.basename(self.onnx_f).split(".")[-1] == "mnn"
            and self.backend != Backends.CPU_MNN
        ):
            logger.info(
                f"detected mnn file, but backend is: {self.backend.name}, force to MNN backend."
            )
            self.backend = Backends.CPU_MNN
            return MNNWrapper(self.onnx_f)
        else:
            if self.backend == Backends.GPU_TENSORRT and HAS_TRT:
                return TensorRTInferencer(self.save_p)
            elif self.backend == Backends.CPU_ORT:
                # we don't do graphsurgeon for now.
                return ORTWrapper(self.onnx_f)
            elif (
                self.backend == Backends.CPU_MNN
                and os.path.basename(self.onnx_f).split(".")[-1] == "mnn"
            ):
                # we don't do graphsurgeon for now.
                return MNNWrapper(self.onnx_f)
            elif self.backend == Backends.CPU_OPENVINO:
                return OpenVINOWrapper(self.onnx_f)
            else:
                return ORTWrapper(self.onnx_f)
