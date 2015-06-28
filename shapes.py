#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
# Modified for BSB by Asmfreak
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
import sys

from bsb_io import *
import spidev
import NokiaLCD as lcd

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

disp = lcd.display()
image, draw = lcd.image()

# Draw a white filled box to clear the image.
draw.rectangle((0,0,PCD8544.LCDWIDTH,PCD8544.LCDHEIGHT), outline=255, fill=255)

# Draw some shapes.
draw.ellipse((2,2,22,22), outline=0, fill=255)
draw.rectangle((24,2,44,22), outline=0, fill=255)
draw.polygon([(46,22), (56,2), (66,22)], outline=0, fill=255)
draw.line((68,22,81,2), fill=0)
draw.line((68,2,81,22), fill=0)

# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
#font = ImageFont.truetype(sys.argv[1], 16)

# Write some text.
#draw.text((8,20), 'Happy Birthday', font=font)

#draw.text((8,30), 'Hello World!', font=font)


# Display image.
disp.image(image)
disp.display()
def fill_vdot(disp, image, draw, v):
    for i in range(PCD8544.LCDWIDTH):
        for j in range(PCD8544.LCDHEIGHT):
            draw.line((i, j, i, j+1), fill=v)
            disp.image(image)
            disp.display()

def fill_hdot(disp, image, draw, v):
    for j in range(PCD8544.LCDHEIGHT):
        for i in range(PCD8544.LCDWIDTH):
            draw.line((i, j, i+1, j), fill=v)
            disp.image(image)
            disp.display()

def fill_vline(disp, image, draw, v):
    for i in range(PCD8544.LCDWIDTH):
        draw.line((i, 0, i, PCD8544.LCDHEIGHT), fill=v)
        disp.image(image)
        disp.display()

def fill_hline(disp, image, draw, v):
    for i in range(PCD8544.LCDHEIGHT):
        draw.line((0, i, PCD8544.LCDWIDTH, i), fill=v)
        disp.image(image)
        disp.display()

fill_hline(disp, image, draw, 0)
fill_vline(disp, image, draw, 1)
