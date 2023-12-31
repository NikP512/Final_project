import pygame
import random
from player import *
from menu import *
from level import *
import os.path


def main():
    fps = 60
    width = 800
    height = 800

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    menu = Menu(screen)

    while not menu.finished:
        menu.start_menu(5)
        while menu.running:
            menu.update()
            pygame.display.update()
            menu.check_events(pygame.event.get())

            clock.tick(fps)

        if menu.finished:
            return

        player = Player(screen, menu.choose_player)
        level = Level(screen, menu.choose_level, player)
        file_name = "levels/" + level.id + "."

        n = 1
        while os.path.exists(file_name + str(n)):
            level.locations.append(Location(screen))
            level.locations[-1].set_object_from_file(file_name + str(n))
            n += 1
        level.start_level()

        while level.running:
            level.draw(random.choice([(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255),
                                      (255, 255, 0), (255, 0, 255), (0, 255, 255)]))
            pygame.display.update()
            level.update(pygame.key.get_pressed())
            level.check_events(pygame.event.get(), pygame.key.get_pressed())

            clock.tick(fps)


pygame.quit()


if __name__ == "__main__":
    main()
