import random
from turtle import Turtle


def randmov(a:Turtle, screen_height, screen_width):
    r=random.randint(1, 4)
    mxcor = a.xcor()
    mycor = a.ycor()
    if abs(mxcor) + 45 >= screen_width or abs(mycor) + 45 >= screen_height:
        r = random.choice([2, 3])
    if r==1:
        return(a.forward(45))
    if r==2:
        if int(a.heading())== 90:
            a.shape("assets/mouse_top.gif")
        if int(a.heading())== 180:
            a.shape("assets/mouse_left.gif")
        if int(a.heading())== 270:
            a.shape("assets/mouse_down.gif")
        if int(a.heading())== 0:
            a.shape("assets/mouse_right.gif")
        return(a.left(90))
    if r==3:
        if int(a.heading())== 90:
            a.shape("assets/mouse_top.gif")
        if int(a.heading())== 180:
            a.shape("assets/mouse_left.gif")
        if int(a.heading())== 270:
            a.shape("assets/mouse_down.gif")
        if int(a.heading())== 0:
            a.shape("assets/mouse_right.gif")
        return(a.right(90))
    if r==4:
        return(a.back(45))