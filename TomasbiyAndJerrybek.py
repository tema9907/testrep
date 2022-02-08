import imp
from time import sleep
from turtle import *
from threading import *

from cat_class import Cat
from mouse_class import Mouse
from drawing_class import *


class TomasbiyAndJerrybek():
    def __init__(self) -> None:
        self.screen_height = 500
        self.screen_width  = 700
        # setup(600, 600)
        setup(self.screen_width, self.screen_height)
        Screen()
        screen=Screen()
        title("Tomasbiy and Jerrybek")
        screen.addshape("assets/cat_left.gif")
        screen.addshape("assets/cat_right.gif")
        screen.addshape("assets/cat_top.gif")
        screen.addshape("assets/cat_down.gif")
        screen.addshape("assets/mouse_left.gif")
        screen.addshape("assets/mouse_right.gif")
        screen.addshape("assets/mouse_down.gif")
        screen.addshape("assets/mouse_top.gif")
        self.cat = Cat()
        self.mouse = Mouse()
        
        self.start()
        #self.interface()


    def interface(self):
        Drawing.floor()
        print("1111111111111111")
        Drawing.draw_star(100,"purple")


    def start(self):
        Drawing.floor()
        print("1111111111111111")
        Drawing.draw_star(100,"purple")
        self.cat.cat_move()
        
        thread_mouse = Thread(target = self.mouse.move_mouse(self.mouse, self.cat))
        thread_mouse.start()
        thread_collision = Thread(target=self.isCollision)
        thread_collision.start()
        mainloop()
        thread_mouse.join()
        thread_collision.join()

    