from time import sleep
from turtle import *
from threading import *
from cat_class import *
from mouse_class import Mouse
from drawing_class import *  # Импорт библиотек


class TomasbiyAndJerrybek():  # Основной игровой класс
    def __init__(self) -> None:
        self.screen_height = 512  # Высота экрана
        self.screen_width = 750  # Ширина экрана
        setup(self.screen_width, self.screen_height)
        screen = Screen()
        title("Tomasbiy and Jerrybek")  # Название игры Томасбай и Джеррибек
        screen.addshape("assets/cat_left.gif")  # Добавление гиф-изображений мыши и кота
        screen.addshape("assets/cat_right.gif")
        screen.addshape("assets/cat_top.gif")
        screen.addshape("assets/cat_down.gif")
        screen.addshape("assets/mouse_left.gif")
        screen.addshape("assets/mouse_right.gif")
        screen.addshape("assets/mouse_down.gif")
        screen.addshape("assets/mouse_top.gif")
        self.interface()  # Рисование интерфейса
        self.mouse = Mouse()  # Создание экземпляра кота
        self.cat = Cat(self.mouse)  # Создание экземпляра мыши
        self.start()  # Запуск игры

    def interface(self):  # Интерфейс Пол, авторы и очки
        Drawing.floor()
        Drawing.draw_score(0)  # Рисование счета 0, так как это только начало игры
        Drawing.authors()
        print("Interface нарисован")

    def start(self):  # Инициализаци и запуск игры.
        self.cat.cat_move()  # Запуск управления котом - listen
        thread_mouse = Thread(target=self.mouse.move_mouse(self.mouse, self.cat))  # Запуск потока с мышью
