import os
from ConfigParser import ConfigParser

def config():
    cfg = ConfigParser()
    cfg_path = os.path.dirname(__file__) + '/config.ini'
    local_cfg_path = os.getcwd() + 'config.ini'
    cfg.read([cfg_path, local_cfg_path])
    return cfg
