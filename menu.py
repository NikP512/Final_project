import pygame
from objects import Object

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
        """Добавить отрисовку заднего фона и кнопок по аналогии с классом Location"""
        pass

    def check_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
                break
            # Добавить проверку, что мы ткнули на кнопку. Использовать pygame.collidepoint
            pass


class Button(Object):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def move(self):
        pass


if __name__ == "__main__":
    print("This module is not for direct call!")
