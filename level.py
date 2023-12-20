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
        self.player_location = None

    def start_level(self):
        self.player_location = 0
        self.player.x = 20
        self.player.y = 600
        self.player.vx = 0
        self.player.vy = 0

    def update(self, keys):
        for location in self.locations:
            location.update()

        for obj in self.locations[self.player_location].objects:

            if obj.id == "trap":
                if check_contact(obj, self.player):
                    self.start_level()
            elif obj.id == "goal":
                if check_contact(obj, self.player):
                    self.running = False
            elif obj.id == "trampoline":
                if check_contact(obj, self.player):
                    obj.boost(self.player)
            else:
                self.player.check_space(obj)

        if self.player.y > self.screen.get_height() + 200:
            self.start_level()

        self.player.jump(keys)
        self.player.move(keys)
        self.player.place_up = True
        self.player.place_right = True
        self.player.place_down = True
        self.player.place_left = True

    def change_location(self):
        for obj in self.locations[(self.player_location+1) % len(self.locations)].objects:
            if self.player.check_change_location_space(obj):
                return

        self.player_location = (self.player_location+1) % len(self.locations)

    def draw(self):
        self.locations[self.player_location].draw()
        self.player.draw()

    def check_events(self, events, keys):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
                self.change_location()

        self.update(keys)


class Location:
    """Класс, описывающий слой уровня. Каждый слой имеет свой id и список объектов, на нем расположенных."""
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.images = {"block": pygame.image.load("pictures/block.png"),
                       "wall": pygame.image.load("pictures/wall.png"),
                       "trap": pygame.image.load("pictures/trap.png"),
                       "goal": pygame.image.load("pictures/goal.gif"),
                       "trampoline": pygame.image.load("pictures/trampoline.png"),
                       "shooting_trap": pygame.image.load("pictures/trap.png")}
        self.background_image = pygame.image.load("pictures/background.png")
        self.object_type_dictionary = {"block": Block, "wall": Wall, "trap": Trap, "goal": Goal,
                                       "trampoline": Trampoline, "shooting_trap": ShootingTrap}

    def draw(self):
        scale_image = pygame.transform.scale(self.background_image, (self.screen.get_width(), self.screen.get_height()))
        scale_rect = scale_image.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(scale_image, scale_rect)
        for obj in self.objects:
            image = self.images.get(obj.id, None)
            scale_image = pygame.transform.scale(image, (obj.w, obj.h))
            scale_rect = scale_image.get_rect(center=(obj.x, obj.y))
            self.screen.blit(scale_image, scale_rect)

    def update(self):
        for obj in self.objects:
            obj.move()
            obj.rubbish_delete(self)
            if obj.id == "shooting_trap":
                obj.shot(self)

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

                    if obj_id in ["wall", "trap", "trampoline"]:
                        x, y, w, h, vx, vy = line.split()[1:]
                        self.objects.append(
                            self.object_type_dictionary[obj_id](round(float(x), 0), round(float(y), 0),
                                                                int(w), int(h), float(vx), float(vy)))

                    if obj_id == "goal":
                        x, y = line.split()[1:]
                        self.objects.append(Goal(int(x), int(y)))

                    if obj_id == "shooting_trap":
                        x, y, w, h, vx, vy, cooldown = line.split()[1:]
                        self.objects.append(
                            self.object_type_dictionary[obj_id](round(float(x), 0), round(float(y), 0), int(w), int(h),
                                                                float(vx), float(vy), round(float(cooldown), 0)))


def check_contact(obj1, obj2):
    rect1 = pygame.Rect(obj1.x - obj1.w//2, obj1.y - obj1.h//2, obj1.w, obj1.h)
    rect2 = pygame.Rect(obj2.x - obj2.w // 2, obj2.y - obj2.h // 2, obj2.w, obj2.h)
    return rect1.colliderect(rect2)


if __name__ == "__main__":
    print("This module is not for direct call!")
