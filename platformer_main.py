import pygame


def main():
    pass


if __name__ == "__main__":

    pygame.init()

    HEIGHT = 800
    WIDTH = 800
    FPS = 60

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True

    while running:
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
