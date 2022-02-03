from turtle import *


class Cat(Turtle):

    def __init__(self, shape: str = "assets/cat_top.gif", visible: bool = True) -> None:
        super().__init__(shape, visible)
        self.penup()
        self.shape("assets/cat_right.gif")


    def cat_rotate(self):
        if int(self.heading())== 90:
            self.shape("assets/cat_top.gif")
        if int(self.heading())== 180:
            self.shape("assets/cat_left.gif")
        if int(self.heading())== 270:
            self.shape("assets/cat_down.gif")
        if int(self.heading())== 0:
            self.shape("assets/cat_right.gif")
    
    def cat_move(self):
        onkey(self.k1, "Up")
        onkey(self.k2, "Left")
        onkey(self.k3, "Right")
        onkey(self.k4, "Down")
        listen()
        mainloop()
        
    def k1(self):
        self.forward(45)
        

    def k2(self):
        self.left(90)
        self.cat_rotate()
    
    
    def k3(self):
        self.right(90)
        self.cat_rotate()
    
    
    def k4(self):
        self.back(45)

