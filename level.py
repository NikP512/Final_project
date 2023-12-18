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

    def update(self, keys):
        self.player.move(keys)
        self.player.jump(keys)

        for obj in self.locations[self.player_location].objects:
            obj.move()

            if obj.id == "trap" and check_contact(obj, self.player):
                pass

            if obj.id == "goal" and check_contact(obj, self.player):
                pass

    def draw(self):
        self.locations[self.player_location].draw()
        self.player.draw()

    def check_events(self, events, keys):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

        self.update(keys)


class Location:
    """Класс, описывающий слой уровня. Каждый слой имеет свой id и список объектов, на нем расположенных."""
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.images = {"block": pygame.image.load("pictures/block.png"),
                       "wall": pygame.image.load("pictures/wall.png"),
                       "trap": pygame.image.load("pictures/trap.png")}
        self.object_type_dictionary = {"block": Block, "wall": Wall, "trap": Trap}

    def draw(self):
        for obj in self.objects:
            image = self.images.get(obj.id, None)
            scale_image = pygame.transform.scale(image, (obj.w, obj.h))
            scale_rect = scale_image.get_rect(center=(obj.x, obj.y))
            self.screen.blit(scale_image, scale_rect)

    def update(self):
        for obj in self.objects:
            obj.move()

    def set_object_from_file(self, file_name):
        if os.path.exists(file_name):
            with open(file_name) as input_file:
                for line in input_file:
                    if len(line.strip()) == 0 or line[0] == '#':
                        continue  # пустые строки и строки-комментарии пропускаем
                    obj_id = line.split()[0].lower()

                    if obj_id == "block":
                        x, y = line.split()[1:]
                        self.objects.append(Block(int(x), int(y)))

                    if obj_id in ["wall", "trap"]:
                        x, y, w, h, vx, vy = line.split()[1:]
                        self.objects.append(
                            self.object_type_dictionary[obj_id](round(float(x), 0), round(float(y), 0),
                                                                int(w), int(h), float(vx), float(vy)))

                    if obj_id == "goal":
                        x, y = line.split()[1:]
                        self.objects.append(Goal(int(x), int(y)))


def check_contact(obj1, obj2):
    rect1 = pygame.Rect(obj1.x - obj1.w//2, obj1.y - obj1.h//2, obj1.w, obj1.h)
    rect2 = pygame.Rect(obj2.x - obj2.w // 2, obj2.y - obj2.h // 2, obj2.w, obj2.h)
    return rect1.colliderect(rect2)


if __name__ == "__main__":
    print("This module is not for direct call!")
