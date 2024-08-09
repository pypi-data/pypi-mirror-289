import torch
import types
from copy import deepcopy

from torch import nn
from pathlib import Path
from collections import OrderedDict
from typing import Union, List, Optional, Type, Tuple
from dataclasses import dataclass

from mmdet.models.backbones import SwinTransformer, ResNet

from mmdet.structures.mask import encode_mask_results
from mmengine.config import Config, ConfigDict
from mmdet.apis import init_detector
from .split_backbones import SplitSwinTransformer, SplitResNet
# from mmengine.runner import load_checkpoint

    
@dataclass
class SplitSwinFeatures:
    outs: List[torch.Tensor]
    hw_shape: torch.Tensor
    device: torch.device
    x: Optional[torch.tensor] = None
    
    def __len__(self):
        return self.outs[0].shape[0] if self.outs else 0

@dataclass
class SplitResNetFeatures:
    outs: List[torch.Tensor]
    device: torch.device
    x: Optional[torch.tensor] = None
    
    def __len__(self):
        return self.outs[0].shape[0] if self.outs else 0
    
def _feature_frontend(model: nn.Module, data : Union[torch.Tensor, dict]) -> Union[torch.Tensor, dict]:
    '''
    Return the split features extracted by the frontend of the split model
    if input 'data' is a dictionary, assume preprocessing has not been performed and preprocess it ourselves
    Otherwise assume that 'data' is the tensor part of the preprocessed input
    currently only works with swintransformer backbone 
    '''
    # print(model)
    if isinstance(data, dict):
        data = model.frontend_preprocessor(data, model.training)
        x = data['inputs']
    else:
        x = data

    if model.cut_point>0:
        out =  model.backbone.split_forward(x, output_layer = model.cut_point-1)
        # data['inputs'] = {"hw_shape": out[0],
        #                   "outs": out[1]}
        if isinstance(model.backbone, SplitSwinTransformer):
            data['inputs'] = SplitSwinFeatures(outs=out[1], hw_shape=out[0], device=x.device)
        elif isinstance(model.backbone, SplitResNet):
            data['inputs'] = SplitResNetFeatures(outs=list(out), device=x.device)

    return data       

def _extract_feat_from_split(model: nn.Module, batch_inputs: Union[torch.Tensor, SplitSwinFeatures, SplitResNetFeatures]) -> Tuple[torch.Tensor]:
    """Extract full features from frontend split features (from swintransformer based models only)
    for backwards compatability - allow use of dictionary alongside SplitSwinFeatures


    Args:
        model (nn.Module): The model with a backbone from which to extract features
        batch_inputs (Tensor): Image tensor with shape (N, C, H ,W).

    Returns:
        tuple[Tensor]: Multi-level features that may have
        different resolutions.
    """
    # x, hw_shape, outputs = self.backbone.split_forward(batch_inputs, outs=[], output_layer=1)
    # print("splitting at layer 1")
    # print(batch_inputs)
    if isinstance(batch_inputs, SplitSwinFeatures):
        hw_shape = batch_inputs.hw_shape
        outs = batch_inputs.outs
        x = batch_inputs.x
    elif isinstance(batch_inputs, SplitResNetFeatures):
        outs = batch_inputs.outs
        x = batch_inputs.x
    # elif isinstance(batch_inputs, dict):
    #     x = batch_inputs["x"] if "x" in batch_inputs else None
    #     hw_shape = batch_inputs["hw_shape"]
    #     outs = batch_inputs["outs"]
    else:
        x = batch_inputs
        hw_shape = 0
        outs = []
    if isinstance(model.backbone, SplitSwinTransformer):
        x = model.backbone.split_forward(x, hw_shape, outs=outs, input_layer=model.cut_point)
    elif isinstance(model.backbone, SplitResNet):
        x = model.backbone.split_forward(x, outs=outs, input_layer=model.cut_point)
    else:
        raise TypeError("Only SwinTransformer and ResNet backbones are supported at the moment")
    
    if model.with_neck:
        x = model.neck(x)
    return x

def _create_from_cfg_and_checkpoint(cls: Type, cfg: Union[str, Path, Config], checkpoint_path: str, device: Union[torch.device, str] = 'cpu', cut_point: int=1) -> nn.Module:
    model_init = init_detector(cfg, checkpoint_path, device=device)
    if isinstance(cfg, (str, Path)):
        config = Config.fromfile(cfg)
    elif not isinstance(cfg, Config):
        raise TypeError('config must be a filename or Config object, '
                    f'but got {type(cfg)}')
    model = cls.create_from_instance_and_cfg(model_init, config, cut_point = cut_point )
    # model.prepare_preprocessing()
    return model


def _create_from_instance_and_cfg(cls: Type, model_instance: nn.Module, cfg: Config , cut_point:int = 0, device: Union[torch.device, str] = 'cpu')-> nn.Module:
    split_instance = cls(cut_point = cut_point, **cfg.model)
    split_instance.load_state_dict(model_instance.state_dict())
    # Return the new instance of Subclass
    split_instance.cfg = model_instance.cfg
    if isinstance(split_instance.backbone, SwinTransformer):
        split_instance.backbone = SplitSwinTransformer.create_from_instance_and_cfg(split_instance.backbone, cfg)
    elif isinstance(split_instance.backbone, ResNet):
        split_instance.backbone = SplitResNet.create_from_instance_and_cfg(split_instance.backbone, cfg)
    else:
        raise ValueError("Only SwinTransformer or ResNet backbones are supported at the moment")
    split_instance.prepare_preprocessing()
    return split_instance.to(device)

    
class TwoInputIdentity(nn.Module):
    def __init__(self):
        super().__init__()
    def forward(self, x, bol):
        return x


# TODO: this get_mean_metrics function does not seem to be correct
# def get_mean_metrics(metrics_list):
#     # Initialize sums for each metric
#     sum_aAcc = 0
#     sum_mIoU = 0
#     sum_mAcc = 0

#     # Iterate through the list of dictionaries
#     for item in metrics_list:
#         sum_aAcc += item['aAcc']
#         sum_mIoU += item['mIoU']
#         sum_mAcc += item['mAcc']

#     # Calculate the mean for each metric
#     mean_aAcc = sum_aAcc / len(metrics_list)
#     mean_mIoU = sum_mIoU / len(metrics_list)
#     mean_mAcc = sum_mAcc / len(metrics_list)

#     # Create a dictionary to store the means
#     mean_metrics = {
#         'mean_aAcc': mean_aAcc,
#         'mean_mIoU': mean_mIoU,
#         'mean_mAcc': mean_mAcc
#     }

#     return mean_metrics


def swin_converter_inverse(ckpt):

    new_ckpt = OrderedDict()

    def correct_unfold_reduction_order(x):
        out_channel, in_channel = x.shape
        x = x.reshape(out_channel, 4, in_channel // 4)
        x = x[:, [0, 2, 1, 3], :].transpose(1,
                                            2).reshape(out_channel, in_channel)
        return x
    
    def correct_reverse_unfold_reduction_order(x):
        out_channel, in_channel = x.shape
        x = x.reshape(out_channel, in_channel // 4, 4)
        x = x[:, :, [0, 2, 1, 3]].transpose(1,
                                            2).reshape(out_channel, in_channel)
        return x

    def correct_unfold_norm_order(x):
        in_channel = x.shape[0]
        x = x.reshape(4, in_channel // 4)
        x = x[[0, 2, 1, 3], :].transpose(0, 1).reshape(in_channel)
        return x
    
    def correct_reverse_unfold_norm_order(x):
        in_channel = x.shape[0]
        x = x.reshape(in_channel // 4, 4)
        x = x[:, [0, 2, 1, 3]].transpose(0, 1).reshape(in_channel)
        return x

    for k, v in ckpt.items():
        if k.startswith('head'):
            continue
        elif k.startswith('backbone.stages'):
            new_v = v
            if 'attn.' in k:
                # new_k = k.replace('attn.', 'attn.w_msa.')
                new_k = k.replace('attn.w_msa.', 'attn.')
            elif 'ffn.layers' in k:
                if 'ffn.layers.0.0.' in k:
                    # new_k = k.replace('mlp.fc1.', 'ffn.layers.0.0.')
                    new_k = k.replace('ffn.layers.0.0.', 'mlp.fc1.' )
                elif 'ffn.layers.1.' in k:
                    # new_k = k.replace('mlp.fc2.', 'ffn.layers.1.')
                    new_k = k.replace('ffn.layers.1.', 'mlp.fc2.')
                else:
                    new_k = k.replace('ffn.', 'mlp.')
            elif 'downsample' in k:
                new_k = k
                if 'reduction.' in k:
                    new_v = correct_reverse_unfold_reduction_order(v)
                elif 'norm.' in k:
                    new_v = correct_reverse_unfold_norm_order(v)
            else:
                new_k = k
            # new_k = new_k.replace('layers', 'stages', 1)
            new_k = new_k.replace('stages', 'layers', 1)
        elif k.startswith('backbone.patch_embed'):
            new_v = v
            if 'proj' in k:
                # new_k = k.replace('proj', 'projection')
                new_k = k.replace('projection', 'proj')
            else:
                new_k = k
        else:
            new_v = v
            new_k = k

        new_k = new_k.replace('backbone.', '')
        # new_k = new_k.replace('stages.', '')
        new_ckpt[new_k] = new_v
        

    return new_ckpt


def correct_unfold_reduction_order(x):
        out_channel, in_channel = x.shape
        x = x.reshape(out_channel, 4, in_channel // 4)
        x = x[:, [0, 2, 1, 3], :].transpose(1,
                                            2).reshape(out_channel, in_channel)
        return x
    
def correct_reverse_unfold_reduction_order(x):
    out_channel, in_channel = x.shape
    x = x.reshape(out_channel, in_channel // 4, 4)
    x = x[:, :, [0, 2, 1, 3]].transpose(1,
                                        2).reshape(out_channel, in_channel)
    return x

def correct_unfold_norm_order(x):
        in_channel = x.shape[0]
        x = x.reshape(4, in_channel // 4)
        x = x[[0, 2, 1, 3], :].transpose(0, 1).reshape(in_channel)
        return x
    
def correct_reverse_unfold_norm_order(x):
    in_channel = x.shape[0]
    x = x.reshape(in_channel // 4, 4)
    x = x[:, [0, 2, 1, 3]].transpose(0, 1).reshape(in_channel)
    return x


def get_train_pipeline_cfg(cfg: Union[str, ConfigDict]) -> ConfigDict:
    """Get the test dataset pipeline from entire config.

    Args:
        cfg (str or :obj:`ConfigDict`): the entire config. Can be a config
            file or a ``ConfigDict``.

    Returns:
        :obj:`ConfigDict`: the config of test dataset.
    """
    if isinstance(cfg, str):
        cfg = Config.fromfile(cfg)

    def _get_train_pipeline_cfg(dataset_cfg):
        if 'pipeline' in dataset_cfg:
            return dataset_cfg.pipeline
        # handle dataset wrapper
        elif 'dataset' in dataset_cfg:
            return _get_train_pipeline_cfg(dataset_cfg.dataset)
        # handle dataset wrappers like ConcatDataset
        elif 'datasets' in dataset_cfg:
            return _get_train_pipeline_cfg(dataset_cfg.datasets[0])

        raise RuntimeError('Cannot find `pipeline` in `train_dataloader`')

    return _get_train_pipeline_cfg(cfg.train_dataloader.dataset)

def set_data_root_in_cfg(cfg, data_root):
    cfg.data_root = data_root
    cfg.test_dataloader.dataset.data_root = data_root
    cfg.train_dataloader.dataset.data_root = data_root
    cfg.val_dataloader.dataset.data_root = data_root


def NetworkSplitter():
    def decorator(cls):
        new_cls = type(f'Split{cls.__name__}', (cls,), {})

        def __init__(self, cut_point:int = 0, **kwargs):
            if 'type' in kwargs:
                del kwargs['type']
            super(cls,self).__init__(**kwargs)
            cls.__init__(self, **kwargs)  # Call the original __init__ method
            self.cut_point = cut_point
        
        

        @classmethod
        def create_from_cfg_and_checkpoint(cls, cfg_path: str, checkpoint_path: str, device: Union[torch.device, str] = 'cpu', cut_point: int = 1):
            return _create_from_cfg_and_checkpoint(cls, cfg_path, checkpoint_path, device=device, cut_point=cut_point)
        
        @classmethod
        def create_from_instance_and_cfg(cls, model_instance, cfg, cut_point=0):
            return _create_from_instance_and_cfg(cls, model_instance, cfg, cut_point=cut_point)
        
        def prepare_preprocessing(self):
            self.frontend_preprocessor = deepcopy(self.data_preprocessor)
            self.data_preprocessor = TwoInputIdentity()
        
        def set_cfg(self, model_instance):
            self.cfg = model_instance.cfg
        
        def extract_feat(self, batch_inputs):
            """Extract features.
        
            Args:
                batch_inputs (Tensor): Image tensor with shape (N, C, H ,W).
        
            Returns:
                tuple[Tensor]: Multi-level features that may have
                different resolutions.
            """
            return _extract_feat_from_split(self, batch_inputs) 
        
        def feature_frontend(self, data):
            return _feature_frontend(self, data)
        
        def backend_inference(self, data):
            return self.test_step(data)
        
        def backend_raw(self, data):
            return self(data['inputs'], data['data_samples'])
        
        def backend_loss(self, data):
            return self.parse_losses(self.loss(data['inputs'], data['data_samples']))

        new_cls.__init__ = __init__
        new_cls.create_from_cfg_and_checkpoint = create_from_cfg_and_checkpoint if not 'create_from_cfg_and_checkpoint' in dir(new_cls) else new_cls.create_from_cfg_and_checkpoint
        new_cls.create_from_instance_and_cfg = create_from_instance_and_cfg if not 'create_from_instance_and_cfg' in dir(new_cls) else new_cls.create_from_instance_and_cfg
        new_cls.prepare_preprocessing = prepare_preprocessing if not 'prepare_preprocessing' in dir(new_cls) else new_cls.prepare_preprocessing
        new_cls.set_cfg = set_cfg if not 'set_cfg' in dir(new_cls) else new_cls.set_cfg
        new_cls.extract_feat = extract_feat
        new_cls.feature_frontend = feature_frontend if not 'feature_frontend' in dir(new_cls) else new_cls.feature_frontend
        new_cls.backend_inference = backend_inference if not 'backend_inference' in dir(new_cls) else new_cls.backend_inference
        new_cls.backend_raw = backend_raw if not 'backend_raw' in dir(new_cls) else new_cls.backend_raw
        new_cls.backend_loss = backend_loss if not 'backend_loss' in dir(new_cls) else new_cls.backend_loss

        return new_cls

    return decorator

# if __name__ == '__main__':
#     main()