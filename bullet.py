import pygame
from pygame.sprite import sprite

class Bullet(Sprite):
    #manage bullets fired from the ship

    def __init__(self, game_settings, screen, ship):
        super().__init__()
        self.screen = screen

        #create bullet rect
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)

        #bullet starts at the top center of ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y =float(self.rect.y)
        self.color - game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        #move bullets up the screen
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet():
        pygame.draw.rect(self.screen, self.color, self.rect)
