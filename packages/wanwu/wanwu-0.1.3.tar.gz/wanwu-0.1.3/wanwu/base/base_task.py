from wanwu.utils.image_utils import load_inputs_std_mean
from ..core.infer import Backends, BaseInfer
from ..core.modelloader import ModelLoader, TaskType
import time
import numpy as np
from alfred import logger


class TaskBase(BaseInfer):
    def __init__(
        self,
        onnx_f: str = None,
        backend: Backends = Backends.CPU_ORT,
        model_type: str = "yolov5s_coco",
        batch_size=1,
        input_width=640,
        input_height=512,
        num_classes=80,
        fp16=False,
        timing=False,
        task_type: TaskType = TaskType.BASE,
        **kargs,
    ) -> None:
        super(TaskBase, self).__init__(
            type=model_type,
            onnx_f=onnx_f,
            backend=backend,
            batch_size=batch_size,
            input_width=input_width,
            input_height=input_height,
        )

        self.num_classes = num_classes

        self.timing = timing
        self.frame_time_cost = 0

        model_loader = ModelLoader(
            self.onnx_f,
            backend=self.backend,
            task_type=task_type,
            fp16=fp16,
            num_classes=self.num_classes,
            batch_size=self.batch_size,
            input_width=self.input_width,
            input_height=self.input_height,
        )
        self.infer_wrapper = model_loader.get_infer_wrapper()
        self.backend = model_loader.backend
        self.log_once_tag = False

    def infer(self, inp, return_dict=True):
        if isinstance(inp, list):
            inp = np.concatenate(inp, axis=0)

        if self.timing:
            t0 = time.perf_counter()
        res = self.infer_wrapper.infer(inp, return_dict=return_dict)
        if self.timing:
            t1 = time.perf_counter()
            self.frame_time_cost = round(t1 - t0, 3)
            res["time"] = self.frame_time_cost
        return res

    def infer_dummy(self):
        inputs = {}
        for k, v in self.infer_wrapper.get_inputs_dict().items():
            in_shape = v.shape
            in_shape_new = in_shape
            if -1 in in_shape[1:]:
                in_shape_new = [self.input_height if (i == -1) else i for i in in_shape]
                in_shape_new[0] = self.batch_size
                if not self.log_once_tag:
                    logger.info(
                        f"detected dynamic shape: {in_shape}, forced using: {in_shape_new}"
                    )
            elif -1 == in_shape[0]:
                if not self.log_once_tag:
                    logger.info(
                        f"detected dynamic shape, forced using batch=={self.batch_size}"
                    )
                in_shape_new = in_shape
                in_shape_new[0] = self.batch_size
            ii = np.random.rand(*in_shape_new).astype(v.dtype)
            inputs[k] = ii
        # todo: using dict as input format
        res = self.infer(inputs, return_dict=True)
        t = res["time"]
        if not self.log_once_tag:
            self.log_once_tag = True
        return t

    def load_inputs(self, img, std=1, mean=0, transpose=True, is_rgb=False):
        return load_inputs_std_mean(
            img,
            self.input_height,
            self.input_width,
            std=std,
            mean=mean,
            transpose=transpose,
            is_rgb=is_rgb,
        )

    def vis_res(self, img, res, class_names=None):
        print("Classes: ", res)
