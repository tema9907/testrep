from cat_class import *
from mouse_class import *
from threading import Thread
from turtle import *

# for artem

setup(500, 500)
Screen()
scre=Screen()
title("Turtle Keys")

scre.addshape("assets/cat_left.gif")
scre.addshape("assets/cat_right.gif")
scre.addshape("assets/cat_top.gif")
scre.addshape("assets/cat_down.gif")
scre.addshape("assets/mouse_left.gif")
scre.addshape("assets/mouse_right.gif")
scre.addshape("assets/mouse_down.gif")
scre.addshape("assets/mouse_top.gif")

mouse = Mouse()

cat = Cat()


def isCollision(cat, mouse):
        cxcor = cat.xcor()
        cycor = cat.ycor()
        mxcor = mouse.xcor()
        mycor = mouse.ycor()
        print("cat(%i,%i) mouse(%i,%i)" % (cxcor, cycor, mxcor, mycor))
        if ((cxcor >= mxcor-20) and (cxcor <= mxcor+20) and (cycor >= mycor-20) and (cycor <= mycor+20)):
            print("словил")
        else:
            return 0
            
onkey(cat.k1, "Up")
onkey(cat.k2, "Left")
onkey(cat.k3, "Right")
onkey(cat.k4, "Down")

thread = Thread(target = mouse.move_mouse(mouse))
thread.start()
# mouse.move_mouse(mouse)



listen()
mainloop()
thread.join()
