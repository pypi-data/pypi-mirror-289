from typing import Union
from wanwu.core.enums import Backends
from wanwu.utils.image_utils import load_inputs_naive
from .det import Det
import numpy as np
from PIL import Image

try:
    import cv2

    has_cv2 = True
except ImportError:
    has_cv2 = False


class FaceWanwu(Det):

    def __init__(
        self,
        onnx_f: str = None,
        backend: Backends = Backends.CPU_ORT,
        type: str = "yolov5n-0.5",
        batch_size=1,
        input_width=416,
        input_height=416,
        num_classes=1,
        score_thr=0.4,
        nms_thr=0.45,
        keep_to_topk=100,
        fp16=False,
        timing=False,
        do_nms=True,
        **kargs
    ) -> None:
        super().__init__(
            onnx_f,
            backend,
            type,
            batch_size,
            input_width,
            input_height,
            num_classes,
            score_thr,
            nms_thr,
            keep_to_topk,
            fp16,
            timing,
            do_nms,
            **kargs
        )
        pass

    def get_face_boxes(self, im: Union[str, np.ndarray, Image.Image]) -> np.ndarray:

        if isinstance(im, str):
            if has_cv2:
                try:
                    im = cv2.imread(im)
                    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
                except Exception as e:
                    im = Image.open(im).convert("RGB")
            else:
                im = Image.open(im).convert("RGB")

            if isinstance(im, Image.Image):
                im = np.array(im)
        elif isinstance(im, Image.Image):
            im = np.array(im)
        inp = self.load_inputs(im, normalize_255=True)
        raw_boxes, scores, labels = self.infer(inp)
        return raw_boxes, scores

    def load_inputs(self, im, normalize_255=False):
        self.crt_image_raw_h = im.shape[0]
        self.crt_image_raw_w = im.shape[1]
        return load_inputs_naive(
            im,
            self.input_height,
            self.input_width,
            normalize_255=normalize_255,
        )
