# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
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

import math
import time

from bsb_io import *
import spidev
import NokiaLCD as lcd

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


disp = lcd.display()

image, draw = lcd.image()

# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('fonts/Mario-Kart-DS.ttf', 16)


# Define text and get total width.
text = 'NOKIA 5110: NOT JUST FOR SNAKE ANYMORE. THIS IS AN OLD SCHOOL DEMO SCROLLER!! GREETZ TO: LADYADA & THE ADAFRUIT CREW, TRIXTER, FUTURE CREW, AND FARBRAUSCH'
maxwidth, height = draw.textsize(text, font=font)

# Set starting position.
startpos = 83
pos = startpos

# Animate text moving in sine wave.
print 'Press Ctrl-C to quit.'
ts = time.time()
nf = 0
try:
    while True:
        # Clear image buffer.
        draw.rectangle((0,0,83,47), outline=255, fill=255)
        # Enumerate characters and draw them offset vertically based on a sine wave.
        x = pos
        for i, c in enumerate(text):
            # Stop drawing if off the right side of screen.
            if x > 83:
                break
            # Calculate width but skip drawing if off the left side of screen.
            if x < -10:
                width, height = draw.textsize(c, font=font)
                x += width
                continue
            # Calculate offset from sine wave.
            y = (24-8)+math.floor(10.0*math.sin(x/83.0*2.0*math.pi))
            # Draw text.
            draw.text((x, y), c, font=font, fill=0)
            # Increment x position based on chacacter width.
            width, height = draw.textsize(c, font=font)
            x += width
        # Draw the image buffer.
        disp.image(image)
        disp.display()
        nf += 1
        # Move position for next frame.
        pos -= 2
        # Start over if text has scrolled completely off left side of screen.
        if pos < -maxwidth:
            pos = startpos
        # Pause briefly before drawing next frame.
        time.sleep(0.1)
finally:
    dt = time.time() - ts
    print("Ran for " + str(dt) + "seconds. Drew " + str(nf) + "frames. FPS " + str(nf / dt))
