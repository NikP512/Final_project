from objects import Object
import pygame
pygame.font.init()


class Menu:
    def __init__(self, screen):
        self.screen = screen

        self.running = True
        self.finished = False

        self.choose_level = 0
        self.choose_player = 0

        self.background_image = pygame.image.load("pictures/background.png")
        self.button_image = pygame.image.load("pictures/button.png")
        self.font = pygame.font.Font("Font.otf", 30)

        self.icons = []
        self.buttons = []

    def start_menu(self, number):
        """number -- число уровней"""
        self.icons.append(Icon(300, 250, 1))
        self.icons.append(Icon(500, 250, 2))
        for n in range(1, number+1):
            self.buttons.append(Button(400 + (-1)**n*125, 275+100*((n + 1)//2), n, self.font))

    def update(self):
        """Отрисовка заднего фона и кнопок"""
        scale_image = pygame.transform.scale(self.background_image, (self.screen.get_width(), self.screen.get_height()))
        scale_rect = scale_image.get_rect(center=(self.screen.get_width()//2, self.screen.get_height()//2))
        self.screen.blit(scale_image, scale_rect)

        for button in self.buttons:
            scale_image = pygame.transform.scale(self.button_image, (button.w, button.h))
            scale_rect = scale_image.get_rect(center=(button.x, button.y))
            self.screen.blit(scale_image, scale_rect)
            self.screen.blit(button.text, button.text.get_rect(center=(button.x, button.y)))

        for icon in self.icons:
            scale_image = pygame.transform.scale(icon.image, (icon.w, icon.h))
            scale_rect = scale_image.get_rect(center=(icon.x, icon.y))
            self.screen.blit(scale_image, scale_rect)

            if icon.id == self.choose_player:
                pygame.draw.circle(self.screen, (255, 0, 0), (icon.x, icon.y), icon.w//2+5, 6)
            else:
                pygame.draw.circle(self.screen, (0, 0, 0), (icon.x, icon.y), icon.w//2+5, 6)

    def check_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
                self.finished = True
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                for icon in self.icons:
                    if (x - icon.x)**2 + (y - icon.y)**2 <= icon.w**2//4:
                        self.choose_player = icon.id

                for button in self.buttons:
                    button_rect = pygame.Rect(button.x - button.w//2, button.y - button.h//2, button.w, button.h)
                    if button_rect.collidepoint((x, y)):
                        if self.choose_player != 0:
                            self.choose_level = button.id
                            self.running = False
                            break


class Button(Object):
    def __init__(self, x, y, ident, font):
        """ident - номер уровня."""
        super().__init__(x, y, 150, 50)
        self.id = ident
        self.text = font.render("Level " + str(ident), False, (0, 0, 0))

    def move(self):
        pass


class Icon(Object):
    def __init__(self, x, y, ident):
        """"ident - номер персонажа"""
        super().__init__(x, y, 100, 100)
        self.id = ident
        self.image = pygame.image.load("pictures/icon"+str(ident)+".png")

    def move(self):
        pass


if __name__ == "__main__":
    print("This module is not for direct call!")
