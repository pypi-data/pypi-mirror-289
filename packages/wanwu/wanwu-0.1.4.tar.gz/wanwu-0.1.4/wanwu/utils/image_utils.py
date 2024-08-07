import numpy as np
from PIL import Image

try:
    import torch
    import cv2
    from torch import Tensor
except ImportError as e:
    torch = None
    cv2 = None
    Tensor = None


def read_image_to_tensor(
    image: np.ndarray,
    is_half: bool = False,
) -> Tensor:
    """
    Parse an image to Tensor.

    Args:
        image (np.ndarray): the candidate ndarray image to be parsed to Tensor.
        is_half (bool): whether to transfer image to half. Default: False.
    """
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = np.ascontiguousarray(image, dtype=np.float32)  # uint8 to float32
    image = np.transpose(image / 255.0, [2, 0, 1])

    image = torch.from_numpy(image)
    image = image.half() if is_half else image.float()
    return image


def load_inputs(
    image, input_height, input_width, normalize_255=True, transpose=True, is_rgb=False
):
    if is_rgb:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (input_width, input_height))
    image = np.ascontiguousarray(image, dtype=np.float32)  # uint8 to float32
    if transpose:
        if normalize_255:
            image = np.transpose(image / 255.0, [2, 0, 1])
        else:
            image = np.transpose(image, [2, 0, 1])
    image = np.expand_dims(image, axis=0)
    return image


def load_inputs_naive(
    image, input_height, input_width, normalize_255=True, transpose=True
):
    """
    the image must be in RGB order
    """
    image = cv2.resize(image, (input_width, input_height))
    image = np.ascontiguousarray(image, dtype=np.float32)  # uint8 to float32
    if transpose:
        if normalize_255:
            image = np.transpose(image / 255.0, [2, 0, 1])
        else:
            image = np.transpose(image, [2, 0, 1])
    image = np.expand_dims(image, axis=0)
    return image


def load_inputs_std_mean(
    image, input_height, input_width, std=1, mean=0, transpose=True, is_rgb=False
):
    if is_rgb:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (input_width, input_height))
    image = np.ascontiguousarray(image, dtype=np.float32)  # uint8 to float32

    image = image.astype(np.float32)
    image -= mean
    image /= std
    if transpose:
        image = np.transpose(image, [2, 0, 1])
    image = np.expand_dims(image, axis=0)
    return image


def rescale_boxes(boxes, ori_h, ori_w, inp_h, inp_w):
    scale_x = ori_w * 1.0 / inp_w
    scale_y = ori_h * 1.0 / inp_h
    boxes[..., 0] *= scale_x
    boxes[..., 2] *= scale_x
    boxes[..., 1] *= scale_y
    boxes[..., 3] *= scale_y
    return boxes


def ensure_pil_bgr(image: Image.Image) -> np.ndarray:
    image_array = np.array(image)

    if image_array.shape[-1] == 3 and np.array_equal(
        image_array[..., :3], image_array[..., ::-1]
    ):
        return np.ascontiguousarray(image_array)

    bgr_array = image_array[..., ::-1]
    return np.ascontiguousarray(bgr_array)


def ensure_ndarray_bgr(image: np.ndarray) -> np.ndarray:
    if image.shape[-1] == 3 and np.array_equal(image[..., :3], image[..., ::-1]):
        return np.ascontiguousarray(image)

    bgr_array = image[..., ::-1]
    return np.ascontiguousarray(bgr_array)
