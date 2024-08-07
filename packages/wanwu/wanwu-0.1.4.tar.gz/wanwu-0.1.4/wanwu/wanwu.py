
import argparse
from wanwu.core.enums import Backends
from wanwu.det.det import Det
from alfred.utils.log import logger
import os
from wanwu.core.cellar import model_urls
from wanwu.core.modelloader import ModelLoader, TaskType
from .version import __version__


def arg_parse():
    """
    parse arguments
    :return:
    """
    parser = argparse.ArgumentParser(prog="wanwu")
    parser.add_argument(
        "--version", "-v", action="store_true", help="show version info."
    )

    main_sub_parser = parser.add_subparsers(dest="subparser_name")

    # =============== totrt part ================
    trt_parser = main_sub_parser.add_parser(
        "totrt", help="Convert model to trt with standared tasks."
    )
    trt_parser.add_argument("--model", "-m", help="onnx model path")
    trt_parser.add_argument(
        "--data_type", "-d", type=int, default=32, help="32, 16, 8 presents fp32, fp16, int8"
    )
    trt_parser.add_argument(
        "--batch_size", "-b", type=int, default=1, help="Batch size of the model."
    )
    trt_parser.add_argument(
        "--score_thr", "-s", type=float, default=0.2, help="score threshold of detection model, only work on det model."
    )
    trt_parser.add_argument(
        "--nms_thr", "-n", type=float, default=0.6, help="nms threshold of detection model, only work on det model."
    )
    trt_parser.add_argument(
        "--input_width", type=int, default=640, help="onnx model input width (for dynamic width onnx model)."
    )
    trt_parser.add_argument(
        "--input_height", type=int, default=512, help="onnx model input height (for dynamic height onnx model)."
    )
    trt_parser.add_argument("--min_shapes", nargs='+',
                            help="min_shapes of opt_params")
    trt_parser.add_argument("--opt_shapes", nargs='+',
                            help="opt_shapes of opt_params")
    trt_parser.add_argument("--max_shapes", nargs='+',
                            help="max_shapes of opt_params")
    trt_parser.add_argument(
        "--task", "-t", default='det', help="task name: det | kps | cls | seg"
    )
    trt_parser.add_argument(
        "--nms_plugin", default='efficient_nms', help="batched_nms | efficient_nms"
    )

    # # =============== check part ================
    # check_parser = main_sub_parser.add_parser(
    #     "ls", help="Check your onnx model is valid or not."
    # )
    # check_parser.add_argument("--model", "-m", help="onnx model path")
    # check_parser.add_argument("--print", action="store_true")
    return parser.parse_args()


class WanwuCli(object):
    def __init__(self):
        args = arg_parse()
        if args.version:
            print(__version__)
        else:
            if args.subparser_name == None:
                print("should provide at least one sub command, -h for detail.")
                exit(-1)
            self.model_path = args.model
            if args.model != None and os.path.exists(args.model):
                if args.subparser_name == "totrt":
                    self.totrt(self.model_path, args)
                elif args.subparser_name == "ls":
                    self.ls()

            else:
                print(
                    "{} does not exist or you should provide model path like `wanwu totrt -m model.onnx`.".format(
                        args.model
                    )
                )

    def ls(self):
        print('supported models" \n')
        print(model_urls)

    def search(self):
        pass

    def check(self, p):
        pass

    def totrt(self, onnx_f, args):
        bs = args.batch_size
        score_thr = args.score_thr
        nms_thr = args.nms_thr
        nms_plugin = args.nms_plugin
        t = args.task
        w = args.input_width
        h = args.input_height
        res = ModelLoader(onnx_f, backend=Backends.GPU_TENSORRT, task_type=TaskType.from_str(t),
                          batch_size=bs, score_thr=score_thr, input_height=h, input_width=w,
                          nms_thr=nms_thr, nms_plugin_name=nms_plugin)
        print('done. a new model should be generated into: {}'.format(res.onnx_f))


def main():
    WanwuCli()


if __name__ == "__main__":
    main()
