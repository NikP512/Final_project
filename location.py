import pygame
from objects import *



class Location:
    """Класс, описывающий слой уровня. Каждый слой имеет свой id и список объектов, на нем расположенных."""
    def __init__(self, screen, ident):
        self.screen = screen
        self.id = str(ident)
        self.objects = []
        self.object_classes = {"block": Block}

    def update(self):
        for obj in self.objects:
            """Отрисовка слоя
            file_name -- название файла, содержащего изображение слоя"""
            image = pygame.image.load(obj.file_name)
            scale_image = pygame.transform.scale(image, (obj.w, obj.h))
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


def check_space(main_object, objects, screen, hitbox_on):
    """функция для проверки есть ли свободное место с каждой стороны от объекта,
     только для объектов с прямоугольным хитбоксом
    main_object -- объект для которого провереяется наличее свободного места,
    objects -- список объектов пересечение с которыми проверяется
    возвращает список булевых значений описывающие есть ли
    с соответствующей стороны от игрока свободное место True -- есть, False -- нет
    порядок в списке: вверх, право, низ, лево
    hitbox_on -- булева переменая которая определяет отрисовывается ли хитбокс
     """
    rect_up = pygame.Rect(main_object.x - main_object.w / 2.4,
                          main_object.y - main_object.h / 2 - 2 - main_object.vy, main_object.w/1.2, 6)
    rect_right = pygame.Rect(main_object.x + main_object.w / 2,
                             main_object.y - main_object.h / 2.2 + main_object.vx, 2, main_object.h/1.1)
    rect_down = pygame.Rect(main_object.x - main_object.w / 2.4,
                            main_object.y + main_object.h / 2 - 6 - main_object.vy, main_object.w/1.2, 6)
    rect_left = pygame.Rect(main_object.x - main_object.w / 2 - 2,
                            main_object.y - main_object.h / 2.2 - main_object.vx, 2, main_object.h/1.1)
    free_spaces = [False, False, False, False]

    for obj in objects:
        rect_object = pygame.Rect(obj.x - obj.w / 2, obj.y - obj.h / 2, obj.w, obj.h)
        for rect, n in zip([rect_up, rect_right, rect_down, rect_left], range(0, 4)):
            if hitbox_on:
                pygame.draw.rect(screen, (255, 0, 0), rect)
            free_spaces[n] += rect.colliderect(rect_object)
    for n in range(0, 4):
        free_spaces[n] = not free_spaces[n]

    return free_spaces


if __name__ == "__main__":
    print("This module is not for direct call!")
