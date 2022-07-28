from os.path import join
from easydict import EasyDict as edict
from AlphaPose.detector import ALPHAPOSE_ROOT


cfg = edict()
cfg.CONFIG = join(ALPHAPOSE_ROOT, 'detector/yolo/cfg/yolov3-spp.cfg')
cfg.WEIGHTS = join(ALPHAPOSE_ROOT, 'detector/yolo/data/yolov3-spp.weights')
cfg.INP_DIM =  608
cfg.NMS_THRES =  0.6
cfg.CONFIDENCE = 0.1
cfg.NUM_CLASSES = 80
