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
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.w, self.h))


class Block:
    """Класс "Block" описывает блоки"""
    def __init__(self, screen, x, y):
        self.id = "block"
        self.screen = screen
        self.x = x
        self.y = y
        self.w = 20
        self.h = 20

    def draw(self, file_name):
        """Отрисовка блоков
        file_name -- название файла, содержащего изображение стены"""
        image = pygame.image.load(file_name)
        scale_image = pygame.transform.scale(image, (self.w, self.h))
        scale_rect = scale_image.get_rect(center=(self.x, self.y))
        self.screen.blit(scale_image, scale_rect)


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

    def draw(self):
        """Отрисовка стены
        file_name -- название файла, содержащего изображение стены"""
        image = pygame.image.load(self.file_name)
        scale_image = pygame.transform.scale(image, (self.w, self.h))
        scale_rect = scale_image.get_rect(center=(self.x, self.y))
        self.screen.blit(scale_image, scale_rect)


class Trap:
    """Класс "Trap" описывает ловушки"""
    def __init__(self, screen, x, y, w, h):
        self.id = "trap"
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, file_name):
        """Отрисовка ловушек
        file_name -- название файла, содержащего изображение ловушки"""
        image = pygame.image.load(file_name)
        scale_image = pygame.transform.scale(image, (self.w, self.h))
        scale_rect = scale_image.get_rect(center=(self.x, self.y))
        self.screen.blit(scale_image, scale_rect)


if __name__ == "__main__":
    print("This module is not for direct call!")
