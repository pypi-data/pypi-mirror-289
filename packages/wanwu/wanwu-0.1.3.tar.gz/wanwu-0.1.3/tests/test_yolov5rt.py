from yolort.runtime.yolo_graphsurgeon import YOLOGraphSurgeon
import sys

checkpoint_path = sys.argv[1]

yolo_gs = YOLOGraphSurgeon(
    checkpoint_path,
    version="r6.0",
    enable_dynamic=False,
)

yolo_gs.register_nms()

# Export the ONNX model
yolo_gs.save('weights/a.onnx')