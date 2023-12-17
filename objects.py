import pygame


class Block:
    """Класс "Block" описывает блоки."""
    def __init__(self, screen, x, y):
        self.id = "block"
        self.screen = screen
        self.x = x
        self.y = y
        self.w = 40
        self.h = 40


class Wall:
    """Класс "Wall" описывает стены"""
    def __init__(self, screen, x, y, w, h):
        self.id = "wall"
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h


class Trap:
    """Класс "Trap" описывает ловушки"""
    def __init__(self, screen, x, y, w, h):
        self.id = "trap"
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h


if __name__ == "__main__":
    print("This module is not for direct call!")