import os
from ConfigParser import ConfigParser

def config():
    cfg = ConfigParser()
    cfg_path = os.path.dirname(__file__) + '/config.ini'
    cfg.read(cfg_path)
    return cfg
