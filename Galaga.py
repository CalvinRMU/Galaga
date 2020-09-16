# Imports
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

#Functions
def run_game():
    #init game, screen, and settings
    pygame.init()
    game_settings= Settings()

    #draw the screen
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Galaga")

    #make ship
    ship =Ship(game_settings, screen)

    #make a group for bullets
    bullets = Group()

    #main game loop
    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(game_settings, screen, ship, bullets)



#***Start Game***#
run_game()
# TODO: Page 256
