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
    def __init__(self, screen, number):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.w = 40
        self.h = 60
        self.place_up = True
        self.place_right = True
        self.place_down = True
        self.place_left = True
        self.jump_time = pygame.time.get_ticks() - 1000
        self.image = pygame.image.load("pictures/player" + str(number) + ".png")

    def check_space(self, obj):
        rects = [pygame.Rect(self.x - self.w//2+5, self.y - self.h//2, self.w-10, 1),
                 pygame.Rect(self.x + self.w//2, self.y - self.h//2+5, 1, self.h-10),
                 pygame.Rect(self.x - self.w//2+5, self.y + self.h//2, self.w-10, 1),
                 pygame.Rect(self.x - self.w//2, self.y - self.h//2+5, 1, self.h-10)]
        rect = pygame.Rect(obj.x - obj.w//2, obj.y - obj.h//2, obj.w, obj.h)

        self.place_up = self.place_up and not rect.colliderect(rects[0])
        self.place_right = self.place_right and not rect.colliderect(rects[1])
        self.place_down = self.place_down and not rect.colliderect(rects[2])
        self.place_left = self.place_left and not rect.colliderect(rects[3])

    def move(self, keys):
        """Описывает движение игрока и остановку при столкновении
        ось для vy направлена вверх
        keys -- список зажатых клавиш"""
        g = 0.05
        if not self.place_down and (self.vy < 0):
            self.vy = 0
        if self.place_down:
            self.vy -= g
            self.y -= self.vy

        if not self.place_up and (self.vy > 0):
            self.vy = 0
        if self.place_up and (self.vy >= 0):
            self.y -= self.vy

        if (not self.place_right) and (self.vx > 0):
            self.vx = 0
        if self.place_right:
            self.x += self.vx
            if keys[pygame.K_RIGHT] and (self.vx < 1):
                self.vx += 0.1

        if (not self.place_left) and (self.vx < 0):
            self.vx = 0
        if self.place_left:
            self.x += self.vx
            if keys[pygame.K_LEFT] and (self.vx > -1):
                self.vx -= 0.1

        if (not self.place_down) and (self.vx < 0):
            self.vx += 0.01
        elif (not self.place_down) and (self.vx > 0):
            self.vx -= 0.01

        if abs(self.vx) < 0.02:
            self.vx = 0

    def jump(self, keys):
        """Метод прыжка
        использует разгон в течении какого-то времени для более плавной анимации
        keys -- список зажатых клавиш
        """
        if (pygame.time.get_ticks() - self.jump_time) > 100 and not self.place_down and keys[pygame.K_SPACE]:
            self.jump_time = pygame.time.get_ticks()
            self.vy = 3
        if not self.place_up and (self.vy > 0):
            self.jump_time -= 100

    def draw(self):
        """Отрисовка игрока
        file_name -- название файла содержащего изображение игрока"""
        scale_image = pygame.transform.scale(self.image, (self.w, self.h))
        scale_rect = scale_image.get_rect(center=(self.x, self.y))
        self.screen.blit(scale_image, scale_rect)


if __name__ == "__main__":
    print("This module is not for direct call!")
