from time import sleep
from turtle import *
from threading import *

from cat_class import Cat
from mouse_class import Mouse

class TomasbiyAndJerrybek():
    def __init__(self) -> None:
        setup(500, 500)
        Screen()
        screen=Screen()
        title("Tomasbiy and Jerrybek")
        screen.addshape("assets/cat_left.gif")
        screen.addshape("assets/cat_right.gif")    
        screen.addshape("assets/cat_top.gif")
        screen.addshape("assets/cat_down.gif")
        screen.addshape("assets/mouse_left.gif")
        screen.addshape("assets/mouse_right.gif")
        screen.addshape("assets/mouse_down.gif")
        screen.addshape("assets/mouse_top.gif")
        self.cat = Cat()
        self.mouse = Mouse()
        self.start()

    def isCollision(self):
        while(True):
            cxcor = self.cat.xcor()
            cycor = self.cat.ycor()
            mxcor = self.mouse.xcor()
            mycor = self.mouse.ycor()
            print("cat(%i,%i) mouse(%i,%i)" % (cxcor, cycor, mxcor, mycor))
            if ((cxcor >= mxcor-20) and (cxcor <= mxcor+20) and (cycor >= mycor-20) and (cycor <= mycor+20)):
                print("словил")
            else:
                pass

    def start(self):
        self.cat.cat_move()
        thread_mouse = Thread(target = self.mouse.move_mouse(self.mouse))
        thread_mouse.start()
        thread_collision = Thread(target=self.isCollision)
        thread_collision.start()
        mainloop()
        thread_mouse.join()
        thread_collision.join()

    