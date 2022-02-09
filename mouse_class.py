import random
import time
from playsound import playsound
from turtle import Turtle, screensize


class Mouse(Turtle):

    def __init__(self, shape: str = "assets/mouse_top.gif", visible: bool = True) -> None:
        super().__init__(shape, visible)
        self.showturtle()
        self.penup()
        self.setx(90)
        self.sety(90)


    def move_mouse(self, mouse, cat):
        c = 199
        while True:
            time.sleep(0.03)
            c += 1
            if c // 200:
                self.randmov(mouse, cat)
                # cxcor = cat.xcor()
                # cycor = cat.ycor()
                # mxcor = mouse.xcor()
                # mycor = mouse.ycor()
                # print("cat(%i,%i) mouse(%i,%i)" % (cxcor, cycor, mxcor, mycor))
                # if ((cxcor >= mxcor-20) and (cxcor <= mxcor+20) and (cycor >= mycor-20) and (cycor <= mycor+20)):
                #     print("словил")
                #     self.score+=1
                #     self.hideturtle()
                #     playsound('assets/wilhelm_scream.mp3')
                #     Drawing.draw_star(mxcor, mycor, 15, "red")
                #     DrawScore.draw_score(self.score)
                # else:
                #     pass


    def randmov(self, mouse, cat):
        # self.showturtle()
        screen_height, screen_width = 500, 500
        r=random.randint(1, 4)
        mxcor = mouse.xcor()
        mycor = mouse.ycor()
        
        if r==1 and mycor + 50 <= screen_height/2:
            self.setheading(90)
            self.shape("assets/mouse_top.gif")
            self.forward(45)
        if r==2 and mxcor - 50 >= -screen_width/2:
            self.setheading(180)
            self.shape("assets/mouse_left.gif")
            self.forward(45)
        if r==3 and mxcor + 50 <= screen_width/2:
            self.setheading(0)
            self.shape("assets/mouse_right.gif")
            self.forward(45)
        if r==4 and mycor - 50 >= -screen_height/2:
            self.setheading(270)
            self.shape("assets/mouse_down.gif")
            self.forward(45)

       