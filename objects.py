import pygame.time


class Object:
    def __init__(self, x, y, w, h, vx=0, vy=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vx = vx
        self.vy = vy

    def move(self):
        self.x += self.vx
        self.y += self.vy


class Block(Object):
    """Класс "Block" описывает блоки."""
    def __init__(self, x, y):
        super().__init__(x, y, 40, 40)
        self.id = "block"

    def move(self):
        pass


class Wall(Object):
    """Класс "Wall" описывает стены"""
    def __init__(self, x, y, w, h, vx, vy):
        super().__init__(x, y, w, h, vx, vy)
        self.id = "wall"


class Trap(Object):
    """Класс "Trap" описывает ловушки"""
    def __init__(self, x, y, w, h, vx, vy):
        super().__init__(x, y, w, h, vx, vy)
        self.id = "trap"


class Goal(Object):
    def __init__(self, x, y):
        super().__init__(x, y, 30, 45)
        self.id = "goal"

class Trampoline(Object):
    """ Класс "Trampoline" описывает батуты
    vx, vy -- скорость которая сообщается объекту при взаимодействии
    """
    def __init__(self, x, y, w, h, vx, vy):
        super().__init__(x, y, w, h, vx, vy)
        self.id = "trampoline"
        self.time = pygame.time.get_ticks()

    def move(self):
        pass

    def boost(self, object):
        if pygame.time.get_ticks() - self.time > 1000:
            object.vx += self.vx
            object.vy += self.vy
            self.time = pygame.time.get_ticks()

if __name__ == "__main__":
    print("This module is not for direct call!")
