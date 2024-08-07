"""

We using a very simple feature extractor model
for appearance extraction, and using for matching
in do tracking.

It was barely based on DeepSort machanism.

"""
import numpy as np
from wanwu.core.enums import Backends

from .matching import NearestNeighborDistanceMetric
from .tracker import Tracker, Detection
from .reid import ReIDFeatureExtractor

__all__ = ["DeepSort"]


class DeepSort(object):
    def __init__(
        self,
        backend=Backends.AUTO,
        max_dist=0.2,
        max_iou_distance=0.7,
        max_age=70,
        n_init=3,
        nn_budget=100,
    ):

        self.extractor = ReIDFeatureExtractor(backend)
        self.height = 512
        self.width = 512

        max_cosine_distance = max_dist
        metric = NearestNeighborDistanceMetric(
            "euclidean", max_cosine_distance, nn_budget
        )
        self.tracker = Tracker(
            metric, max_iou_distance=max_iou_distance, max_age=max_age, n_init=n_init
        )

    def update(self, bbox_xyxy, confidences, classes, ori_img, use_yolo_preds=False):
        """
        boxes-in is xyxy order
        """
        if isinstance(bbox_xyxy, np.ndarray):
            bbox_xyxy = np.array(bbox_xyxy)
        bbox_xyxy = bbox_xyxy.astype(int)
        self.height, self.width = ori_img.shape[:2]
        # generate detections
        features = self._get_features(bbox_xyxy, ori_img)
        bbox_tlwh = self._xyxy_to_x1y1wh(bbox_xyxy)
        detections = [
            Detection(bbox_tlwh[i], conf, features[i])
            for i, conf in enumerate(confidences)
        ]

        # update tracker
        self.tracker.predict()
        self.tracker.update(detections, classes)

        # output bbox identities
        track_boxes = []
        track_ids = []
        track_labels = []
        for track in self.tracker.tracks:
            if not track.is_confirmed() or track.time_since_update > 1:
                continue
            box = track.to_tlwh()
            x1, y1, x2, y2 = self._tlwh_to_xyxy_single(box)
            track_id = track.track_id
            class_id = track.class_id

            track_boxes.append([x1, y1, x2, y2])
            track_ids.append(track_id)
            track_labels.append(class_id)

        if len(track_ids) > 0:
            track_boxes = np.stack(track_boxes, axis=0)
        return track_boxes, track_ids, track_labels

    def increment_ages(self):
        self.tracker.increment_ages()

    def _get_features(self, bbox_xyxy, ori_img):
        im_crops = []
        bbox_xyxy[:, :2] = bbox_xyxy[:, :2].clip(0)
        for box in bbox_xyxy:
            x1, y1, x2, y2 = box
            im = ori_img[y1:y2, x1:x2]
            im_crops.append(im)
        if im_crops:
            features = self.extractor.extract(im_crops)
        else:
            features = np.array([])
        return features

    def _tlwh_to_xyxy_single(self, bbox_tlwh):
        x, y, w, h = bbox_tlwh
        x1 = max(int(x), 0)
        x2 = min(int(x + w), self.width - 1)
        y1 = max(int(y), 0)
        y2 = min(int(y + h), self.height - 1)
        return x1, y1, x2, y2

    @staticmethod
    def _tlwh_to_xyxy(bbox_tlwh):
        if len(bbox_tlwh.shape) < 2:
            bbox_tlwh = np.expand_dims(bbox_tlwh, axis=0)
        t = bbox_tlwh[:, 0]
        l = bbox_tlwh[:, 1]
        bbox_tlwh[:, 2] = l + bbox_tlwh[:, 2]
        bbox_tlwh[:, 3] = t + bbox_tlwh[:, 3]
        bbox_tlwh[:, 0] = l
        bbox_tlwh[:, 1] = t
        return bbox_tlwh

    @staticmethod
    def _xyxy_to_x1y1wh(bbox_xyxy):
        if len(bbox_xyxy.shape) < 2:
            bbox_xyxy = np.expand_dims(bbox_xyxy, axis=0)
        x1 = bbox_xyxy[:, 0].clip(0)
        y1 = bbox_xyxy[:, 1].clip(0)
        bbox_xyxy[:, 2] = bbox_xyxy[:, 2] - x1
        bbox_xyxy[:, 3] = bbox_xyxy[:, 3] - y1
        return bbox_xyxy
