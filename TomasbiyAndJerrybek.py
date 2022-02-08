from time import sleep
from turtle import *
from threading import *

from cat_class import Cat
from mouse_class import Mouse

class TomasbiyAndJerrybek():
    def __init__(self) -> None:
        self.screen_height = 600
        self.screen_width  = 600
        # setup(600, 600)
        setup(self.screen_height, self.screen_width)
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

<<<<<<< HEAD

    def interface(self):
        pass

=======
>>>>>>> ed64282d91142386e8802a9aa35fbec0ec2d23cd

    def start(self):
        self.cat.cat_move()
        thread_mouse = Thread(target = self.mouse.move_mouse(self.mouse, self.cat))
        thread_mouse.start()
        thread_collision = Thread(target=self.isCollision)
        thread_collision.start()
        mainloop()
        thread_mouse.join()
        thread_collision.join()

    