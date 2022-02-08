import imp
from turtle import *
import turtle
from playsound import playsound
from drawing_class import Drawing


class Cat(Turtle):

    def __init__(self, mouse, shape: str = "assets/cat_top.gif", visible: bool = True) -> None:
        super().__init__(shape, visible)
        self.penup()
        self.shape("assets/cat_right.gif")
        self.mouse = mouse
        self.score = 0


    def caught(self, mouse):
        Drawing.draw_score(self.score)
        cxcor = self.xcor()
        cycor = self.ycor()
        mxcor = mouse.xcor()
        mycor = mouse.ycor()
        print("cat(%i,%i) mouse(%i,%i)" % (cxcor, cycor, mxcor, mycor))
        if ((cxcor >= mxcor-20) and (cxcor <= mxcor+20) and (cycor >= mycor-20) and (cycor <= mycor+20)):
            print("словил")
            self.score += 1
            # mouse.hideturtle()
            playsound('assets/wilhelm_scream.mp3')
            Drawing.draw_star(mxcor, mycor, 15, "red")
            Drawing.draw_score(self.score)


    def cat_move(self):
        onkey(self.k1, "Up")
        onkey(self.k2, "Left")
        onkey(self.k3, "Right")
        onkey(self.k4, "Down")
        onkey(turtle.Screen().bye, "Escape")
        listen()
        

    def k1(self):
        self.setheading(90)
        self.shape("assets/cat_top.gif")
        self.forward(45)
        self.caught(self.mouse)
        

    def k2(self):
        self.setheading(180)
        self.shape("assets/cat_left.gif")
        self.forward(45)
        self.caught(self.mouse)
    
    
    def k3(self):
        self.setheading(0)
        self.shape("assets/cat_right.gif")
        self.forward(45)
        self.caught(self.mouse)
    
    
    def k4(self):
        self.setheading(270)
        self.shape("assets/cat_down.gif")
        self.forward(45)
        self.caught(self.mouse)
