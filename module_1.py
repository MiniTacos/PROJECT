import pygame
import random

#Инициализация всей программы
pygame.init()

#Параметры дисплея
display_height = 600
display_width = 1200
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Python project")
pygame.display.set_icon(pygame.image.load("images/icon.png"))

#Загрузка изображений
background = pygame.image.load("images/bg6.jpg")
character_type_one = pygame.image.load("images/player2.png")
character_type_two = pygame.image.load("images/player3.png")
lose = pygame.image.load("images/lose.png")

#Настройка времени и гравитации в игре
clock = pygame.time.Clock()