import vrplib
from pathlib import Path
from typing import List
import numpy as np
from siaf.utils.common import load_config

def test_read_data():
    cfg_path=Path(__file__).parent.parent/'configs/app.yaml'
    app_cfg=load_config(cfg_path)
    
    assert app_cfg.NUM_ITRATION>1000 and app_cfg['NUM_REPEAT']>1
