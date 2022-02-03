import random
import randmove as randmove
import time
from threading import Thread
from turtle import *

# for artem

setup(1000, 1000)
Screen()
scre=Screen()

scre.addshape("assets/cat_left.gif")
scre.addshape("assets/cat_right.gif")
scre.addshape("assets/cat_top.gif")
scre.addshape("assets/cat_down.gif")
scre.addshape('assets/mouse_left.gif')
scre.addshape('assets/mouse_right.gif')
scre.addshape('assets/mouse_down.gif')
scre.addshape('assets/mouse_top.gif')
title("Turtle Keys")
mouse = Turtle("circle")
mouse.showturtle()
mouse.penup()
mouse.setx(100)
mouse.sety(100)


def isCollision(cat, mouse):
    cxcor = cat.xcor()
    cycor = cat.ycor()
    mxcor = mouse.xcor()
    mycor = mouse.ycor()
    print("cat(%i,%i) mouse(%i,%i)" % (cxcor, cycor, mxcor, mycor))
    if ((cxcor >= mxcor-20) and (cxcor <= mxcor+20) and (cycor >= mycor-20) and (cycor <= mycor+20)):
        return True
    else:
        return False




def move_mouse():
    for i in range(10000):
        time.sleep(0.5)
        randmove.randmov(mouse)


thread = Thread(target=move_mouse)
thread.start()



cat = Turtle()
cat.penup()
cat.shape("assets/cat_right.gif")
def cat_rotate():
    if int(cat.heading())== 90:
        cat.shape("assets/cat_top.gif")
    if int(cat.heading())== 180:
        cat.shape("assets/cat_left.gif")
    if int(cat.heading())== 270:
        cat.shape("assets/cat_down.gif")
    if int(cat.heading())== 0:
        cat.shape("assets/cat_right.gif")
        

def k1():
    cat.forward(45)
    if isCollision(cat, mouse):
        print("словил")


def k2():
    cat.left(90)
    print(cat.heading())
    cat_rotate()
    if isCollision(cat, mouse):
        print("словил")


def k3():
    cat.right(90)
    cat_rotate()
    if isCollision(cat, mouse):
        print("словил")


def k4():
    cat.back(45)
    if isCollision(cat, mouse):
        print("словил")


onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")
listen()
mainloop()
thread.join()
