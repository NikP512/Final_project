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


def update_player(player, keys, info):
    """Функция, вызывающая поведение игрока. На вход подается объект класса Player и список нажатых клавиш."""
    player.get_info_about_space(info)
    player.move(keys)
    player.jump(keys)
    player.draw()


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    layers = list()
    layers.append(ScreenLayer(screen, 1, []))
    layers.append(ScreenLayer(screen, 2, []))
    player = Player(screen, layers[0].id)
    player.get_coordinates(300, 600)
    layers[0].objects.append(Wall(screen, 400, 700, 800, 100))
    layers[0].set_object_from_file("1.1")
    info = [True, True, True, True]

    while RUNNING:
        screen.fill((255, 255, 255))
        keys = check_events()
        for layer in layers:
            if layer.id == player.layer_id:
                info = check_space(player, layer.objects)
                layer.update()
                break
        update_player(player, keys, info)
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
