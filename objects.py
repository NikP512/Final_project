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

    def rubbish_delete(self, location):
        w = location.screen.get_width()
        h = location.screen.get_height()
        if (self.x < -w) or (self.x > 2*w) or (self.y < - h) or (self.y > 2*h):
            location.objects.pop(location.objects.index(self))


class Block(Object):
    """Класс "Block" описывает блоки."""
    def __init__(self, x, y):
        super().__init__(x, y, 40, 40)
        self.id = "block"

    def move(self):
        pass


class Trap(Object):
    """Класс "Trap" описывает ловушки"""
    def __init__(self, x, y, w, h, vx, vy):
        super().__init__(x, y, w, h, vx, vy)
        self.id = "trap"


class Goal(Object):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 56)
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


class ShootingTrap(Object):
    """ Класс "ShootingTrap" описывает стреляющие ловушки
    vx, vy -- скорость снарядов запускаемых ловушкой
    """
    def __init__(self, x, y, w, h, vx, vy, shoot_cooldown=100):
        super().__init__(x, y, w, h, vx, vy)
        self.id = "shooting_trap"
        self.time = pygame.time.get_ticks()
        self.shot_cooldown = shoot_cooldown

    def move(self):
        pass

    def shot(self, location):
        if (pygame.time.get_ticks() - self.time) > self.shot_cooldown:
            self.time = pygame.time.get_ticks()
            location.objects.append(Trap(self.x, self.y, self.w//4, self.h//4, self.vx, self.vy))


if __name__ == "__main__":
    print("This module is not for direct call!")
