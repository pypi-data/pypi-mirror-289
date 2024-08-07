from enum import Enum


class Backends(Enum):
    GPU_TENSORRT = 1
    CPU_XNNPACK = 2
    CPU_OPENVINO = 3
    CPU_TVM = 4
    CPU_ORT = 5
    AUTO = 6
    GPU_ORT = 7
    CPU_MNN = 8
    CPU_PPLNN = 9
    GPU_PPLNN = 10

    @staticmethod
    def from_str(s: str):
        if s.lower() == 'tensorrt' or s.lower() == 'trt':
            return Backends.GPU_TENSORRT
        elif 'ort' in s.lower() or 'onnxruntime' in s.lower():
            if 'gpu' in s.lower():
                return Backends.GPU_ORT
            else:
                return Backends.CPU_ORT
        elif s.lower() == 'tvm':
            return Backends.CPU_TVM
        elif s.lower() == 'openvino':
            return Backends.CPU_OPENVINO
        elif s.lower() == 'auto':
            return Backends.AUTO
        elif s.lower() == 'gpu_ort':
            return Backends.GPU_ORT
        elif s.lower() == 'mnn':
            return Backends.CPU_MNN
        elif s.lower() == 'pplnn_cpu':
            return Backends.CPU_PPLNN
        elif s.lower() == 'pplnn_gpu':
            return Backends.GPU_PPLNN
        else:
            return Backends.AUTO

    def __str__(self) -> str:
        if self.value == 1:
            return 'trt'
        elif self.value == 2:
            return 'cpu'
        elif self.value == 5:
            return 'ort'
        elif self.value == 6:
            return 'auto'
        elif self.value == 7:
            return 'gpu_ort'
        elif self.value == 9:
            return 'ppl_cpu'
        elif self.value == 10:
            return 'ppl_gpu'
        else:
            return 'cpu'