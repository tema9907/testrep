import random
import time
from turtle import Turtle



class Mouse(Turtle):

    def __init__(self, shape: str = "assets/mouse_top.gif", visible: bool = True) -> None:
        super().__init__(shape, visible)
        self.showturtle()
        self.penup()
        self.setx(100)
        self.sety(100)

    def move_mouse(self, mouse):
        for i in range(10000):
            time.sleep(0.5)
            self.randmov(mouse)


    def randmov(self, mouse):
        r=random.randint(1, 4) 
        if r==1:
            return(mouse.forward(45))
        if r==2:
            if int(mouse.heading())== 90:
                self.shape("assets/mouse_top.gif")
            if int(mouse.heading())== 180:
                self.shape("assets/mouse_left.gif")
            if int(mouse.heading())== 270:
                self.shape("assets/mouse_down.gif")
            if int(mouse.heading())== 0:
                self.shape("assets/mouse_right.gif")
            return(mouse.left(90))
        if r==3:
            if int(mouse.heading())== 90:
                self.shape("assets/mouse_top.gif")
            if int(mouse.heading())== 180:
                self.shape("assets/mouse_left.gif")
            if int(mouse.heading())== 270:
                self.shape("assets/mouse_down.gif")
            if int(mouse.heading())== 0:
                self.shape("assets/mouse_right.gif")
            return(mouse.right(90))
        if r==4:
            return(mouse.back(45))
