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
        turtle.goto(-250, -250)
        turtle.pensize(2)
        turtle.pendown()
        turtle.setheading(0)
        turtle.pencolor("brown")
        for i in range(23):
            turtle.forward(500)
            turtle.penup()
            turtle.goto(-250, -250 + i * 24)
            turtle.pendown()
        turtle.pencolor("black")
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
        # turtle.pendown()
        if score == 0:
            turtle.write("score: "+ str(score), move=False, align="left", font=("Arial", 12, "normal"))
        else:
            turtle.color("white")
            turtle.write("score: " + str(score - 1), move=False, align="left", font=("Arial", 12, "normal"))
            turtle.color("black")
            turtle.write("score: " + str(score), move=False, align="left", font=("Arial", 12, "normal"))
        turtle.hideturtle()
    

    def authors():
        authors = turtle.Turtle()
        authors.penup()
        authors.hideturtle()
        authors.speed(0)
        authors.goto(255, 220)
        authors.write("Выполнили:", move=False, align="left", font=("Arial", 12, "normal"))
        authors.goto(255, 205)
        authors.write("Жантурин", move=False, align="left", font=("Arial", 12, "normal"))
        authors.goto(255, 190)
        authors.write("Одарич", move=False, align="left", font=("Arial", 12, "normal"))
        authors.goto(255, 175)
        authors.write("Семейников", move=False, align="left", font=("Arial", 11, "normal"))
        authors.goto(255, 160)
        authors.write("Долгушин", move=False, align="left", font=("Arial", 12, "normal"))


    def exit_button():
        exitTurtle = turtle
        exitTurtle.hideturtle()
        exitTurtle.speed(0)
        exitTurtle.goto(-340, 220)
        exitTurtle.fillcolor("red")
        exitTurtle.onclick(exit, 1, add=False)
        exitTurtle.begin_fill()
        exitTurtle.pendown()
        setheading(0)
        for _ in range(2):
            exitTurtle.forward(80)
            exitTurtle.right(90)
            exitTurtle.forward(40)
            exitTurtle.right(90)
        exitTurtle.end_fill()
        exitTurtle.penup()
        exitTurtle.goto(-300, 160)
        exitTurtle.write("exit", move=False, align="center", font=("Arial", 12, "bold"))
        # def button(x,y):
            # if x < 50 and x > -50 and y < 50 and y > -50:
                # print(f"Your coordinates are: ({x}, {y}).")
        # exitTurtle.onscreenclick(button, 1, add=False)
        # exitTurtle.done()
        # exitTurtle.hideturtle()
