import random
import time
from turtle import Turtle  # Импорт библиотек


class Mouse(Turtle):  # Класс мыши

    def __init__(self, shape: str = "assets/mouse_top.gif", visible: bool = True) -> None:  # Конструктор Мыши
        super().__init__(shape, visible)
        self.showturtle()
        self.penup()
        self.setx(90)  # Начальные координаты мыши
        self.sety(90)

    def move_mouse(self, mouse, cat):  # Вызов Движения мыши
        c = 199  # Установка счетчика
        while True:
            time.sleep(0.03)  # Итерация каждые 30 миллисекунд
            c += 1
            if c // 200:  # Каждые 200 итераций мышь
                self.randmov(mouse, cat)

    def randmov(self, mouse, cat):  # Случайное событие от 1 до 4 и выбор движения мыши
        screen_height, screen_width = 500, 500  # Установка размера игрового поля для мыши
        r = random.randint(1, 4)
        mxcor = mouse.xcor()  # Координаты мыши
        mycor = mouse.ycor()

        if r == 1 and mycor + 50 <= screen_height / 2:  # Если мышь случайно выбрала идти вверх (1)
            self.setheading(90)  # и через 50 пикселей не граница поля
            self.shape("assets/mouse_top.gif")  # то она может ходить
            self.forward(45)
        if r == 2 and mxcor - 50 >= -screen_width / 2:  # Аналогичные условия для передвижения мыши
            self.setheading(180)  # для 2 - влево, 3 - вправо, 4 - вниз
            self.shape("assets/mouse_left.gif")
            self.forward(45)
        if r == 3 and mxcor + 50 <= screen_width / 2:
            self.setheading(0)
            self.shape("assets/mouse_right.gif")
            self.forward(45)
        if r == 4 and mycor - 50 >= -screen_height / 2:
            self.setheading(270)
            self.shape("assets/mouse_down.gif")
            self.forward(45)
