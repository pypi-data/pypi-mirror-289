from typing import List, Tuple, Union, Optional

from mmdet.models.detectors.two_stage import TwoStageDetector
from mmdet.models.detectors import GroundingDINO, GLIP, Mask2Former, RetinaNet, CascadeRCNN
from mmdet.structures import DetDataSample
from mmengine.config import Config
from mmseg.models.segmentors import EncoderDecoder
from mmdet.apis import init_detector

from .split_utils import NetworkSplitter
from .legacy import RepPointsV2MaskDetector, convert_swin_checkpoint_file

@NetworkSplitter()
class SplitTwoStageDetector(TwoStageDetector):
    '''
    SplitTwoStageDetector is a class that allows spliting any TwoStageDetector basde model at the input cut_point of the backbone
    Created using the NetworkSplitter automatic network splitter
    '''
    def __init__(self, cut_point=0, **kwargs):
        pass

@NetworkSplitter()
class SplitRepPointsV2MaskDetector(RepPointsV2MaskDetector):
    '''
    SplitRepPointsV2MaskDetector is a class that allows spliting a RepPointsV2MaskDetector model at the input cut_point of the backbone
    Requires special modifications due to RepPointsV2MaskDetector utilizng older version of mmdet and lack of backward compatibility see legacy folder for more details
    Created using the NetworkSplitter automatic network splitter
    '''
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def create_from_cfg_and_checkpoint(cls, cfg_path, checkpoint_path, device = 'cpu', cut_point=1):
        cfg = Config.fromfile(cfg_path)
        # print(cfg.model)
        if not 'converted' in checkpoint_path:
            dst = checkpoint_path.replace('.pth', '_converted.pth')
            checkpoint_path = convert_swin_checkpoint_file(checkpoint_path, dst)
        
        model_init = init_detector(cfg_path, checkpoint_path, device=device)
        model = cls.create_from_instance_and_cfg(model_init, cfg, cut_point = cut_point)
        # model.prepare_preprocessing()
        return model
  
    def backend_inference(self, data):
        result = self.val_step(data)
        return result 
    
    def backend_loss(self, data):
        if isinstance(data['data_samples'][0], DetDataSample):
            img_metas = []
            gt_bboxes = []
            gt_labels = []
            gt_bboxes_ignore = []
            gt_sem_map= []
            gt_sem_weights = []
            gt_masks = []
            for ds in data['data_samples']:
                img_metas.append(ds.metainfo)
                gt_bboxes.append(ds.gt_instances.bboxes)
                gt_labels.append(ds.gt_instances.labels)
                gt_bboxes_ignore.append(ds.ignored_instances.bboxes)
                gt_masks.append(ds.gt_instances.masks)
                gt_sem_map.append(ds.gt_sem.sem_map)
                gt_sem_weights.append(ds.gt_sem.sem_weights)
        return self.parse_losses(self.loss(data['inputs'], img_metas, gt_bboxes, gt_labels, 
                                           gt_bboxes_ignore = gt_bboxes_ignore, 
                                           gt_masks = gt_masks, 
                                           gt_sem_map = gt_sem_map,
                                           gt_sem_weights = gt_sem_weights))

@NetworkSplitter()
class SplitGDINO(GroundingDINO):
    ''''
    SplitGDINO is a class that allows spliting a grounding dino model at the input cut_point of the backbone
    Note that currently, there is no support for splitting the text processing and as such this only works for fixed languange inputs
    Alternitvely, languange inputs may be encoded separately and added to the bitstream to support the current implementation

    '''
    def __init__(self, *args, **kwargs):
        pass

@NetworkSplitter()
class SplitGLIP(GLIP):

    ''''
    SplitGLIP is a class that allows spliting a GLIP model at the input cut_point of the backbone
    Note that currently, there is no support for splitting the text processing and as such this only works for fixed languange inputs
    Alternitvely, languange inputs may be encoded separately and added to the bitstream to support the current implementation
    created using the NetworkSplitter automatic network splitter
    '''
    def __init__(self, *args, **kwargs):
        pass

@NetworkSplitter()
class SplitMask2Former(Mask2Former):

    ''''
    SplitMask2Former is a class that allows spliting a Mask2former model at the input cut_point of the backbone
    Udated vestion supports either Swin Transformer or ResNet backbones
    created using the NetworkSplitter automatic network splitter
    '''
    def __init__(self, *args, **kwargs):
        pass

@NetworkSplitter()
class SplitEncoderDecoder(EncoderDecoder):
    '''
    SplitEncoderDecoder is a class that allows spliting an EncoderDecoder model at the input cut_point of the backbone
    Created using the NetworkSplitter automatic network splitter
    '''
    def __init__(self, cut_point=0, **kwargs):
        pass
    
    def swap_preprocessor(self):
        temp = self.data_preprocessor
        self.data_preprocessor = self.frontend_preprocessor
        self.frontend_preprocessor = temp

    def set_cut_point(self, cut_point):
        self.cut_point = cut_point

@NetworkSplitter()
class SplitRetinaNet(RetinaNet):
    '''
     SplitRetinaNet is a class that allows spliting a RetinaNet model at the input cut_point of the backbone
     Created using the NetworkSplitter automatic network splitter
    '''
    def __init__(self, *args, **kwargs):
        pass
@NetworkSplitter()
class SplitCascadeRCNN(CascadeRCNN):
        
        ''''
        SplitCascadeRCNN is a class that allows spliting a CascadeRCNN model at the input cut_point of the backbone
        Created using the NetworkSplitter automatic network splitter
        '''
        def __init__(self, *args , **kwargs):
            pass