import torch
import json
import os

from mmengine.config import Config
from mmengine.runner import Runner
from split_utils import SplitEncoderDecoder

from tqdm import tqdm

def setup_config():

    
    config_filename = "knet-s3_swin-t_upernet_8xb2-adamw-80k_ade20k-512x512.py"
    checkpoint_file = 'knet_s3_upernet_swin-t_8x2_512x512_adamw_80k_ade20k_20220303_133059-7545e1dc.pth'

    # setup the config file
    orig_config_file = os.path.join('configs', 'segmentation', 'original', config_filename)
    cfg = Config.fromfile(orig_config_file)

    config_file = os.path.join('configs', 'segmentation', config_filename)

    checkpoint_file = os.path.join('configs', 'segmentation', checkpoint_file)
    

    # set the data_root of the config file
    data_root = 'data/ade/ADEChallengeData2016'
    cfg.data_root = data_root
    cfg.test_dataloader.dataset.data_root = data_root
    cfg.train_dataloader.dataset.data_root = data_root
    cfg.val_dataloader.dataset.data_root = data_root


    train_pipeline = [{'type': 'LoadImageFromFile'},
                    {'reduce_zero_label': True, 'type': 'LoadAnnotations'},
                    {'keep_ratio': True,
                    'ratio_range': (0.5, 2.0),
                    'scale': (2048, 1024), # (2048, 512)
                    'type': 'RandomResize'},
                    {'cat_max_ratio': 0.75, 'crop_size': (512, 512), 'type': 'RandomCrop'},
                    {'prob': 0.5, 'type': 'RandomFlip'},
                    {'type': 'PhotoMetricDistortion'},
                    {'type': 'PackSegInputs'}]

    cfg.train_dataloader.dataset.pipeline = train_pipeline
    # cfg.pretrained = "https://download.openmmlab.com/mmsegmentation/v0.5/mask2former/mask2former_swin-t_8xb2-160k_ade20k-512x512/mask2former_swin-t_8xb2-160k_ade20k-512x512_20221203_234230-7d64e5dd.pth"

    cfg.dump(config_file)

    return config_file, checkpoint_file

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Run MMSEG Swin ADE20K Evaluation')
    parser.add_argument(
        '--data-root',
        type=str,
        help='data directory',
        default='data/ade/ADEChallengeData2016')
    parser.add_argument(
        '--config', 
        type=str,
        help='config file path')
    parser.add_argument(
        '--checkpoint', 
        type=str,
        help='checkpoint file path')
    parser.add_argument(
        '--device', 
        type=str,
        default='cuda',
        help='device used for inference')
    parser.add_argument(
        '--output', 
        type=str,
        help='output file path'
    )
    return parser.parse_args()


def set_data_root_in_cfg(cfg, data_root):
    cfg.data_root = data_root
    cfg.test_dataloader.dataset.data_root = data_root
    cfg.train_dataloader.dataset.data_root = data_root
    cfg.val_dataloader.dataset.data_root = data_root

def main(args):
    # config_file, checkpoint_file = setup_config()

    cfg = Config.fromfile(args.config)

    # set the data_root of the config file
    set_data_root_in_cfg(cfg, args.data_root)

    model = SplitEncoderDecoder.create_from_cfg_and_checkpoint(args.config, args.checkpoint)
    
    model = model.to(args.device)
    model.zero_grad()
    model.eval()

    dataloader = Runner.build_dataloader(cfg.val_dataloader)
    evaluator = Runner.build_evaluator(None, cfg.val_evaluator)
    setattr(evaluator,'dataset_meta', dataloader.dataset.metainfo)

    for i, data in tqdm(enumerate(dataloader), total=len(dataloader), desc="Processing images"):
        features = model.feature_frontend(data)
        result_backend_inference = model.backend_inference(features)
        evaluator.process(result_backend_inference)
        # eval_result = evaluator.offline_evaluate(result_backend_inference)
        # eval_results.append(eval_result)
        # result_backend_raw = model.backend_raw(data)

    result = evaluator.evaluate(len(dataloader))
    print(result)

    # Open a file for writing in text mode (use 'w' for writing)
    # add .json to the args.output if it does not have it
    if not args.output.endswith('.json'):
        args.output += '.json'
    result_json_filename = args.output
    # result_json_filename = f"results/result_{config_file.split('/')[-1].split('.')[0]}.json"
    with open(result_json_filename, 'w') as json_file:
        # Convert the dictionary to a JSON string with human-readable indentation
        json_string = json.dumps(result, indent=4)

        # Write the JSON string to the file
        json_file.write(json_string)

if __name__ == '__main__':
    args = parse_args()
    main(args)