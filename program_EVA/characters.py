"""
В данном модуле прописаны параметры и способности персонажа, а также выбор персонажей в меню
"""
from enemies import *

class Character():
    # Класс персонажа: его характеристики, отображение на экране и возможность прыжка
    def __init__(self, type, height=150, width=150):
        """Основные параметры персонажа"""
        try:
            self.horizontal_coordinate, self.vertical_coordinate = 0, 0
            self.height, self.width = height, width
            self.type = type
            self.jumping = False
            self.jump_height = 11.5
        except HeightError:
            raise HeightError("Высота персонажа должна быть положительным числом")
        except WidthError:
            raise WidthError("Ширина персонажа должна быть положительным числом")

    def appearance(self):
        """Появление персонажа на дисплее"""
        try:
            display.blit(self.type, (self.horizontal_coordinate, self.vertical_coordinate, self.height, self.width))
        except:
            raise ValueError("Координаты персонажа должны быть числами")

    def jump(self):
        """Функция, чтобы персонаж мог прыгать через врагов"""
        try:
            jump_speed = 0.5 # Коэффициент ускорения прыжка
            jump_way = (self.jump_height ** 2) # Прыжок описан по сути как парабола
            if self.jumping:
                if self.jump_height >= -11.5:
                    if self.jump_height >= 0:
                        negative_sign_factor = 1 # Пока персонаж не достигнет заданной точки по Оy (высота прыжка), то он будет смещаться вверх
                    else:
                        negative_sign_factor = -1 # Как только он будет в пиковой точке, но начнется опускаться
                    self.vertical_coordinate -= jump_way * jump_speed * negative_sign_factor
                    self.jump_height -= 1
                else:
                    self.jumping = False
                    self.jump_height = 11.5
        except:
            raise ValueError("Высота прыжка должна быть числом")

def type_of_character(type):
    """Выбор персонажа"""
    global character
    characters = [ Character(character_type_one), # Аянами
                   Character(character_type_two)  # Аска
    ]

    while True:
        # Отображение фона и персонажа на дисплее
        display.blit(background, (0, 0))
        for i, character in enumerate(characters):
            character.appearance()
            #Позиционируем персонажей
            character.vertical_coordinate = 150
            character.horizontal_coordinate = 330 + i * 230

        # Параметры текста на экране
        font = pygame.font.Font(None, 60)
        text = font.render("Нажмите \"1\" или \"2\", чтобы выбрать персонажа", True, (225, 225, 225))
        display.blit(text, (110, 90))
        pygame.display.update()

        # Проверяем все действия с кнопками в меню
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                return None

            try:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return characters[0]  # Возвращаем персонажа 1
                    elif event.key == pygame.K_2:
                        return characters[1]  # Возвращаем персонажа 2
                    else:
                        raise TextError()
            except TextError as e:
                TextError.show_error_message(e)