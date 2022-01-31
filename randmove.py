import random
from turtle import Turtle


def randmov(a:Turtle):
    r=random.randint(1, 4) 
    if r==1:
        
        return(a.forward(45))
    if r==2:
       return(a.left(90))
    if r==3:
        return(a.right(90))
    if r==4:
        return(a.back(45))