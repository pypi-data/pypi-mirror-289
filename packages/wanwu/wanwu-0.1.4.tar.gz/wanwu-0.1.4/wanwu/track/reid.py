from wanwu.cls.cls import Classify
from wanwu.core.cellar import model_urls
from wanwu.core.enums import Backends
import numpy as np


class ReIDFeatureExtractor:
    def __init__(self, backend: Backends) -> None:
        self.model = Classify(
            type="reid_osnet_x0_25", backend=backend, input_height=256, input_width=128
        )

    def extract(self, imgs):
        """
        imgs should be NDArray or list of arrays

        ONNX model already solves permute and normalization
        """
        imgs_input = []
        for im in imgs:
            im = self.model.load_inputs(im, transpose=False, is_rgb=True)
            imgs_input.append(im)
        feas = self.model.infer(imgs_input)
        if isinstance(feas, dict):
            feas = feas["feas"]
        else:
            feas = feas[0]
            if len(feas.shape) > 2:
                feas = np.squeeze(feas, axis=1)
        return feas
