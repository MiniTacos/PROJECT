"""
Модуль используется для отображения объектов-врагов, через которых надо перепрыгивать, а также их основных параметров
"""
from exceptions import *

class Enemy():
    def __init__(self, height=225, width=50):
        """Основные параметры врагов"""
        try:
            self.horizontal_coordinate = display_width #Так как враги появляются справа, их начальная координата будет тоже справа
            self.vertical_coordinate = 340
            self.height = height
            self.width = width
        except HeightError:
            raise HeightError("Высота объекта должна быть положительным числом")
        except WidthError:
            raise WidthError("Ширина объекта должна быть положительным числом")

    def appearance(self):
        """Отображение врага, через которого надо прыгать"""
        try:
            pygame.draw.rect(display, (52, 228, 123), (self.horizontal_coordinate, self.vertical_coordinate, self.width, self.height))
        except:
            raise ValueError("Координаты должны быть числами")

    def movement(self, move):
        """Передвижение врага"""
        try:
            self.horizontal_coordinate -= move
        except:
            raise ValueError("Координаты должны быть числами")