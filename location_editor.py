import pygame
from player import *
from objects import *
from location import *
import random


class LocationEditor:
    def __init__(self, screen, layer):
        self.screen = screen
        self.layer = layer
        self.classes_dictionary = {30: Block, 31: Wall}
        self.type = 30
        self.x, self.y = pygame.mouse.get_pos()
        self.stage = 0
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.time = pygame.time.get_ticks()

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
            self.layer.objects.append(self.classes_dictionary[self.type](self.screen,
                                                                         self.x//20*20 + 10,
                                                                         self.y//20*20 + 10))

    def add_wall(self):
        keys = pygame.key.get_pressed()
        surf = pygame.Surface((abs(self.x - self.start_x), abs(self.y - self.start_y)))
        surf.fill((255, 255, 0))
        surf.set_alpha(100)
        self.screen.blit(surf, (min(self.start_x, self.x), min(self.start_y, self.y)))
        if (keys[pygame.K_s]) and (self.stage <= 1):
            self.start_x = self.x
            self.start_y = self.y
            self.stage = 1
        if (keys[pygame.K_e]) and (self.stage == 1) and (pygame.time.get_ticks() - self.time > 200):
            self.end_x = self.x
            self.end_y = self.y
            self.stage += 1
            self.time = pygame.time.get_ticks()
        if self.stage == 2:
            self.stage = 1
            self.layer.objects.append(self.classes_dictionary[self.type](self.screen,
                                                                         (self.start_x + self.end_x)//2,
                                                                         (self.start_y+self.end_y)//2,
                                                                         abs(self.start_x-self.end_x),
                                                                         abs(self.start_y-self.end_y)))

    def add_wall_random(self):
        if self.stage <= 1:
            self.start_x = random.randint(0, 800)
            self.start_y = random.randint(0, 800)
            self.stage = 1
        if (self.stage == 1) and (pygame.time.get_ticks() - self.time > 200):
            self.end_x = random.randint(self.start_x + 10, self.start_x + 20)
            self.end_y = random.randint(self.start_y + 1, self.start_y + 5)
            self.stage += 1
            self.time = pygame.time.get_ticks()
        if self.stage == 2:
            self.stage = 1
            self.layer.objects.append(self.classes_dictionary[self.type](self.screen,
                                                                         (self.start_x + self.end_x)//2,
                                                                         (self.start_y+self.end_y)//2,
                                                                         abs(self.start_x-self.end_x),
                                                                         abs(self.start_y-self.end_y)))


    def write_objects_to_file(self, output_filename):
        """
        """
        with open(output_filename, 'w') as out_file:
            for object in self.layer.objects:
                s = object.id
                if s == "block":
                    s += " " + str(object.x) + " " + str(object.y) + "\n"
                elif s == "wall":
                    s += " " + str(object.x) + " " + str(object.y) + " " + str(object.w) + " " + str(object.h) + "\n"
                out_file.write(s)

    def choose_type(self):
        keys = pygame.key.get_pressed()
        if 1 in keys:
            if keys.index(1) in self.classes_dictionary.keys():
                self.type = keys.index(1)


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
    layers.append(Location(screen, 1, []))
    layers.append(Location(screen, 2, []))
    editor = LocationEditor(screen, layers[0])

    while RUNNING:
        screen.fill((255, 255, 255))
        keys = check_events()
        for layer in layers:
            layer.update()
        editor.choose_type()
        editor.set_mouse_position()
        if editor.type == 30:
            editor.add_block()
        if editor.type == 31:
            editor.add_wall()
        clock.tick(FPS)
        pygame.display.update()

    editor.write_objects_to_file("1.1")
    pygame.quit()


main()
