from time import sleep
from turtle import *
from threading import *
import turtle

from cat_class import Cat
from mouse_class import *

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


    def draw_star(x,y,size,color):
        
        angle = 120
        turtle.penup()
        turtle.goto(x,y)
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.pendown()
        for side in range(5):
            turtle.forward(size)
            turtle.right(angle)
            turtle.forward(size)
            turtle.right(72 - angle)
        turtle.end_fill()
   

    def draw_score(score):
        turtle.penup()
        goto(100,100)
        turtle.pendown()
        write("score"+ str(score), move=False, align="left", font=("Arial", 12, "normal"))