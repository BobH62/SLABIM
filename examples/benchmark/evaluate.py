from registration.eval import RegEval
from pose_tracking.eval import TrackEval
from semantic_mapping.eval import SemanticEval
from time import perf_counter
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, default='registration')
    parser.add_argument('--config', type=str, default='./config/5F/5f_region_01.yaml')
    args = parser.parse_args()

    if args.mode == "registration":
        reg_eval = RegEval(args.config)
        reg_eval.evaluate()
        reg_eval.print_result()
    elif args.mode == 'pose_tracking':
        pass
    elif args.mode == 'semantic_mapping':
        pass