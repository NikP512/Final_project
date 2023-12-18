import pygame
from objects import *
import os.path


class Level:
    def __init__(self, screen, ident, player):
        self.screen = screen
        self.id = str(ident)
        self.running = True
        self.locations = []
        self.player = player

    def check_win(self):
        pass

    def update(self):
        pass

    def check_events(self):
        pass

    def check_space(self):
        pass


class Location:
    """Класс, описывающий слой уровня. Каждый слой имеет свой id и список объектов, на нем расположенных."""
    def __init__(self, screen, ident):
        self.screen = screen
        self.id = str(ident)
        self.objects = []
        self.images = {"block": pygame.image.load("pictures/block.png"),
                       "wall": pygame.image.load("pictures/wall.png"),
                       "trap": pygame.image.load("pictures/trap.png")}

    def update(self):
        for obj in self.objects:
            """Отрисовка слоя"""
            image = self.images.get(obj.id, None)
            scale_image = pygame.transform.scale(image, (obj.w, obj.h))
            scale_rect = scale_image.get_rect(center=(obj.x, obj.y))
            obj.screen.blit(scale_image, scale_rect)

    def set_object_from_file(self, file_name):
        if os.path.exists("levels/"+file_name):
            with open("levels/"+file_name) as input_file:
                for line in input_file:
                    if len(line.strip()) == 0 or line[0] == '#':
                        continue  # пустые строки и строки-комментарии пропускаем
                    obj_id = line.split()[0].lower()

                    if obj_id == "block":
                        x, y = line.split()[1:]
                        self.objects.append(Block(self.screen, int(x), int(y)))

                    if obj_id in ["wall", "trap"]:
                        x, y, w, h, vx, vy = line.split()[1:]
                        self.objects.append(Wall(self.screen, int(x), int(y), int(w), int(h), float(vx), float(vy)))


if __name__ == "__main__":
    print("This module is not for direct call!")
