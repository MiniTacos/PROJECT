from options import *

class Enemy():
    def __init__(self, height=225, width=50):
        """Основные параметры врагов"""
        self.horizontal_coordinate = display_width #Так как враги появляются справа
        self.vertical_coordinate = 390
        self.height = height
        self.width = width


    def appearance(self):
        """Отображение врага, через которого надо прыгать"""
        display.blit(enemy_image, (self.horizontal_coordinate, self.vertical_coordinate, self.width, self.height))

    def movement(self, move):
        """Передвижение врага"""
        self.horizontal_coordinate -= move