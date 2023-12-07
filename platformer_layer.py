import pygame
from platformer_objects import *

class ScreenLayer:
    """Класс, описывающий слой уровня. Каждый слой имеет свой id и список объектов, на нем расположенных."""
    def __init__(self, screen, id, objects):
        self.screen = screen
        self.id = str(id)
        self.objects = objects
        self.object_classes = {"block": Block}

    def update(self):
        for object in self.objects:
            """Отрисовка слоя
            file_name -- название файла, содержащего изображение слоя"""
            image = pygame.image.load(object.file_name)
            scale_image = pygame.transform.scale(image, (object.w, object.h))
            scale_rect = scale_image.get_rect(center=(object.x, object.y))
            object.screen.blit(scale_image, scale_rect)

    def set_object_from_file(self, file_name):
        with open(file_name) as input_file:
            for line in input_file:
                if len(line.strip()) == 0 or line[0] == '#':
                    continue  # пустые строки и строки-комментарии пропускаем
                object_id = line.split()[0].lower()
                if object_id == "block":
                    x, y = line.split()[1:]
                    self.objects.append(Block(self.screen, int(x), int(y)))


def check_space(main_object, objects):
    """функция для проверки есть ли свободное место с каждой стороны от объекта,
     только для объектов с прямоугольным хитбоксом
    main_object -- объект для которого провереяется наличее свободного места,
    objects -- список объектов пересечение с которыми проверяется
    возвращает список булевых значений описывающие есть ли
    с соответствующей стороны от игрока свободное место True -- есть, False -- нет
    порядок в списке: вверх, право, низ, лево
     """
    rect_up = pygame.Rect(main_object.x - main_object.w / 3, main_object.y - main_object.h / 2 - 1, main_object.w/1.5, 2)
    rect_right = pygame.Rect(main_object.x + main_object.w / 2 + 1, main_object.y - main_object.h / 2.4, 2, main_object.h/1.2)
    rect_down = pygame.Rect(main_object.x - main_object.w / 3, main_object.y + main_object.h / 2 + 1, main_object.w/1.5, 2)
    rect_left = pygame.Rect(main_object.x - main_object.w / 2 - 1, main_object.y - main_object.h / 2.4, 2, main_object.h/1.2)
    free_spaces = [False, False, False, False]

    for object in objects:
        rect_object = pygame.Rect(object.x - object.w / 2, object.y - object.h / 2, object.w, object.h)
        for rect, n in zip([rect_up, rect_right, rect_down, rect_left], range(0, 4)):
            free_spaces[n] += rect.colliderect(rect_object)
    for n in range(0, 4):
        free_spaces[n] = not free_spaces[n]

    return free_spaces


if __name__ == "__main__":
    print("This module is not for direct call!")
