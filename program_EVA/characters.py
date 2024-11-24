from enemies import *

class Character():
    #Класс персонажа: его характеристики, отображение на экране и возможность прыжка
    def __init__(self, type, height=80, width=80):
        """Основные параметры персонажа"""
        self.horizontal_coordinate, self.vertical_coordinate = 0, 300
        self.height, self.width = height, width
        self.type = type
        self.jumping = False
        self.jump_height = 11.5

    def appearance(self):
        """Появление персонажа на экране"""
        display.blit(self.type, (self.horizontal_coordinate, self.vertical_coordinate, self.height, self.width))

    def jump(self):
        """Функция, чтобы персонаж мог прыгать через врагов"""
        jump_speed = 0.5 #Коэффициент ускорения прыжка
        jump_way = (self.jump_height ** 2) #Прыжок описан по сути как парабола с отображением по Оy
        if self.jumping:
            if self.jump_height >= -11.5:
                if self.jump_height >= 0:
                    negative_sign_factor = 1 #Пока персонаж не достигнет заданной точки по Оy (высота прыжка), то он будет смещаться вверх
                else:
                    negative_sign_factor = -1 #Как только он будет в пиковой точке, но начнется опускаться
                self.vertical_coordinate -= jump_way * jump_speed * negative_sign_factor
                self.jump_height -= 1
            else:
                self.jumping = False
                self.jump_height = 11.5

def type_of_character(type):
    """Выбор персонажа"""
    characters = [ Character(character_type_one),
                   Character(character_type_two)
    ]

    while True:
        #Отображение фона и персонажа на дисплее
        display.blit(background, (0, 0))
        for i, character in enumerate(characters):
            character.appearance()
            #Позиционируем персонажей
            character.horizontal_coordinate = 10 + i * 230

        #параметры текста на экране
        font = pygame.font.Font(None, 60)
        text = font.render("Нажмите \"1\" или \"2\", чтобы выбрать персонажа", True, (225, 225, 225))
        display.blit(text, (100, 90))
        pygame.display.update()

        #Проверяем все действия с кнопками в меню(?)
        for i in pygame.event.get():
            if i.type == pygame.QUIT or (i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE):
                display_start = False
                pygame.quit()
                return None
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_1:
                    return characters[0]
                elif i.key == pygame.K_2:
                    return characters[1]