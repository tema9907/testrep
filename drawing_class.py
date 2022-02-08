from time import sleep
from turtle import *
from threading import *
import turtle

from cat_class import Cat
from mouse_class import Mouse

class Drawing(Turtle):
    def __init__(self) -> None:
        self.our_pen = turtle.Turtle()
        self.our_pen.penup()
        self.floor()


    def snowflake(self):
        pass


    def floor(self):
        
        pass