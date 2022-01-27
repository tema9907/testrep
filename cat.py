from turtle import *
setup(1000, 1000)
Screen()
title("Turtle Keys")
sec  = Turtle("turtle")
sec.showturtle()
move = Turtle()
move.penup()
#showturtle()
def k1():
    move.forward(45)
def k2():
    move.left(45)
def k3():
    move.right(45)
def k4():
    move.back(45)
onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")
listen()
mainloop()