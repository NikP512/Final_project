import pygame
from platformer_player import *
from platformer_objects import *
from platformer_layer import *


class level_editor:
    def __init__(self, screen, layer):
        self.screen = screen
        self.layer = layer
        self.classes_dictionary = {"1": Block}
        self.type = "1"
        self.x, self.y = pygame.mouse.get_pos()

    def set_mouse_position(self):
        self.x, self.y = pygame.mouse.get_pos()
    def add_block(self):
        keys = pygame.key.get_pressed()
        key = pygame.MOUSEBUTTONDOWN
        if key == 1 or keys[pygame.K_q]:
            self.layer.objects.append(self.classes_dictionary["1"](self.screen, self.x//20*20 + 10, self.y//20*20 + 10))

    def choose_type(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.type = "1"


HEIGHT = 800
WIDTH = 800
RUNNING = True
FPS = 60


def check_events():
    """Функция, обрабатывающая нажатие клавиш.
    Возвращает список всех нажатых клавиш.
    """
    global RUNNING

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    keys = pygame.key.get_pressed()
    return keys

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    layers = list()
    layers.append(ScreenLayer(screen, 1, []))
    layers.append(ScreenLayer(screen, 2, []))
    editor = level_editor(screen, layers[0])

    while RUNNING:
        screen.fill((255, 255, 255))
        keys = check_events()
        for layer in layers:
            layer.update()
        pygame.display.update()
        editor.set_mouse_position()
        editor.add_block()
        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()


main()