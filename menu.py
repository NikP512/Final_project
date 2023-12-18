import pygame


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.choose_level = 0
        self.choose_player = 0
        self.background_image = None
        self.button_image = None
        self.buttons = []

    def update(self):
        """Добавить отрисовку заднего фона и кнопок по аналогии с objects.py"""
        pass

    def check_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
                break
            # Добавить проверку, что мы ткнули на кнопку. Использовать pygame.collidepoint
            pass


class Button:
    """Добавить констркутор. Атрибуты: координатцы центра кнопки x, y и размеры w, h."""
    pass


if __name__ == "__main__":
    print("This module is not for direct call!")
