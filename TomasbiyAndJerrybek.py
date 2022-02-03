import imp
from turtle import *


class TomasbiyAndJerrybek(Turtle):
    def __init__(self, Cat, Jerry, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__(shape=shape, undobuffersize=undobuffersize, visible=visible)
        self.cat = Cat
        self.mouse = Jerry
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

    def isCollision(self):
        cxcor = self.cat.xcor()
        cycor = self.cat.ycor()
        mxcor = self.mouse.xcor()
        mycor = self.mouse.ycor()
        print("cat(%i,%i) mouse(%i,%i)" % (cxcor, cycor, mxcor, mycor))
        if ((cxcor >= mxcor-20) and (cxcor <= mxcor+20) and (cycor >= mycor-20) and (cycor <= mycor+20)):
            print("словил")
        else:
            return 0 