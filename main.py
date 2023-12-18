import pygame
from player import *
from menu import *
from level import *


def main():
    fps = 60
    width = 800
    height = 800

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    menu = Menu(screen)

    while menu.running:
        menu.update()
        pygame.display.update()
        menu.check_events(pygame.event.get())

        clock.tick(fps)

    player = Player(screen, menu.choose_player)
    level = Level(screen, menu.choose_level, player)

    while level.running:
        pass

    pygame.quit()


if __name__ == "__main__":
    main()
