import numpy as np


def ltwh_to_x1y1x2y2(boxes):
    # Ensure the input is a numpy array
    boxes = np.array(boxes)

    # Create a new array for the output
    new_boxes = np.zeros_like(boxes)

    # Set x1 and y1
    new_boxes[:, 0] = boxes[:, 0]  # x1 = left
    new_boxes[:, 1] = boxes[:, 1]  # y1 = top

    # Set x2 and y2
    new_boxes[:, 2] = boxes[:, 0] + boxes[:, 2]  # x2 = left + width
    new_boxes[:, 3] = boxes[:, 1] + boxes[:, 3]  # y2 = top + height

    return new_boxes
