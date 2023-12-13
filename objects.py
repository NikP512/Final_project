import pygame
from location import *


class Block:
    """Класс "Block" описывает блоки."""
    def __init__(self, screen, x, y):
        self.id = "block"
        self.screen = screen
        self.x = x
        self.y = y
        self.w = 20
        self.h = 20
        self.file_name = "block.png"


class Wall:
    """Класс "Wall" описывает стены"""
    def __init__(self, screen, x, y, w, h):
        self.id = "wall"
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.file_name = "wall.png"


class Trap:
    """Класс "Trap" описывает ловушки"""
    def __init__(self, screen, x, y, w, h):
        self.id = "trap"
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.file_name = "trap.png"


if __name__ == "__main__":
    print("This module is not for direct call!")
