from typing import Dict
import numpy as np
from alfred.utils.log import logger
import os
from abc import ABC, abstractclassmethod


class TensorInfo:
    def __init__(self, shape, dtype) -> None:
        self.shape = shape
        self.dtype = dtype


class WrapperBase:
    @abstractclassmethod
    def infer(self, inputs, return_dict=True):
        NotImplemented

    @abstractclassmethod
    def get_inputs_dict(self) -> Dict[str, TensorInfo]:
        NotImplemented

    @abstractclassmethod
    def get_outputs_dict(self) -> Dict[str, TensorInfo]:
        NotImplemented
