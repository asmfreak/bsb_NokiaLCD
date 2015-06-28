# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
# Modified: Paul Pletenev
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import time

from bsb_io import *
import spidev
import PCD8544
from config import config

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def init():
    import init_spi

def display():
    init()
    cfg = config()
    DC = cfg.getint("screen", "DC")
    RST = cfg.getint("screen", "RST")
    SPI_DEVICE = cfg.getint("screen", "device")
    SPI_PORT = cfg.getint("screen", "port")
    disp = PCD8544.PCD8544(DC, RST, SPI_PORT, SPI_DEVICE)
    # Initialize library.
    disp.begin(contrast=60)
    # Clear display.
    disp.clear()
    disp.display()
    return disp

def image():
    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new('1', (PCD8544.LCDWIDTH, PCD8544.LCDHEIGHT))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a white filled box to clear the image.
    draw.rectangle((0,0,PCD8544.LCDWIDTH,PCD8544.LCDHEIGHT), outline=255, fill=255)
    return image, draw

def font(name, size):
    return ImageFont.truetype(name, size)


def render_display(disp, image):
    disp.image(image)
    disp.display()
