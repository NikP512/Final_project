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
    def __init__(self, screen, x, y, w, h, vx, vy):
        self.id = "wall"
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vx = vx
        self.vy = vy


class Trap:
    """Класс "Trap" описывает ловушки"""
    def __init__(self, screen, x, y, w, h, vx, vy):
        self.id = "trap"
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.w = w
        self.h = h

    def move(self):
        "Функции движения ловушек. Метод описывает перемещение ловушки за один кадр перерисовки."
        self.x += self.vx
        self.y += self.vy


if __name__ == "__main__":
    print("This module is not for direct call!")