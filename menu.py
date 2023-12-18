import pygame


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.choose_level = 0
        self.choose_player = 0
        self.buttons = []

    def update(self):
        self.screen.fill((255, 255, 255))


    def check_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
                break
            pass


class Button:
    pass


if __name__ == "__main__":
    print("This module is not for direct call!")
