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
        self.x, self.y = pygame.mouse.get_pos

    def add_block(self):
        key = pygame.MOUSEBUTTONDOWN
        if key == 1:
            self.layer.objects.append(self.classes_dictionary["1"](self.screen, self.x//20 + 10, self.y//20 + 10))

    def choose_type(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.type = "1"

