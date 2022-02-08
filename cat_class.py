from turtle import *


class Cat(Turtle):

    def __init__(self, shape: str = "assets/cat_top.gif", visible: bool = True) -> None:
        super().__init__(shape, visible)
        self.penup()
        self.shape("assets/cat_right.gif")


    def cat_rotate(self):
        if int(self.heading()) == 90:
            return 1
        if int(self.heading()) == 180:
            return 2
        if int(self.heading()) == 270:
            return 3
        if int(self.heading()) == 0:
            return 4
    

    def cat_move(self):
        onkey(self.k1, "Up")
        onkey(self.k2, "Left")
        onkey(self.k3, "Right")
        onkey(self.k4, "Down")
        onkey(exit, "Escape")
        listen()
        

    def k1(self):
        self.setheading(90)
        self.shape("assets/cat_top.gif")
        self.forward(45)
        

    def k2(self):
        self.setheading(180)
        self.shape("assets/cat_left.gif")
        self.forward(45)
    
    
    def k3(self):
        self.setheading(0)
        self.shape("assets/cat_right.gif")
        self.forward(45)
    
    
    def k4(self):
        self.setheading(270)
        self.shape("assets/cat_down.gif")
        self.forward(45)
