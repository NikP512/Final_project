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
        """Отрисовка заднего фона и кнопок"""
        image = self.background_image
        scale_image = pygame.transform.scale(image, (self.screen.get_width(), self.screen.get_height()))
        scale_rect = scale_image.get_rect(center=(self.screen.get_width()//2, self.screen.get_height()//2))
        self.screen.blit(scale_image, scale_rect)

        for obj in self.buttons:
            scale_image = pygame.transform.scale(self.button_image, (obj.w, obj.h))
            scale_rect = scale_image.get_rect(center=(obj.x, obj.y))
            self.screen.blit(scale_image, scale_rect)

    def check_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for button in self.buttons:
                    button_rect = pygame.Rect(button.x - button.w//2, button.y - button.h//2, button.w, button.h)
                    if button_rect.collidepoint((x, y)):
                        pass


class Button(Object):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)

    def move(self):
        pass


if __name__ == "__main__":
    print("This module is not for direct call!")
