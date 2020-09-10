# %%
import sys
import pygame

from settings import Settings

def run_game():
    #init game, screen, and settings
    pygame.init()
    game_settings= Settings()

    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Galaga")
    bg_color = (230, 230, 230)

    #main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(game_settings.bg_color)
        pygame.display.flip()

run_game()
