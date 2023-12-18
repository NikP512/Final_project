import pygame
from objects import *
import os.path


class Level:
    def __init__(self, screen, ident, player):
        self.screen = screen
        self.id = str(ident)
        self.running = True
        self.locations = dict()
        self.player = player
        self.player_location = None

    def start_level(self):
        self.player_location = self.locations[0].id

    def check_win(self):
        pass

    def update(self):
        self.locations[self.player_location].update()

    def check_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False


class Location:
    """Класс, описывающий слой уровня. Каждый слой имеет свой id и список объектов, на нем расположенных."""
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.images = {"block": pygame.image.load("pictures/block.png"),
                       "wall": pygame.image.load("pictures/wall.png"),
                       "trap": pygame.image.load("pictures/trap.png")}

    def update(self):
        for obj in self.objects:
            obj.move()
            image = self.images.get(obj.id, None)
            scale_image = pygame.transform.scale(image, (obj.w, obj.h))
            scale_rect = scale_image.get_rect(center=(obj.x, obj.y))
            self.screen.blit(scale_image, scale_rect)

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
