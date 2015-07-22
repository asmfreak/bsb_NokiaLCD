import os
from ConfigParser import ConfigParser


def config():
    cfg = ConfigParser()
    cfg_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    local_cfg_path = os.path.join(os.getcwd(), 'config.ini')
    cfg.readfp(open(cfg_path))
    files = cfg.read([local_cfg_path])
    print "Additional config loaded from {}".format(files)
    return cfg
