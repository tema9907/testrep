import random
import randmove
import time
from threading import Thread
from turtle import *
image ='cat.gif'
setup(1000, 1000)

scre=Screen()
scre.addshape(image)
scre.addshape("cat_left.gif")
title("Turtle Keys")
sec  = Turtle("circle")
sec.showturtle()
sec.penup()
sec.setx(100)
sec.sety(100)
def move_mouse():
    for i in range(10000):
        time.sleep(0.5)
        randmove.randmov(sec)

thread = Thread(target=move_mouse)
thread.start()

move = Turtle()
move.penup()
move.shape(image)


def k1():
    move.forward(45)

    if sec.position() == move.position():
        print("словил")
def k2():
    move.left(90)
    move.shape("cat_left.gif")
    print(move.heading())
    if int(move.heading())== 90:
        move.shape("cat_left.gif")
    if sec.position() == move.position():
        print("словил")
def k3():
    move.right(90)
    print("povorot"+move.heading())
    if sec.position() == move.position():
        print("словил")
def k4():
    move.back(45)
    if sec.position() == move.position():
        print("словил")
onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")
listen()
mainloop()
thread.join()
