from objects import *


class Level:
    def __init__(self, screen, ident, player):
        self.screen = screen
        self.id = str(ident)
        self.locations = []
        self.player = player

    def check_win(self):
        pass


class Location:
    """Класс, описывающий слой уровня. Каждый слой имеет свой id и список объектов, на нем расположенных."""
    def __init__(self, screen, ident):
        self.screen = screen
        self.id = str(ident)
        self.objects = []
        self.object_classes = {"block": Block}
        self.image_block = pygame.image.load("pictures/block.png")
        self.image_wall = pygame.image.load("pictures/wall.png")
        self.image_trap = pygame.image.load("pictures/trap.png")

    def update(self):
        for obj in self.objects:
            """Отрисовка слоя"""
            if obj.id == "wall":
                scale_image = pygame.transform.scale(self.image_wall, (obj.w, obj.h))
                scale_rect = scale_image.get_rect(center=(obj.x, obj.y))
                obj.screen.blit(scale_image, scale_rect)
            if obj.id == "block":
                scale_image = pygame.transform.scale(self.image_block, (obj.w, obj.h))
                scale_rect = scale_image.get_rect(center=(obj.x, obj.y))
                obj.screen.blit(scale_image, scale_rect)
            if obj.id == "trap":
                scale_image = pygame.transform.scale(self.image_trap, (obj.w, obj.h))
                scale_rect = scale_image.get_rect(center=(obj.x, obj.y))
                obj.screen.blit(scale_image, scale_rect)

    def set_object_from_file(self, file_name):
        with open(file_name) as input_file:
            for line in input_file:
                if len(line.strip()) == 0 or line[0] == '#':
                    continue  # пустые строки и строки-комментарии пропускаем
                obj_id = line.split()[0].lower()

                if obj_id == "block":
                    x, y = line.split()[1:]
                    self.objects.append(Block(self.screen, int(x), int(y)))

                if obj_id == "wall":
                    x, y, w, h = line.split()[1:]
                    self.objects.append(Wall(self.screen, int(x), int(y), int(w), int(h)))

                if obj_id == "trap":
                    x, y, w, h = line.split()[1:]
                    self.objects.append(Trap(self.screen, int(x), int(y), int(w), int(h)))


if __name__ == "__main__":
    print("This module is not for direct call!")