from cmath import asin
from time import sleep
from turtle import *
from threading import *
import turtle
from math import sin, pi
# import asyncio
from cat_class import *
from mouse_class import *


class Drawing(Turtle):  # Класс Илюстратор

    @staticmethod
    def snowflake():  # Снежинка по синусоиде
        angle = 0
        turtle.speed(0)
        turtle.pensize(2)
        while angle < 2 * pi:
            turtle.goto(40 * sin(angle) + 314, -40 * angle + 132)  # Выбор по синусоиде где рисовать снежинку
            angle += 0.4  # Угол меняется на 0.4
            turtle.penup()
            if angle // 30 == 0:  # Каждые 30 градусов рисуем снежинку
                turtle.pendown()
                for _ in range(0, 6):  # Снежинка в цикле
                    turtle.forward(10)
                    turtle.forward(-4)
                    turtle.left(40)
                    turtle.forward(3)
                    turtle.forward(-3)
                    turtle.right(80)
                    turtle.forward(3)
                    turtle.forward(-3)
                    turtle.left(40)
                    turtle.forward(-6)
                    turtle.right(60)  # Поворот на 60 градусов, рисуем 6 раз. 6*60=360 круг
                turtle.penup()
                turtle.pencolor("black")
                turtle.penup()

    @staticmethod
    def floor():  # Пол
        turtle.showturtle()
        turtle.speed(0)
        turtle.penup()
        turtle.goto(-250, -250)  # Рисуем линии пола
        turtle.pensize(2)  # 2 пикселя ручка
        turtle.pendown()
        turtle.setheading(0)  # Смотрим вниз
        turtle.pencolor("brown")  # Коричневый увет
        for i in range(23):  # Рисуем полосы пола
            turtle.forward(500)
            turtle.penup()
            turtle.goto(-250, -250 + i * 24)  # каждые 24 пикселя
            turtle.pendown()
        turtle.pencolor("black")
        turtle.penup()
        turtle.goto(-250, 260)  # Идем рисовать боковые полосы игроовго поля
        turtle.pendown()
        turtle.color("black")  # Полосы - черные
        turtle.pensize(6)
        turtle.setheading(270)
        turtle.forward(530)
        turtle.penup()
        turtle.goto(250, 260)  # Идем рисовать вторую полосу
        turtle.pendown()
        turtle.forward(530)
        turtle.penup()
        turtle.hideturtle()

    def draw_star(x, y, size, color):  # Звезда на месте ловли
        turtle.showturtle()
        angle = 120
        turtle.pencolor('black')
        turtle.penup()
        turtle.goto(x, y)
        turtle.fillcolor(color)  # Выбираем цвет заливки
        turtle.begin_fill()
        turtle.pendown()
        for side in range(5):  # Рисуем звезду в цикле
            turtle.forward(size)
            turtle.right(angle)
            turtle.forward(size)
            turtle.right(72 - angle)
        turtle.end_fill()  # Заливаем звезду
        turtle.hideturtle()

    def draw_score(score):  # Рисование Очков
        turtle.showturtle()
        turtle.penup()
        goto(-365, 235)
        # turtle.pendown()
        if score == 0:  # Пишем счет 0
            turtle.write("score: " + str(score), move=False, align="left", font=("Arial", 12, "normal"))
        else:  # Стираем предыдущий счет и пишем новый
            turtle.color("white")  # Пишем белым на черном - стираем
            turtle.write("score: " + str(score - 1), move=False, align="left", font=("Arial", 12, "normal"))
            turtle.color("black")  # Пишем новый счет черным цветом
            turtle.write("score: " + str(score), move=False, align="left", font=("Arial", 12, "normal"))
        turtle.hideturtle()
        if score // 4 != 0 and score != 0:  # Каждые 4 очка рисуется снежинка
            Drawing.snowflake()

    @staticmethod
    def authors():  # Надпись авторов
        authors = turtle.Turtle()  # Создание черепахи
        authors.penup()  # Поднять ручку, чтобы не черкать пока перемещаем
        authors.hideturtle()  # Прячем
        authors.speed(0)  # Самая быстрая скорость
        authors.goto(255, 220)  # Перемещение к координатам надписи
        authors.write("Выполнили:", move=False, align="left", font=("Arial", 12, "normal"))  # Пишем текст
        authors.goto(255, 205)
        authors.write("Жантурин", move=False, align="left", font=("Arial", 12, "normal"))
        authors.goto(255, 190)
        authors.write("Одарич", move=False, align="left", font=("Arial", 12, "normal"))
        authors.goto(255, 175)
        authors.write("Семейников", move=False, align="left", font=("Arial", 12, "normal"))
        authors.goto(255, 160)
        authors.write("Долгушин", move=False, align="left", font=("Arial", 12, "normal"))
