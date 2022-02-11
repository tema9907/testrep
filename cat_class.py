from turtle import *
import turtle
from playsound import playsound
from drawing_class import Drawing


class Cat(Turtle):  # Конструктор

    def __init__(self, mouse, shape: str = "assets/cat_top.gif", visible: bool = True) -> None:
        super().__init__(shape, visible)
        self.penup()
        self.shape("assets/cat_right.gif")
        self.mouse = mouse
        self.score = 0

    def caught(self, mouse):  # Коллизия кота
        if self.score == 0:
            Drawing.draw_score(self.score)
        cxcor = self.xcor()  # Координаты кота
        cycor = self.ycor()
        mxcor = mouse.xcor()  # Координаты мыши
        mycor = mouse.ycor()
        print("cat(%i,%i) mouse(%i,%i)" % (cxcor, cycor, mxcor, mycor))  # Вывод в консоль координат сущностей
        if (cxcor >= mxcor - 20) and (cxcor <= mxcor + 20) and (cycor >= mycor - 20) and (cycor <= mycor + 20):
            self.score += 1
            playsound('assets/wilhelm_scream.mp3')  # Проигрывание звука "Крик Вингельма"
            Drawing.draw_star(mxcor, mycor, 15, "red")  # Рисование звезды
            Drawing.draw_score(self.score)  # Рисование счета

    def cat_move(self):  # События Движения кота
        onkey(self.k1, "Up")
        onkey(self.k2, "Left")
        onkey(self.k3, "Right")
        onkey(self.k4, "Down")
        onkey(turtle.Screen().bye, "Escape")  # Выход из программы
        listen()

    def k1(self):  # Поворот и движение кота
        self.setheading(90)
        self.shape("assets/cat_top.gif")  # Модель кота
        if self.ycor() + 50 <= 500 / 2:  # Условие, непозволяющее коту уйти с поля
            self.forward(45)
        self.caught(self.mouse)

    def k2(self):  # Поворот и движение кота
        self.setheading(180)
        self.shape("assets/cat_left.gif")  # Модель кота
        if self.xcor() - 50 >= -500 / 2:  # Условие, непозволяющее коту уйти с поля
            self.forward(45)
        self.caught(self.mouse)

    def k3(self):  # Поворот и движение кота
        self.setheading(0)
        self.shape("assets/cat_right.gif")  # Модель кота
        if self.xcor() + 50 <= 500 / 2:  # Условие, непозволяющее коту уйти с поля
            self.forward(45)
        self.caught(self.mouse)

    def k4(self):  # Поворот и движение кота
        self.setheading(270)
        self.shape("assets/cat_down.gif")  # Модель кота
        if self.ycor() - 50 >= -500 / 2:  # Условие, непозволяющее коту уйти с поля
            self.forward(45)
        self.caught(self.mouse)
