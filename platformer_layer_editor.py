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
        is_there_block = False
        for object in self.layer.objects:
            rect = pygame.Rect(object.x - object.w / 2, object.y - object.h / 2, object.w, object.h)
            is_there_block += rect.collidepoint(self.x, self.y)
        if key == 1 or keys[pygame.K_q] and not is_there_block:
            self.layer.objects.append(self.classes_dictionary[self.type](self.screen, self.x//20*20 + 10, self.y//20*20 + 10))

    def write_objects_to_file(self, output_filename):
        """
        """
        with open(output_filename, 'w') as out_file:
            for object in self.layer.objects:
                s = object.id
                s += " " + str(object.x) + " " + str(object.y) + "\n"
                out_file.write(s)

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

    editor.write_objects_to_file("1.1")
    pygame.quit()


main()