

from wanwu.utils.image_utils import load_inputs_std_mean
from ..core.infer import Backends, BaseInfer
from ..core.modelloader import ModelLoader, TaskType
import time
import numpy as np


class Seg(BaseInfer):
    def __init__(
        self,
        onnx_f: str = None,
        backend: Backends = Backends.CPU_ORT,
        type: str = "yolov5s_coco",
        batch_size=1,
        input_width=640,
        input_height=512,
        num_classes=80,
        fp16=False,
        timing=False,
        **kargs,
    ) -> None:
        super(Seg, self).__init__(
            type=type,
            onnx_f=onnx_f,
            backend=backend,
            batch_size=batch_size,
            input_width=input_width,
            input_height=input_height,
        )

        # add some CPU realtime Segmentation Models
        self.num_classes = num_classes

        self.timing = timing
        self.frame_time_cost = 0

        self.model_loader = ModelLoader(
            self.onnx_f,
            backend=self.backend,
            task_type=TaskType.SEG,
            fp16=fp16,
            num_classes=self.num_classes,
            batch_size=self.batch_size,
            input_width=self.input_width,
            input_height=self.input_height,
        )
        self.infer_wrapper = self.model_loader.get_infer_wrapper()

    def infer(self, inp):
        if not self.model_loader.is_dynamic_on_hw:
            assert (
                inp.shape[-2] == self.input_width or inp.shape[-2] == self.input_height
            ), f"Seems your inp shape not equal to your Det input hw, please check. {inp.shape} vs {self.input_height}x{self.input_width}"
        if self.timing:
            t0 = time.perf_counter()
        res = self.infer_wrapper.infer(inp)
        if self.timing:
            t1 = time.perf_counter()
            self.frame_time_cost = round(t1 - t0, 3)
        return res

    def load_inputs(self, img, std, mean, transpose=True, is_rgb=False):
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
