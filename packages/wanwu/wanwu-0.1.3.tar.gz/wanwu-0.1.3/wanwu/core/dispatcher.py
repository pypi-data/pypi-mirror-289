'''
auto detect backend to use
logic:

if GPU:
    if tensorrt installed:
        tensorrt
    else:
        ort gpu
else:
    if openvino installed:
        openvino
    else:
        ort
'''
from ast import Import
from math import fabs
from typing import List
import wanwu.utils.gpu_utils as gpu_utils
from wanwu.core.enums import Backends
from alfred.utils.log import logger


def print_gpus_info(gpus: List[gpu_utils.GPU]):
    logger.info('Located GPU info: ')
    for g in gpus:
        logger.info(f'  {g.name}, {g.memoryUsed}MB/{g.memoryTotal}MB')


def dispatcher_on_device_auto():
    """
    return the fastest backend based on currently hardware and software
    """
    gpus = gpu_utils.getGPUs()
    if len(gpus) > 0:
        # check if tensorrt installed
        print_gpus_info(gpus)
        try:
            import tensorrt
            logger.info('Auto switching backend to TensorRT.')
            return Backends.GPU_TENSORRT
        except ImportError:
            # tensorrt not install
            logger.info(
                'Not found TensorRT installed, fallback to default CUDA, this might not fastest.')
            return Backends.GPU_ORT
    else:
        try:
            import openvino
            return Backends.CPU_OPENVINO
        except ImportError:
            logger.info('openvino not installed, fallback to normal CPU.')
            return Backends.CPU_ORT


def check_backend_support_on_host(b: Backends):
    if b == Backends.GPU_TENSORRT:
        try:
            from wanwu.core.backends.trt import TensorRTInferencer
            return True
        except ImportError as e:
            logger.warning(f'import trt error: {e}')
            return False
    elif b == Backends.CPU_ORT:
        try:
            import onnxruntime
            return True
        except ImportError:
            return False
    elif b == Backends.CPU_MNN:
        try:
            import MNN
            return True
        except ImportError:
            return False
    elif b == Backends.CPU_PPLNN:
        try:
            import pyppl
            return True 
        except ImportError:
            return False
    elif b == Backends.CPU_OPENVINO:
        try:
            from openvino import runtime
            return True
        except ImportError:
            return False
    return False
