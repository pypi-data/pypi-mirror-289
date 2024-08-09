import torch
from torch import nn
from typing import List, Tuple, Union, Optional
# from mmseg.models.backbones.swin import SwinTransformer as SwinTransformerSeg
from mmdet.models.backbones.swin import SwinTransformer
from mmdet.models.backbones.resnet import ResNet

class SplitSwinTransformer(SwinTransformer):
    '''
    Split version of the Swin Transformer backbone. 
    Can be initialized with the same parameters as the Swin Transformer backbone or using a cfg file and optional Checkpoint
    '''
    def __init__(self, **kwargs):
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)
        # super(SplitSwinTransformer, self).__init__(**kwargs)
        
    @classmethod
    def create_from_swin(cls, swin_instance):
        split_instance = cls(**swin_instance.__dict__)
        split_instance.load_state_dict(swin_instance.state_dict)
        # Return the new instance of Sub
        return split_instance
    
    @classmethod
    def create_from_instance_and_cfg(cls, swin_instance, cfg):
        split_instance = cls(**cfg.model.backbone)
        split_instance.load_state_dict(swin_instance.state_dict())
        # Return the new instance of Subclass
        return split_instance
    
    def split_forward(self,
                      x: torch.Tensor, 
                      hw_shape: Tuple = (0,0), 
                      outs: List[torch.Tensor]=[], 
                      input_layer:int = 0,
                      output_layer:Optional[int]=None) -> Union[Tuple[Tuple, List[torch.Tensor]], List[torch.Tensor]]:
        if input_layer == 0:
            x, hw_shape = self.patch_embed(x)

            if self.use_abs_pos_embed:
                x = x + self.absolute_pos_embed
            x = self.drop_after_pos(x)

        for i, stage in enumerate(self.stages):
            if i < input_layer-1:
                continue
            if i == input_layer-1:
                out = outs[-1]
                outs = outs[:-1]
                out_hw_shape = hw_shape
                if stage.downsample!=None:
                    x,hw_shape = stage.downsample(out, out_hw_shape)
                else:
                    x,hw_shape = out, out_hw_shape
            else:
                x, hw_shape, out, out_hw_shape = stage(x, hw_shape)
            # print(f'x: {x.shape}, hw_shape: {hw_shape}, out: {out.shape}, out_hw_shape: {out_hw_shape}')
            if i == output_layer:
                return out_hw_shape, outs + [out]
            if i in self.out_indices:
                norm_layer = getattr(self, f'norm{i}')
                out = norm_layer(out)
                out = out.view(-1, *out_hw_shape,
                                self.num_features[i]).permute(0, 3, 1,
                                                                2).contiguous()
                outs = outs + [out]
        return outs

class SplitResNet(ResNet):
    def __init__(self, **kwargs):
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)
    
    @classmethod
    def init_from_resnet(cls, resnet_instance):
        split_instance = cls(**resnet_instance.__dict__)
        split_instance.load_state_dict(resnet_instance.state_dict)
        # Return the new instance of Sub
        return split_instance
    
    @classmethod
    def create_from_instance_and_cfg(cls, resnet_instance, cfg):
        split_instance = cls(**cfg.model.backbone)
        split_instance.load_state_dict(resnet_instance.state_dict())
        # Return the new instance of Subclass
        return split_instance

    def split_forward(self,
                      x: torch.Tensor, 
                      outs: List[torch.Tensor]=[], 
                      input_layer:int = 0,
                      output_layer:Optional[int]=None) -> Union[Tuple[Tuple, List[torch.Tensor]], List[torch.Tensor]]:
        """Forward function."""
        if input_layer == 0:
            if self.deep_stem:
                x = self.stem(x)
            else:
                x = self.conv1(x)
                x = self.norm1(x)
                x = self.relu(x)
            x = self.maxpool(x)
        
        for i, layer_name in enumerate(self.res_layers):
            if i < input_layer - 1:
                continue
            if i == input_layer-1 and x is None:
                x = outs[-1]
                continue
            res_layer = getattr(self, layer_name)
            x = res_layer(x)
            if i == output_layer:
                return tuple(outs + [x])
            
            if i in self.out_indices:
                outs = outs + [x]
        
        return tuple(outs)

# class SplitSwinTransformerSeg(SwinTransformerSeg):
#     def __init__(self, **kwargs):
#         if 'type' in kwargs:
#             del kwargs['type']
#         super().__init__(**kwargs)

#     @classmethod
#     def create_from_swin(cls, swin_instance):
#         split_instance = cls(**swin_instance.__dict__)
#         split_instance.load_state_dict(swin_instance.state_dict)
#         # Return the new instance of Sub
#         return split_instance
    
#     @classmethod
#     def create_from_instance_and_cfg(cls, swin_instance, cfg):
#         split_instance = cls(**cfg.model.backbone)
#         split_instance.load_state_dict(swin_instance.state_dict())
#         # Return the new instance of Subclass
#         return split_instance
    
    
#     def split_forward(self, x, hw_shape=0, outs=[], input_layer=0, output_layer=None):
#         return _split_forward(self, x, hw_shape, outs, input_layer, output_layer)
