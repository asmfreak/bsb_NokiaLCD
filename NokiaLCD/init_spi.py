#!/usr/bin/python
from subprocess import call
from config import config


def init_spi():
    cfg = config()

    hard = "screen"
    vars = {}
    vars["mosi"] = cfg.getint(hard, 'MOSI')
    vars["miso"] = cfg.getint(hard, 'MISO')
    vars["clk"] = cfg.getint(hard, 'CLK')
    vars["cs"] = cfg.getint(hard, 'CS')
    vars["mode"] = cfg.getint(hard, 'mode')
    vars["max_speed"] = cfg.getint(hard, 'max_speed')
    vars["device"] = cfg.getint(hard, 'device')
    vars["port"] = cfg.getint(hard,'port')

    args = "bus{device}={port},{clk},{mosi},{miso},{mode},{max_speed},{cs}".format(**vars)

    call(["rmmod", "spi-gpio-custom"])
    call(["insmod","spi-gpio-custom", args])

if __name__ == "__main__":
    init_spi()
