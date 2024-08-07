from wanwu.utils.image_utils import load_inputs_std_mean
from ..core.infer import Backends, BaseInfer
from ..core.modelloader import ModelLoader, TaskType
import time
import numpy as np
from .utils import box2cs, get_affine_transform, transform_preds_batch
from wanwu.base.base_task import TaskBase
import numpy as np
from wanwu import Det
from wanwu.track.deepsort import DeepSort
from alfred import logger
try:
    import cv2
except ImportError as e:
    cv2 = None


class Keypoints(BaseInfer):
    def __init__(
        self,
        onnx_f: str = None,
        backend: Backends = Backends.CPU_ORT,
        type: str = "alphapose_r50",
        batch_size=1,
        input_width=640,
        input_height=512,
        num_classes=80,
        fp16=False,
        timing=False,
        **kargs,
    ) -> None:
        super(Keypoints, self).__init__(
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
            task_type=TaskType.KPS,
            fp16=fp16,
            num_classes=self.num_classes,
            batch_size=self.batch_size,
            input_width=self.input_width,
            input_height=self.input_height,
        )
        self.infer_wrapper = self.model_loader.get_infer_wrapper()
        self.pose_input_size = [self.input_height, self.input_width]

    def get_croped_images(self, boxes, ori_img):
        batch_images = []
        batch_centers = []
        batch_scales = []
        for box in boxes:
            c, s = box2cs(self.pose_input_size[::-1], box)
            batch_centers.append(c)
            batch_scales.append(s)
            # tt = time.perf_counter()
            trans = get_affine_transform(c, s, 0, self.pose_input_size[::-1])
            crop = cv2.warpAffine(
                ori_img, trans, self.pose_input_size[::-1], flags=cv2.INTER_LINEAR
            )
            # Alphapose using RGB as input
            crop = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
            # ttt = time.perf_counter()
            # print(ttt -tt)
            crop = crop.astype(np.float32)
            batch_images.append(crop)
        return (
            np.array(batch_images).astype(np.float32),
            np.array(batch_centers),
            np.array(batch_scales),
        )

    def infer(self, raw_img, boxes):
        """
        this only for bottom up keypoints model which using boxes crop image patch first
        the send into keypoints detection model

        CAUTION: all keypoints model must wrap HWC=>CHW into model inside
        """
        if self.timing:
            t0 = time.perf_counter()
        batched_inputs, batch_centers, batch_scales = self.get_croped_images(
            boxes, raw_img
        )
        # print(batched_inputs.shape)
        res = self.infer_wrapper.infer(batched_inputs)
        if self.timing:
            t1 = time.perf_counter()
            self.frame_time_cost = round(t1 - t0, 3)
        # hardcoded on onnx model
        if isinstance(res, dict):
            cords = res["coords"]
            scores = res["maxvals"]
        else:
            # TensorRT returns list
            cords = res[1]
            scores = res[0]
            # print(cords.shape)
            # print(scores.shape)
        cords = self.postprocess(cords, batch_centers, batch_scales)
        return cords, scores

    def postprocess(self, outs, batch_centers, batch_scales):
        preds = transform_preds_batch(
            outs,
            batch_centers,
            batch_scales,
            (self.pose_input_size[1] // 4, self.pose_input_size[0] // 4),
        )
        return preds

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


class TopDownKptsDetector(TaskBase):
    def __init__(self, kpts_model_f=None, track=False, **args) -> None:
        super(TopDownKptsDetector, self).__init__(**args)

        self.det = Det(
            type="yolox_tiny_coco",
            onnx_f=self.onnx_f,
            backend=self.backend,
            input_height=416,
            input_width=416,
            score_thr=0.45,
            fp16=False,
            timing=True,
        )
        self.kps = Keypoints(
            type="alp_halpe26_res50",
            onnx_f=kpts_model_f,
            backend=Backends.AUTO,
            input_height=256,
            input_width=192,
        )
        self.track = track
        if track:
            logger.info("Enabled tracking.")
            self.deepsort = DeepSort(
                Backends.AUTO, max_dist=0.4, max_iou_distance=0.8, max_age=20
            )

    def infer(self, im):
        inp = self.det.load_inputs(im, normalize_255=False, is_rgb=True)
        boxes, scores, labels = self.det.infer(inp, im.shape[0], im.shape[1])
        if self.track:
            boxes, track_ids, labels = self.deepsort.update(boxes, scores, labels, im)
        else:
            track_ids = None

        mask_idx = labels == 0
        boxes = boxes[mask_idx]

        if boxes.shape[0] > 0:
            kps_coords, score_kps = self.kps.infer(im, boxes)
        else:
            kps_coords = None
            score_kps = None
        return boxes, scores, labels, kps_coords, score_kps, track_ids
