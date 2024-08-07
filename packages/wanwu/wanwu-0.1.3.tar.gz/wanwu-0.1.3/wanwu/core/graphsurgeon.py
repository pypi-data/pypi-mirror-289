# Copyright (c) 2022 Lucas Jin. All rights reserved.
#
# This source code is licensed under the GPL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
#
# Copyright (c) 2021, NVIDIA CORPORATION. All rights reserved.
#
# This source code is licensed under the Apache-2.0 license found in the
# LICENSE file in the root directory of TensorRT source tree.
#

from pathlib import Path

import numpy as np
import onnx
from onnx import shape_inference
from typing import Any, List, Text, Dict, Set
from onnx import ModelProto, ValueInfoProto

import onnx.checker
from alfred.utils.log import logger

try:
    import onnx_graphsurgeon as gs
except ImportError:
    logger.warning('onnx_graphsurgeon is not installed, not do surgeon.')
    gs = None

"""
this file try surgeon on normal Detection onnx model
and add BatchedNMS plugin to it.
"""


# type: (ModelProto, Dict[Text, List[Any]], Dict[Text, List[Any]]) -> ModelProto
def update_inputs_outputs_dims(model, input_dims, output_dims=None):
    """
        This function updates the dimension sizes of the model's inputs and outputs to the values
        provided in input_dims and output_dims. if the dim value provided is negative, a unique dim_param
        will be set for that dimension.

        Example. if we have the following shape for inputs and outputs:
                shape(input_1) = ('b', 3, 'w', 'h')
                shape(input_2) = ('b', 4)
                and shape(output)  = ('b', 'd', 5)

            The parameters can be provided as:
                input_dims = {
                    "input_1": ['b', 3, 'w', 'h'],
                    "input_2": ['b', 4],
                }
                output_dims = {
                    "output": ['b', -1, 5]
                }

            Putting it together:
                model = onnx.load('model.onnx')
                updated_model = update_inputs_outputs_dims(model, input_dims, output_dims)
                onnx.save(updated_model, 'model.onnx')
    """
    dim_param_set = set()  # type: Set[Text]

    # type: (Set[Text], List[ValueInfoProto]) -> None
    def init_dim_param_set(dim_param_set, value_infos):
        for info in value_infos:
            shape = info.type.tensor_type.shape
            for dim in shape.dim:
                if dim.HasField('dim_param'):
                    dim_param_set.add(dim.dim_param)  # type: ignore

    init_dim_param_set(dim_param_set, model.graph.input)  # type: ignore
    init_dim_param_set(dim_param_set, model.graph.output)  # type: ignore
    init_dim_param_set(dim_param_set, model.graph.value_info)  # type: ignore

    def update_dim(tensor, dim, j, name):  # type: (ValueInfoProto, Any, int, Text) -> None
        dim_proto = tensor.type.tensor_type.shape.dim[j]
        if isinstance(dim, int):
            if dim >= 0:
                if dim_proto.HasField('dim_value') and dim_proto.dim_value != dim:
                    raise ValueError('Unable to set dimension value to {} for axis {} of {}. Contradicts existing dimension value {}.'
                                     .format(dim, j, name, dim_proto.dim_value))
                dim_proto.dim_value = dim
            else:
                generated_dim_param = name + '_' + str(j)
                if generated_dim_param in dim_param_set:
                    raise ValueError('Unable to generate unique dim_param for axis {} of {}. Please manually provide a dim_param value.'
                                     .format(j, name))
                dim_proto.dim_param = generated_dim_param
        elif isinstance(dim, str):
            dim_proto.dim_param = dim
        else:
            raise ValueError(
                'Only int or str is accepted as dimension value, incorrect type: {}'.format(type(dim)))
    
    new_batch_size = 1
    for input in model.graph.input:
        input_name = input.name
        input_dim_arr = input_dims[input_name]
        new_batch_size = input_dim_arr[0]
        for j, dim in enumerate(input_dim_arr):
            update_dim(input, dim, j, input_name)

    if output_dims is not None:
        for output in model.graph.output:
            output_name = output.name
            output_dim_arr = output_dims[output_name]
            for j, dim in enumerate(output_dim_arr):
                update_dim(output, dim, j, output_name)
    else:
        # only update output on batchSize
        logger.info('updating onnx model output batchsize to: {}'.format(new_batch_size))
        for output in model.graph.output:
            output_name = output.name
            update_dim(output, new_batch_size, 0, output_name)
    onnx.checker.check_model(model)
    return model


def get_inputs(model: onnx.ModelProto) -> List[onnx.ValueInfoProto]:
    initializer_names = [x.name for x in model.graph.initializer]
    return [ipt for ipt in model.graph.input if ipt.name not in initializer_names]


def is_model_dynamic_on_hw(model):
    _inputs = get_inputs(model)
    input_specs = dict()

    for _input in _inputs:
        tensor_type = _input.type.tensor_type
        sh = []
        # check if it has a shape:
        if (tensor_type.HasField("shape")):
            # iterate through dimensions of the shape:
            for d in tensor_type.shape.dim:
                # the dimension may have a definite (integer) value or a symbolic identifier or neither:
                if (d.HasField("dim_value")):
                    sh.append(d.dim_value)
                elif (d.HasField("dim_param")):
                    sh.append(-1)
                else:
                    sh.append('?')
            input_specs[_input.name] = sh
        else:
            print("unknown rank", end="")
    # logger.info(f'input shapes: {input_specs}')
    # check input0
    a = list(input_specs.values())[0]
    if a[-2] == -1:
        return True
    else:
        return False


def is_model_dynamic_on_batch(onnx_model):
    _inputs = get_inputs(onnx_model)
    input_specs = dict()

    for _input in _inputs:
        tensor_type = _input.type.tensor_type
        sh = []
        # check if it has a shape:
        if (tensor_type.HasField("shape")):
            # iterate through dimensions of the shape:
            for d in tensor_type.shape.dim:
                # the dimension may have a definite (integer) value or a symbolic identifier or neither:
                if (d.HasField("dim_value")):
                    sh.append(d.dim_value)
                elif (d.HasField("dim_param")):
                    sh.append(-1)
                else:
                    sh.append('?')
            input_specs[_input.name] = sh
        else:
            print("unknown rank", end="")
    a = list(input_specs.values())[0]
    if a[0] == -1:
        return True, input_specs
    else:
        return False, None


class OnnxModelSurgeonOperationer:
    """
    Surgeon normal detection model, attach different NMS plugin based on backend
    """

    def __init__(
        self,
        onnx_path: str,
        num_classes: int,
        enable_dynamic: bool = True,
        batch_size: int = 1,
    ):
        onnx_path = Path(onnx_path)
        assert onnx_path.exists()

        self.num_classes = num_classes

        self.onnx_path = onnx_path
        logger.info(f"Loaded origin onnx model from {onnx_path}")

        self.onnx_model = onnx.load(onnx_path)
        self.is_dynamic_on_hw = is_model_dynamic_on_hw(self.onnx_model)
        self.is_dynamic_on_batch, self.inputs_dict = is_model_dynamic_on_batch(self.onnx_model)
        
        if gs is not None:
            self.graph = gs.import_onnx(self.onnx_model)
            assert self.graph
            logger.info("ONNX graph created successfully")

            # Fold constants via ONNX-GS that PyTorch2ONNX may have missed
            self.graph.fold_constants()
            self.batch_size = batch_size

            self.input_name = self.graph.inputs[0].name
            self.ok = True
        else:
            self.ok = False

    def infer(self):
        """
        Sanitize the graph by cleaning any unconnected nodes, do a topological resort,
        and fold constant inputs values. When possible, run shape inference on the
        ONNX graph to determine tensor shapes.
        """
        for _ in range(3):
            count_before = len(self.graph.nodes)

            self.graph.cleanup().toposort()
            try:
                for node in self.graph.nodes:
                    for o in node.outputs:
                        o.shape = None
                model = gs.export_onnx(self.graph)
                model = shape_inference.infer_shapes(model)
                self.graph = gs.import_onnx(model)
            except Exception as e:
                logger.info(
                    f"Shape inference could not be performed at this time:\n{e}")
            try:
                self.graph.fold_constants(fold_shapes=True)
            except TypeError as e:
                logger.error(
                    "This version of ONNX GraphSurgeon does not support folding shapes, "
                    f"please upgrade your onnx_graphsurgeon module. Error:\n{e}"
                )
                raise

            count_after = len(self.graph.nodes)
            if count_before == count_after:
                # No new folding occurred in this iteration, so we can stop for now.
                break

    def save(self, output_path=None):
        """
        Save the ONNX model to the given location.

        Args:
            output_path: Path pointing to the location where to write
                out the updated ONNX model.
        """
        if output_path is None:
            output_path = self.onnx_path.with_name(
                self.onnx_path.stem + '_w_nms' + self.onnx_path.suffix)
        if gs is not None:
            self.graph.cleanup().toposort()
            model = gs.export_onnx(self.graph)
            onnx.save(model, output_path)
            logger.info(f"Saved ONNX model to {output_path}")
            return output_path, model
        else:
            return output_path, self.onnx_model

    def update_inputs_dims(self, batch_size=1, input_height=512, input_width=608):
        if self.is_dynamic_on_hw:
            updated_model = update_inputs_outputs_dims(self.onnx_model,
                                                       {self.input_name: [batch_size, 3, input_height, input_width]})
            # update surgeon graph
            self.graph = gs.import_onnx(updated_model)
            logger.info('Updated model inputs...')
        # else:
        #     logger.info(
        #         '.')

    def register_trt_batched_nms(
        self,
        score_thresh: float = 0.25,
        nms_thresh: float = 0.45,
        detections_per_img: int = 100,
        normalized: bool = True,
    ):
        """
        Register the ``BatchedNMS_TRT`` plugin node.

        NMS expects these shapes for its input tensors:
            - box_net: [batch_size, number_boxes, 1, 4]
            - class_net: [batch_size, number_boxes, number_labels]

        Args:
            score_thresh (float): The scalar threshold for score (low scoring boxes are removed).
            nms_thresh (float): The scalar threshold for IOU (new boxes that have high IOU
                overlap with previously selected boxes are removed).
            detections_per_img (int): Number of best detections to keep after NMS.
            normalized (bool): Set to false if the box coordinates are not normalized,
                meaning they are not in the range [0,1]. Defaults: True.
        """

        self.infer()
        # Find the concat node at the end of the network
        nms_inputs = self.graph.outputs
        op = "BatchedNMS_TRT"
        attrs = {
            "plugin_version": "1",
            "shareLocation": True,
            "backgroundLabelId": -1,  # no background class
            "numClasses": self.num_classes,
            "topK": 1024,
            "keepTopK": detections_per_img,
            "scoreThreshold": score_thresh,
            "iouThreshold": nms_thresh,
            "isNormalized": normalized,
            "clipBoxes": False,
        }

        # NMS Outputs
        output_num_detections = gs.Variable(
            name="num_detections",
            dtype=np.int32,
            shape=[self.batch_size, 1],
        )  # A scalar indicating the number of valid detections per batch image.
        output_boxes = gs.Variable(
            name="detection_boxes",
            dtype=np.float32,
            shape=[self.batch_size, detections_per_img, 4],
        )
        output_scores = gs.Variable(
            name="detection_scores",
            dtype=np.float32,
            shape=[self.batch_size, detections_per_img],
        )
        output_labels = gs.Variable(
            name="detection_classes",
            dtype=np.float32,
            shape=[self.batch_size, detections_per_img],
        )

        nms_outputs = [output_num_detections,
                       output_boxes, output_scores, output_labels]

        # Create the NMS Plugin node with the selected inputs. The outputs of the node will also
        # become the final outputs of the graph.
        self.graph.layer(
            op=op,
            name="batched_nms",
            inputs=nms_inputs,
            outputs=nms_outputs,
            attrs=attrs,
        )
        logger.info(
            f"Created NMS plugin '{op}' with attributes: {attrs}, using BatchSize: {self.batch_size}")
        self.graph.outputs = nms_outputs
        self.infer()

    def register_trt_efficient_nms(
        self,
        score_thresh: float = 0.25,
        nms_thresh: float = 0.45,
        detections_per_img: int = 100,
    ):
        """
        Register the ``EfficientNMS_TRT`` plugin node.

        NMS expects these shapes for its input tensors:
            - box_net: [batch_size, number_boxes, 4]
            - class_net: [batch_size, number_boxes, number_labels]

        Args:
            score_thresh (float): The scalar threshold for score (low scoring boxes are removed).
            nms_thresh (float): The scalar threshold for IOU (new boxes that have high IOU
                overlap with previously selected boxes are removed).
            detections_per_img (int): Number of best detections to keep after NMS.
        """

        self.infer()
        # Find the concat node at the end of the network
        nms_inputs = self.graph.outputs

        op = "EfficientNMS_TRT"
        attrs = {
            "plugin_version": "1",
            "background_class": -1,  # no background class
            "max_output_boxes": detections_per_img,
            "score_threshold": score_thresh,
            "iou_threshold": nms_thresh,
            "score_activation": False,
            "box_coding": 0,
        }

        # NMS Outputs
        output_num_detections = gs.Variable(
            name="num_detections",
            dtype=np.int32,
            shape=[self.batch_size, 1],
        )  # A scalar indicating the number of valid detections per batch image.
        output_boxes = gs.Variable(
            name="detection_boxes",
            dtype=np.float32,
            shape=[self.batch_size, detections_per_img, 4],
        )
        output_scores = gs.Variable(
            name="detection_scores",
            dtype=np.float32,
            # dtype=np.float16,
            shape=[self.batch_size, detections_per_img],
        )
        output_labels = gs.Variable(
            name="detection_classes",
            dtype=np.int32,
            shape=[self.batch_size, detections_per_img],
        )

        nms_outputs = [output_num_detections,
                       output_boxes, output_scores, output_labels]

        # Create the NMS Plugin node with the selected inputs. The outputs of the node will also
        # become the final outputs of the graph.
        self.graph.layer(
            op=op,
            name="batched_nms",
            inputs=nms_inputs,
            outputs=nms_outputs,
            attrs=attrs,
        )
        logger.info(
            f"Created Efficient NMS plugin '{op}' with attributes: {attrs}")
        self.graph.outputs = nms_outputs
        self.infer()

    def register_onnx_nonmaxsuppression(
        self,
        score_thresh: float = 0.25,
        iou_threshold: float = 0.45,
        max_output_boxes_per_class: int = 100,
        normalized: bool = True,
    ):
        """
        Register the ``NonMaxSuppression`` node

        WARN: this is not supported yet, seems it using different inputs with TRT

        NMS expects these shapes for its input tensors:
            - boxes: [batch_size, number_boxes, 4]
            - scores: [batch_size, number_labels, number_boxes]
        the scores last 2 dimension is opposite with EfficientNMS
        """

        self.infer()
        # Find the concat node at the end of the network
        nms_inputs = self.graph.outputs
        op = "NonMaxSuppression"
        attrs = {
            "plugin_version": "1",
            "shareLocation": True,
            "backgroundLabelId": -1,  # no background class
            "numClasses": self.num_classes,
            "topK": 1024,
            "max_output_boxes_per_class": max_output_boxes_per_class,
            "score_thresh": score_thresh,
            "iou_threshold": iou_threshold,
            "isNormalized": normalized,
            "clipBoxes": False,
        }

        # NMS Outputs
        output_num_detections = gs.Variable(
            name="num_detections",
            dtype=np.int32,
            shape=[self.batch_size, 1],
        )  # A scalar indicating the number of valid detections per batch image.
        output_boxes = gs.Variable(
            name="detection_boxes",
            dtype=np.float32,
            shape=[self.batch_size, max_output_boxes_per_class, 4],
        )
        output_scores = gs.Variable(
            name="detection_scores",
            dtype=np.float32,
            shape=[self.batch_size, max_output_boxes_per_class],
        )
        output_labels = gs.Variable(
            name="detection_classes",
            dtype=np.float32,
            shape=[self.batch_size, max_output_boxes_per_class],
        )

        nms_outputs = [output_num_detections,
                       output_boxes, output_scores, output_labels]

        # Create the NMS Plugin node with the selected inputs. The outputs of the node will also
        # become the final outputs of the graph.
        self.graph.layer(
            op=op,
            name="batched_nms",
            inputs=nms_inputs,
            outputs=nms_outputs,
            attrs=attrs,
        )
        logger.info(f"Created NMS plugin '{op}' with attributes: {attrs}")

        self.graph.outputs = nms_outputs

        self.infer()
