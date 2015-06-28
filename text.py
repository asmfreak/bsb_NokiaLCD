#!/usr/bin/python
import NokiaLCD as ex
import sys
class text:
    def __init__(self, font = None, fsize=None):
        self.d = ex.display()
        self.img,self.drw = ex.image()
        ft = ex.font(font, fsize)
        self.drw.text((4,3),'Happy', font=ft)
        self.drw.text((8,20),'Birthday', font=ft)
        self.drw.text((30,36),'Elsa!',font=ft)

    def run(self):
        ex.render_display(self.d,self.img)

if __name__ == '__main__':
    import sys
    text(sys.argv[1], int(sys.argv[2])).run()
