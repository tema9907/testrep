from time import sleep
from turtle import *
from threading import *
import turtle

from cat_class import *
from mouse_class import *

class Drawing(Turtle):

    def snowflake(self):
        pass


    def floor():
        turtle.showturtle()
        turtle.speed(0)
        turtle.penup()
        turtle.goto(-250, 260)
        turtle.pendown()
        turtle.color("black")
        turtle.pensize(6)
        turtle.setheading(270)
        turtle.forward(530)
        turtle.penup()
        turtle.goto(250, 260)
        turtle.pendown()
        turtle.forward(530)
        turtle.penup()
        turtle.hideturtle()


    def draw_star(x,y,size,color):
        turtle.showturtle()
        angle = 120
        turtle.pencolor('black')
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
        turtle.hideturtle()
    

    def draw_score(score):
        turtle.showturtle()
        turtle.penup()
        goto(-340, 235)
        turtle.pendown()
        if score == 0:
            turtle.write("score: "+ str(score), move=False, align="left", font=("Arial", 12, "normal"))
        else:
            turtle.color("white")
            turtle.write("score: " + str(score - 1), move=False, align="left", font=("Arial", 12, "normal"))
            turtle.color("black")
            turtle.write("score: " + str(score), move=False, align="left", font=("Arial", 12, "normal"))
        turtle.hideturtle()
