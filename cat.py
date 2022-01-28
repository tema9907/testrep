import random
import randmove
import time
from threading import Thread
from turtle import *

# for artem

setup(1000, 1000)
Screen()
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

# random move mouse


def move_mouse():
    for i in range(10000):
        time.sleep(0.5)
        randmove.randmov(mouse)


thread = Thread(target=move_mouse)
thread.start()


# cat.goto(random.randint(0,900),random.randint(0,900))
cat = Turtle()
cat.penup()
# showturtle()


def k1():
    cat.forward(45)
    if isCollision(cat, mouse):
        print("словил")


def k2():
    cat.left(45)
    # cat.shapetransform(1.0, 1.0, 0, 0)
    if isCollision(cat, mouse):
        print("словил")


def k3():
    cat.right(45)
    # cat.shapetransform(0, 0, 1.0, 1.0)
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
