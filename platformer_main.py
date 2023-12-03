import pygame
from platformer_player import *
from platformer_objects import *
from platformer_layer import *
HEIGHT = 800
WIDTH = 800
RUNNING = True
FPS = 60


def check_events():
    """Функция, обрабатывающая нажатие клавиш.
    Возвращает список всех нажатых клавиш.
    """
    global RUNNING

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    keys = pygame.key.get_pressed()

    return keys


def update_player(player, keys):
    """Функция, вызывающая поведение игрока. На вход подается объект класса Player и список нажатых клавиш."""
    player.get_info_about_space([True, True, True, True])
    player.move(keys)
    player.jump(keys)
    player.draw("image_player.jpg")


def update_layer(layer):
    """Функция, обновляющая слой. На вход подается объект класса ScreenLayer."""
    pass


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    player = Player(screen)
    layer = ScreenLayer()

    while RUNNING:
        screen.fill((255, 255, 255))
        keys = check_events()
        update_player(player, keys)
        update_layer(layer)
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
