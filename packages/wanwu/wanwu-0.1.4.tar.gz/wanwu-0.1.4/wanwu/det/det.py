from typing import Union
from wanwu.utils.boxes_utils import ltwh_to_x1y1x2y2
from wanwu.utils.image_utils import (
    ensure_ndarray_bgr,
    ensure_pil_bgr,
    rescale_boxes,
    load_inputs,
)
from ..core.infer import Backends, BaseInfer
from ..core.modelloader import ModelLoader, TaskType
import time
import numpy as np
import cv2
from PIL import Image


class Det(BaseInfer):
    def __init__(
        self,
        onnx_f: str = None,
        backend: Backends = Backends.CPU_ORT,
        type: str = "yolov5s_coco",
        batch_size=1,
        input_width=640,
        input_height=512,
        num_classes=80,
        score_thr=0.2,
        nms_thr=0.6,
        keep_to_topk=100,
        fp16=False,
        timing=False,
        do_nms=False,
        **kargs,
    ) -> None:
        super(Det, self).__init__(
            type=type,
            onnx_f=onnx_f,
            backend=backend,
            batch_size=batch_size,
            input_width=input_width,
            input_height=input_height,
        )

        self.num_classes = num_classes
        self.score_thr = score_thr
        self.nms_thr = nms_thr
        self.keep_to_topk = keep_to_topk
        self.do_nms = do_nms

        self.timing = timing
        self.frame_time_cost = 0

        model_loader = ModelLoader(
            self.onnx_f,
            backend=self.backend,
            task_type=TaskType.DET,
            fp16=fp16,
            num_classes=self.num_classes,
            batch_size=self.batch_size,
            input_width=self.input_width,
            input_height=self.input_height,
            score_thr=self.score_thr,
            nms_thr=self.nms_thr,
            keep_to_topk=self.keep_to_topk,
        )
        self.infer_wrapper = model_loader.get_infer_wrapper()

        self.crt_image_raw_w = 640
        self.crt_image_raw_h = 640

    def infer(self, inp, ori_h=None, ori_w=None):
        if ori_h is None or ori_w is None:
            ori_h, ori_w = self.crt_image_raw_h, self.crt_image_raw_w
        assert (
            inp.shape[-2] == self.input_width or inp.shape[-2] == self.input_height
        ), f"Seems your inp shape not equal to your Det input hw, please check. {inp.shape} vs {self.input_height}x{self.input_width}"
        if self.timing:
            t0 = time.perf_counter()
        res = self.infer_wrapper.infer(inp)
        if self.timing:
            t1 = time.perf_counter()
            self.frame_time_cost = round(t1 - t0, 3)

        boxes = None
        scores = None
        labels = None

        if self.backend == Backends.CPU_ORT:
            # solving ORT outputs
            if self.do_nms:
                # assue output like [1, 10647, 16]
                # [1, 25200, 21] for yolov7-face
                res = res["output"]
                boxes, scores, labels = self.do_nms_postprocess(res, ori_h, ori_w)
                # print(f"boxes: {boxes.shape}, scores: {scores.shape}, labels: {labels.shape}")
            else:
                if isinstance(res, dict):
                    # as boxes, scores, labels order
                    boxes = res["boxes"]
                    labels = res["labels"]
                    if "scores" in res.keys():
                        scores = res["scores"]
                    else:
                        scores = boxes[..., -1]
                        boxes = boxes[..., :-1]

                    shs = res["boxes"].shape
                    if len(shs) > 2:
                        n = shs[1]
                        if shs[0] == 1:
                            # if only one batch
                            boxes = boxes[0]
                            scores = scores[0]
                            labels = labels[0]

        elif self.backend == Backends.GPU_TENSORRT:
            """
            typically output of TensorRT should be:
            n: 1, 14
            boxes: 1, 100, 4
            scores: 1, 100
            labels: 1, 100
            """
            # solving TRT outputs
            shs = res[1].shape
            if len(shs) > 2:
                # TODO: add multi-batch supported here.
                n = np.squeeze(res[0], axis=-1)[0]
                if shs[0] == 1:
                    boxes = res[1][0][:n]
                    scores = res[2][0][:n]
                    labels = res[3][0][:n]
                else:
                    boxes = res[1][:n]
                    scores = res[2][:n]
                    labels = res[3][:n]
            else:
                n = res[0]
                boxes = res[1][:n]
                scores = res[2][:n]
                labels = res[3][:n]
        else:
            ValueError(f"Backend {self.backend} not implemented for Det infer")

        # finally get boxes, scores, labels
        boxes, scores, labels = self.postprocess(ori_h, ori_w, boxes, scores, labels)
        return boxes, scores, labels

    def load_inputs(self, im, normalize_255=False, is_rgb=True):
        self.crt_image_raw_h = im.shape[0]
        self.crt_image_raw_w = im.shape[1]
        return load_inputs(
            im,
            self.input_height,
            self.input_width,
            normalize_255=normalize_255,
            is_rgb=is_rgb,
        )

    def do_nms_postprocess(self, outs, ori_h, ori_w, type="yolo-face"):
        confidences = []
        boxes = []
        class_ids = []
        landmarks = []
        ratioh, ratiow = ori_h / self.input_height, ori_w / self.input_width
        if len(outs.shape) > 2:
            # get batch out
            outs = outs[0]
        # we might have different type for post-process
        if type == "yolo-face":
            for detection in outs:
                if len(detection) == 21:
                    # yolov7 face
                    # 21 corresponds to: 1 channel, 4 bounding box, 1 score, 15 landmarks
                    confidence = detection[5]
                else:
                    confidence = detection[15]
                # if confidence > self.confThreshold and detection[4] > self.objThreshold:
                # if float(confidence) > self.score_thr:
                # this objness
                if detection[4] > 0.5:
                    cx = detection[0]
                    cy = detection[1]
                    w = detection[2]
                    h = detection[3]
                    left = int(cx - w / 2)
                    top = int(cy - h / 2)

                    confidences.append(float(confidence))
                    boxes.append([left, top, w, h])
                    class_ids.append(0)
                    landmark = detection[5:15] * np.tile(
                        np.float32([ratiow, ratioh]), 5
                    )
                    landmarks.append(landmark.astype(np.int32))
        else:
            raise ValueError(f"{type} not supported now, only yolo-face support")

        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.score_thr, self.nms_thr)
        boxes = np.array(boxes)
        confidences = np.array(confidences)
        class_ids = np.array(class_ids)

        boxes = boxes[indices]
        class_ids = class_ids[indices]
        confidences = confidences[indices]
        if len(boxes) > 0:
            boxes = ltwh_to_x1y1x2y2(boxes)
        return boxes, confidences, class_ids

    def postprocess(self, ori_h, ori_w, boxes, scores, labels):
        """
        rescale box,
        and return final:
        boxes, scores, labels in order
        """
        if len(boxes) > 0:
            boxes = rescale_boxes(
                boxes, ori_h, ori_w, self.input_height, self.input_width
            )
            # filter again on score
            idx = scores > self.score_thr
            boxes = boxes[idx]
            scores = scores[idx]
            labels = labels[idx]
        return boxes, scores, labels

    def vis_res(
        self,
        img: Union[np.ndarray, Image.Image],
        bboxes,
        scores,
        labels=None,
        track_ids=None,
        class_names=None,
        transparent=False,
    ):
        from alfred.vis.image.det import visualize_det_cv2_part

        if isinstance(img, Image.Image):
            img = ensure_pil_bgr(img)
        else:
            # np.ndarray also need ensure bgr for cv2 to visualize
            img = ensure_ndarray_bgr(img)

        img = visualize_det_cv2_part(
            img,
            scores,
            labels,
            bboxes,
            thresh=self.score_thr,
            track_ids=track_ids,
            class_names=class_names,
            font_scale=0.8,
            line_thickness=2,
            show_time=self.frame_time_cost,
            transparent=transparent,
        )
        return img
