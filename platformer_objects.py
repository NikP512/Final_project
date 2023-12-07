import pygame


class Floor:
    """Класс, описывающий положение пола на данном слое. Пол представляет собой прямоугольник,
    с координатами (x, y) верхнего левого угла, высотой h и шириной w."""
    def __init__(self, screen, x, y, w, h):
        self.id = "floor"
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        """Функция, рисующая пол."""
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.w, self.h))


class Block:
    """Класс "Block" описывает блоки."""
    def __init__(self, screen, x, y):
        self.id = "block"
        self.screen = screen
        self.x = x
        self.y = y
        self.w = 20
        self.h = 20
        self.file_name = ""


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
    def __init__(self, screen, x, y, r):
        self.id = "trap"
        self.screen = screen
        self.x = x
        self.y = y
        self.r = r
        self.file_name = ""


if __name__ == "__main__":
    print("This module is not for direct call!")
