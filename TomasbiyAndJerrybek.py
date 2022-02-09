from time import sleep
from turtle import *
from threading import *
# import asyncio
from cat_class import *
from mouse_class import Mouse
from drawing_class import *


class TomasbiyAndJerrybek():
    def __init__(self) -> None:
        self.screen_height = 512
        self.screen_width  = 750
        # setup(600, 600)
        setup(self.screen_width, self.screen_height)
        #Screen()
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
        self.interface()
        self.mouse = Mouse()
        self.cat = Cat(self.mouse)
        self.start()

    def interface(self):
        print("1111111111111111")
        Drawing.floor()
        Drawing.draw_score(0)
        # Drawing.exit_button()
        Drawing.authors()
        
        print("Interface нарисован")

    def start(self):
        self.cat.cat_move()
        thread_mouse = Thread(target = self.mouse.move_mouse(self.mouse, self.cat))
        # thread_mouse.start()
        # thread_snowflake = Thread(target = Drawing.snowflake())
        # thread_snowflake.start()
        # mainloop()
        # thread_snowflake.join()
        # thread_mouse.join()
       

    