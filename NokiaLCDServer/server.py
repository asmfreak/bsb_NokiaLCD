import os
import json
import web
from StringIO import StringIO
import PIL
import PIL.PpmImagePlugin

import NokiaLCD as LCD
from config import config

urls = (
    '/', 'Index',
    '/size', 'Size',
    '/buffer', 'Buffer'
)

app = web.application(urls, locals())


class Index:
    def GET(self):
        return "This is a screen server"


class Size:
    def GET(self):
        return json.dumps(web.size)


class Buffer:
    def POST(self):
        data = unicode(web.data(), 'utf-8').split("\n")
        LCD.clear_image(web.draw)
        for n, line in enumerate(data):
            web.draw.text((0, n*web.font_size[1]), line, font=web.font)
        LCD.render_display(web.disp, web.img)


web.disp = LCD.display()
web.img, web.draw = LCD.image()
cfg = config()
fname = cfg.get("server", "font")
fsize = cfg.getint("server", "size")
print "Got font {} size {}".format(fname, fsize)
try:
    web.font = LCD.font(fname, fsize)
except IOError:
    fname = os.path.join(os.path.dirname(__file__), fname)
    web.font = LCD.font(fname, fsize)
sizes = web.font_size = web.font.getsize(u"\u2592")
web.size = int(LCD.width / sizes[0]), int(LCD.height / sizes[1])

if __name__ == "__main__":
    app.run()
