import os

model_urls_root_r01 = (
    "https://github.com/jinfagang/wanwu_release/releases/download/v0.1"
)

LOCAL_CACHE_FOLDER = os.path.expanduser("~/wanwu_models")

"""
Following todo:

- SCRFD gpu model, fix efficientNMS issue;
- YOLOX CPU and GPU version model;

"""

model_urls = {
    # r10 version: init workable version with models
    "yolov5s_coco_trt": f"{model_urls_root_r01}/yolov5s_gpu.onnx",
    "yolov5s_coco_cpu": f"{model_urls_root_r01}/yolov5s_cpu.onnx",
    # "yolov5_s6_coco": f"{model_urls_root_r40}/yolov5_darknet_pan_s_r31_coco-eb728698.pt",
    "scrfd_500m_cpu": f"{model_urls_root_r01}/scrfd_500m_cpunms.onnx",
    "scrfd_500m_trt": f"{model_urls_root_r01}/scrfd_500m_gpu.onnx",
    "yolox_s_coco_trt": f"{model_urls_root_r01}/yolox_s_gpu.onnx",
    "yolox_tiny_coco_cpu": f"{model_urls_root_r01}/yolox_tiny_cpunms.onnx",
    "reid_osnet_x0_25_cpu": f"{model_urls_root_r01}/reid_osnet_x0_25_256x128.onnx",
    "reid_osnet_x0_25_trt": f"{model_urls_root_r01}/reid_osnet_x0_25_256x128.onnx",
    "alp_halpe26_res50_cpu": f"{model_urls_root_r01}/alp_halpe26_res50.onnx",
    "alp_halpe26_res50_trt": f"{model_urls_root_r01}/alp_halpe26_res50.onnx",
    "alp_halpe26_res18_cpu": f"{model_urls_root_r01}/alp_halpe26_r18.onnx",
    "alp_halpe26_res18_trt": f"{model_urls_root_r01}/alp_halpe26_r18.onnx",
    "yolov7_cpu": f"{model_urls_root_r01}/yolov7_cpu.onnx",
    "yolov7_trt": f"{model_urls_root_r01}/yolov7_gpu.onnx",
    "yolov7-tiny_cpu": f"{model_urls_root_r01}/yolov7-tiny_cpu.onnx",
    "yolov7-tiny_trt": f"{model_urls_root_r01}/yolov7-tiny_gpu.onnx",
    "yolov5n-0.5_cpu": f"{model_urls_root_r01}/yolov5n-0.5.onnx",
}
