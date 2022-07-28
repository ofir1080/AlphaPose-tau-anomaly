from os.path import join
from easydict import EasyDict as edict

from AlphaPose.detector import ALPHAPOSE_ROOT

cfg = edict()
cfg.CONFIG = join(ALPHAPOSE_ROOT, 'detector/tracker/cfg/yolov3.cfg')
cfg.WEIGHTS = join(ALPHAPOSE_ROOT, 'detector/tracker/data/jde.1088x608.uncertainty.pt')
cfg.IMG_SIZE =  (1088, 608)
cfg.NMS_THRES =  0.6
cfg.CONFIDENCE = 0.4
cfg.BUFFER_SIZE = 30 # frame buffer
