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
        pendown()
        goto(200, 100)
    
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
   

    