"""
Модуль с исключениями
"""
from options import *

class WidthError(Exception):
    """Исключение для ошибок, связанных с шириной"""
    pass
    def set_character_width(width):
        """Устанавливает ширину"""
        if width <= 0:
            raise WidthError()

class HeightError(Exception):
    """Исключение для ошибок, связанных с высотой"""
    def set_character_width(height):
        """Устанавливает высоту"""
        if height <= 0:
            raise HeightError()

class NumberFormatError(Exception):
    """Исключение для ошибок, связанных с числами"""
    def set_character_coordinates(x, y):
        """Проверка формата"""
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise NumberFormatError()

class TextError(Exception):
    """Text"""
    def show_error_message(self):
        """Показывает сообщение об ошибке на экране"""
        font = pygame.font.Font(None, 60)
        error_text = font.render("Прочитай, что написано выше!", True, (255, 0, 0))
        display.blit(error_text, (275, 500))
        pygame.display.update()
        pygame.time.wait(1000)