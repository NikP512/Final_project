import pygame
from player import *
from objects import *
from level import *
import random
"""Управление:
В любом режиме
d -- удалить обЪект в точке где находиться курсор
shif + d -- удалить все
c -- выбрать объект для редактирования
для выбраного объекта стрелочками изменяется скорость в соответствующем направлении
при нажатом p стрелочками меняется позиция объекта
при нажатом t для ShootingTrap меняется cooldown
backspace -- обнулить скорость выбраного объекта
m -- отображение движения
w -- сохранить текущую версию в файл
l -- загрузить текущую версию из файла
1 -- режим добавленния блоков
4 -- режим добавления цели
q -- добавить объект в точке где находится курсор
3 -- режим добавления ловушек
5 -- режим добавления батутов
6 -- режим добавления стреляющих ловушек
s -- выбор начала объекта 
e -- выбор конца объекта и его создание
"""


class LocationEditor:
    """
    Класс описывающий редактор
    self.classes_dictionary -- список доступных объектов
    self.type -- текущий режим соответствующий ключу класса текущего объекта
    self.x, self.y -- текущие координаты курсора
    self.start_x, self.start_y, self.end_x, self.end_y -- координаты точек начала и конца чего-то
    self.block_w, self.block_h -- ширина и высота блоков
    self.file_name -- название редактируемого файла
    self.current_object -- редактируемый объект
    """
    def __init__(self, screen, layer):
        self.screen = screen
        self.layer = layer
        self.classes_dictionary = {30: Block, 32: Trap, 33: Goal, 34: Trampoline, 35: ShootingTrap}
        self.type = 30
        self.x = 0
        self.y = 0
        self.stage = 1
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.time = pygame.time.get_ticks()
        self.block_w = Block(0, 0).w
        self.block_h = Block(0, 0).h
        self.file_name = "levels/" + input()
        self.current_object = Trap(0, 0, 0, 0, 0, 0)
        self.current_object_surf = pygame.Surface((0, 0))

    def get_mouse_position(self):
        self.x, self.y = pygame.mouse.get_pos()

    def information(self):
        f = pygame.font.Font(None, 20)
        text = "Текущий файл " + str(self.file_name).split("/")[-1]
        text = f.render(text, 1, (90, 40, 250))
        self.screen.blit(text, (0, 20))
        text = "vx: " + str(round(self.current_object.vx, 1)) + " " + "vy: " + str(round(self.current_object.vy, 1))
        text = f.render(text, 1, (90, 40, 250))
        self.screen.blit(text, (0, 40))
        if self.current_object.id == "shooting_trap":
            text = "cooldown " + str(self.current_object.shot_cooldown)
            text = f.render(text, 1, (90, 40, 250))
            self.screen.blit(text, (0, 60))

    def save(self, events):
        for event in events:
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_w):
                self.write_objects_to_file()

    def load(self, events):
        for event in events:
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_l):
                self.layer.objects = []
                self.layer.set_object_from_file(self.file_name)

    def delete(self):
        """функция удаления
        """
        keys = pygame.key.get_pressed()
        for object in self.layer.objects:
            object_rect = pygame.Rect(object.x - object.w / 2, object.y - object.h / 2, object.w, object.h)
            if object_rect.collidepoint((self.x, self.y)) and keys[pygame.K_d]:
                self.layer.objects.pop(self.layer.objects.index(object))

    def delete_all(self):
        keys = pygame.key.get_pressed()
        if (pygame.KMOD_SHIFT & pygame.key.get_mods()) and keys[pygame.K_d]:
            self.layer.objects = []

    def motion_viewing(self, events):
        """
        при нажатии m запускает движение объектов
        при отжатии m возвращает объекты в состояние, которое было до начала движения
        """
        keys = pygame.key.get_pressed()
        for event in events:
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_m):
                self.write_objects_to_file()
            if (event.type == pygame.KEYUP) and (event.key == pygame.K_m):
                self.layer.objects = []
                self.layer.set_object_from_file(self.file_name)
        if keys[pygame.K_m]:
            self.layer.update()

    def add_block_like_object(self):
        """функция добавления блоков
        """
        keys = pygame.key.get_pressed()
        key = pygame.MOUSEBUTTONDOWN
        is_there_block = False
        for obj in self.layer.objects:
            rect = pygame.Rect(obj.x - obj.w / 2, obj.y - obj.h / 2, obj.w, obj.h)
            is_there_block += rect.collidepoint(self.x, self.y)
        if key == 1 or keys[pygame.K_q] and not is_there_block:
            self.layer.objects.append(self.classes_dictionary[self.type](self.x//self.block_w*self.block_w + self.block_w//2,
                                                                         self.y//self.block_h*self.block_h + self.block_h//2))

    def add_wall_like_object(self):
        """функция добавления стен
        при нажатии s -- создает один из углов стены,
        при нажатие e -- создает угол противоположный исходному и создает стену
        """
        keys = pygame.key.get_pressed()
        surf = pygame.Surface((abs(self.x - self.start_x), abs(self.y - self.start_y)))
        surf.fill((255, 255, 0))
        surf.set_alpha(100)
        self.screen.blit(surf, (min(self.start_x, self.x), min(self.start_y, self.y)))
        if (keys[pygame.K_s]) and (self.stage <= 1):
            self.start_x = self.x
            self.start_y = self.y
            self.stage = 1
        if (keys[pygame.K_e]) and (self.stage == 1) and (pygame.time.get_ticks() - self.time > 200):
            self.end_x = self.x
            self.end_y = self.y
            self.stage += 1
            self.time = pygame.time.get_ticks()
        if self.stage == 2:
            self.stage = 1
            self.layer.objects.append(self.classes_dictionary[self.type]((self.start_x + self.end_x)//2,
                                                                         (self.start_y+self.end_y)//2,
                                                                         abs(self.start_x-self.end_x),
                                                                         abs(self.start_y-self.end_y),
                                                                         0, 0))

    def choose_object(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            for obj in self.layer.objects:
                if obj.id in ["wall", "trap", "trampoline", "shooting_trap"]:
                    rect = pygame.Rect(obj.x - obj.w / 2, obj.y - obj.h / 2, obj.w, obj.h)
                    if rect.collidepoint(self.x, self.y):
                        self.current_object = obj
                        self.current_object_surf = pygame.Surface((obj.w, obj.h))
                        self.current_object_surf.fill((0, 255, 255))
                        self.current_object_surf.set_alpha(100)
                        break

    def change_current_object(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            self.current_object.vx = 0
            self.current_object.vy = 0
        if (self.current_object.id == "shooting_trap") and keys[pygame.K_t]:
            if keys[pygame.K_RIGHT]:
                self.current_object.shot_cooldown += 1
            if keys[pygame.K_LEFT]:
                self.current_object.shot_cooldown -= 1
        elif (pygame.time.get_ticks() - self.time > 500) and keys[pygame.K_p]:
            if keys[pygame.K_UP]:
                self.current_object.y -= 1
            if keys[pygame.K_RIGHT]:
                self.current_object.x += 1
            if keys[pygame.K_DOWN]:
                self.current_object.y += 1
            if keys[pygame.K_LEFT]:
                self.current_object.x -= 1
        else:
            if keys[pygame.K_UP]:
                self.current_object.vy -= 0.1
            if keys[pygame.K_RIGHT]:
                self.current_object.vx += 0.1
            if keys[pygame.K_DOWN]:
                self.current_object.vy += 0.1
            if keys[pygame.K_LEFT]:
                self.current_object.vx -= 0.1

    def write_objects_to_file(self):
        """
        """
        with (open(self.file_name, 'w') as out_file):
            for obj in self.layer.objects:
                s = obj.id
                if s in ["block", "goal"]:
                    s += " " + str(obj.x) + " " + str(obj.y) + "\n"
                elif s in ["wall", "trap", "trampoline"]:
                    s += " " + str(obj.x) + " " + str(obj.y) + " " + str(obj.w) + " " + str(obj.h) + " " + str(obj.vx) + " " + str(obj.vy) + "\n"
                elif s in ["shooting_trap"]:
                    s += (" " + str(obj.x) + " " + str(obj.y) + " " + str(obj.w) + " " + str(obj.h)
                         + " " + str(obj.vx) + " " + str(obj.vy) + " " + str(obj.shot_cooldown) + "\n")
                out_file.write(s)

    def choose_type(self):
        keys = pygame.key.get_pressed()
        if 1 in keys:
            if keys.index(1) in self.classes_dictionary.keys():
                self.type = keys.index(1)


HEIGHT = 800
WIDTH = 800
RUNNING = True
FPS = 60


def check_events(events):
    """Функция, обрабатывающая нажатие клавиш.
    Возвращает список всех нажатых клавиш.
    """
    global RUNNING

    for event in events:
        if event.type == pygame.QUIT:
            RUNNING = False


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    location = Location(screen)
    editor = LocationEditor(screen, location)
    location.set_object_from_file(editor.file_name)

    while RUNNING:
        screen.fill((255, 255, 255))
        events = pygame.event.get()
        check_events(events)
        location.draw()
        editor.screen.blit(editor.current_object_surf,
                           (editor.current_object.x - editor.current_object.w//2,
                            editor.current_object.y - editor.current_object.h//2))
        editor.information()
        editor.save(events)
        editor.load(events)
        editor.choose_type()
        editor.get_mouse_position()
        editor.delete()
        editor.delete_all()
        editor.choose_object()
        editor.change_current_object()
        editor.motion_viewing(events)
        if editor.type in [30, 33]:
            editor.add_block_like_object()
        if editor.type in [32, 34, 35]:
            editor.add_wall_like_object()
        clock.tick(FPS)
        pygame.display.update()

    editor.write_objects_to_file()
    pygame.quit()


main()
