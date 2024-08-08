import argparse

from loguru import logger

from inference.inference_service import InferenceService


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_file_path', type=str)
    parser.add_argument('--dataset_file_path', type=str)
    return parser.parse_args()
    


def main(model_file_path:str, dataset_file_path:str):
    inf_service = InferenceService(
        opt.model_file_path,
        opt.dataset_file_path
        )
    inf_service.run()
    logger.info(f"Result file path: {inf_service.result_file_path}")
    return inf_service.result_file_path


if __name__ == "__main__":
    opt = parse_opt()
    result_file_path = main(opt.model_file_path, opt.dataset_file_path)