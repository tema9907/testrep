import random
import randmove
from turtle import *
setup(1000, 1000)
Screen()
title("Turtle Keys")
sec  = Turtle("circle")
sec.showturtle()
sec.penup()
sec.setx(100)
sec.sety(100)
#sec.goto(random.randint(0,900),random.randint(0,900))
move = Turtle()
move.penup()
#showturtle()
def k1():
    move.forward(45)
    randmove.randmov(sec)
    if sec.position() == move.position():
        print("словил")
def k2():
    move.left(45)
    randmove.randmov(sec)
    if sec.position() == move.position():
        print("словил")
def k3():
    move.right(45)
    randmove.randmov(sec)
    if sec.position() == move.position():
        print("словил")
def k4():
    move.back(45)
    randmove.randmov(sec)
    if sec.position() == move.position():
        print("словил")
onkey(k1, "Up")   
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")
listen()
mainloop()
