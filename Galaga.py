# %%
import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #init game, screen, and settings
    pygame.init()
    game_settings= Settings()

    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Galaga")
    ship =Ship(screen)

    #main game loop
    while True:
        gf.check_events()
        gf.update_screen(game_settings, screen, ship)

run_game()


# TODO: Page 249
