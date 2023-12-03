import pygame

class ScreenLayer:
    pass

def check_space(main_object, objects):
    """функция для проверки есть ли свободное место с каждой стороны от объекта,
     только для объектов с прямоугольным хитбоксом
    main_object -- объект для которого провереяется наличее свободного места,
    objects -- список объектов пересечение с которыми проверяется
    возвращает список булевых значений описывающие есть ли
    с соответствующей стороны от игрока свободное место True -- есть, False -- нет
    порядок в списке: вверх, право, низ, лево
     """
    rect_up = (main_object.x - main_object.w / 2, main_object.y + main_object.h / 2 + 1, main_object.w, 1)
    rect_right = (main_object.x + main_object.w / 2 + 1, main_object.y + main_object.h / 2, 1, main_object.h)
    rect_down = (main_object.x - main_object.w / 2, main_object.y - main_object.h / 2 - 1, main_object.w, 1)
    rect_left = (main_object.x - main_object.w / 2 - 1, main_object.y + main_object.h / 2, 1, main_object.h)
    free_spaces = [False, False, False, False]

    for object in objects:
        rect_object = (object.x - object.w / 2, object.y + object.h / 2 + 1, object.w, 1)
        for rect, n in zip([rect_up, rect_right, rect_down, rect_left], range(0, 4)):
            free_spaces[n] + rect.colliderect(rect_object)
    for n in range(0, 4):
        free_spaces[n] = not free_spaces[n]

    return free_spaces

if __name__ == "__main__":
    print("This module is not for direct call!")
