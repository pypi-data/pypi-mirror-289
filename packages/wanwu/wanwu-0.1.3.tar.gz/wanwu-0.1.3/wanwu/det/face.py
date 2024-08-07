from typing import Union

import cv2
from wanwu.core.enums import Backends
from .det import Det
import numpy as np
from PIL import Image


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
        score_thr=0.5,
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

    def get_face_boxes(
        self, im: Union[str, np.ndarray, Image.Image], threshold=0.5
    ) -> np.ndarray:

        if isinstance(im, str):
            im = cv2.imread(im)
        elif isinstance(im, Image.Image):
            im = np.array(im)
        inp = self.load_inputs(im, normalize_255=True, is_rgb=True)
        raw_boxes, scores, labels = self.infer(inp)
        return raw_boxes, scores
