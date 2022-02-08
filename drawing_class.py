from time import sleep
from turtle import *
from threading import *
import turtle

from cat_class import Cat
from mouse_class import Mouse

class Drawing(Turtle):

    def snowflake(self):
        pass


    def floor():
        speed(0)
        penup()
        goto(-250, 260)
        pendown()
        color("black")
        pensize(6)
        setheading(270)
        forward(530)
        penup()
        goto(250, 260)
        pendown()
        forward(530)
        penup()


    def draw_star(size,color):
        angle = 120
        turtle.fillcolor(color)
        turtle.begin_fill()

        for side in range(5):
            turtle.forward(size)
            turtle.right(angle)
            turtle.forward(size)
            turtle.right(72 - angle)
        turtle.end_fill()
   

    