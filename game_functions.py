import sys
import pygame

def check_events(ship):
    #respond to keypresses and mouse movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

def update_screen(game_settings, screen, ship):
    #Update the screen

    #redraw the screen
    screen.fill(game_settings.bg_color)
    ship.blitme()

    #make the drawn screen visible
    pygame.display.flip()
