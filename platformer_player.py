import pygame


class Player:
    """Класс описывающий игрока
    layer_id -- идентификатор слоя, на котором в данный момент находится игрок
    screen -- pygame.Surface на которой отображается игрок
    x, y, vx, vy -- координаты и скорости
    w, h -- высота и ширина игрока
    self.place_up, self.place_right, self.place_down, self.place_left -- атрибуты описывающие есть ли
    с соответствующей стороны от игрока свободное место, True -- есть, False -- нет
    self.jump_time -- время последнего прыжка
    """
    def __init__(self, screen, layer_id):
        self.layer_id = layer_id
        self.screen = screen
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.w = 20
        self.h = 40
        self.place_up = False
        self.place_right = False
        self.place_down = False
        self.place_left = False
        self.jump_time = pygame.time.get_ticks() - 1000

    def get_info_about_space(self, info):
        """Метод для получения self.place_up и так далее
        info -- список из четырех элемнтов с соответствующими данными"""
        self.place_up, self.place_right, self.place_down, self.place_left = info

    def move(self, keys):
        """Описывает движение игрока и остановку при столкновении
        ось для vy направлена вверх
        keys -- список зажатых клавиш"""
        g = 1
        if self.place_down:
            self.vy -= g
            self.y -= self.vy
        elif not self.place_up and (self.vy < 0):
            self.vy = 0

        if self.place_up:
            self.y -= self.vy
        elif not self.place_up and (self.vy > 0):
            self.vy = 0

        if self.place_right:
            self.x += self.vx
            if keys[pygame.K_RIGHT]:
                self.vx += 0.2
        elif not self.place_left and (self.vx > 0):
            self.vx = 0

        if self.place_left:
            self.x += self.vx
            if keys[pygame.K_LEFT]:
                self.vx -= 0.2
        elif not self.place_left and (self.vx < 0):
            self.vx = 0

    def jump(self, keys):
        """Метод прыжка
        использует разгон в течении какого-то времени для более плавной анимации
        keys -- список зажатых клавиш
        """
        if (pygame.time.get_ticks() - self.jump_time) < 100 and self.place_up:
            self.vy += 2
        if (pygame.time.get_ticks() - self.jump_time) > 1000 and self.place_down and keys[pygame.K_SPACE]:
            self.jump_time = pygame.time.get_ticks()
        if not self.place_up and (self.vy > 0):
            self.jump_time -= 100

    def draw(self, file_name):
        """Отрисовка игрока
        file_name -- название файла содержащего изображение игрока"""
        image = pygame.image.load(file_name)
        scale_image = pygame.transform.scale(image, (self.w, self.h))
        scale_rect = scale_image.get_rect(center=(self.x, self.y))
        self.screen.blit(scale_image, scale_rect)


if __name__ == "__main__":
    print("This module is not for direct call!")
