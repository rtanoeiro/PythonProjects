from sys import exit
import pygame

def check_events(ship):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        ## Recording when a key is pressed
        elif event.type == pygame.KEYDOWN: # Key pressed
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                # Move the ship to the right
                ship.moving_left = True
            if event.key == pygame.K_UP:
                # Move the ship to the right
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                # Move the ship to the right
                ship.moving_down = True    
        
        # Recording when a key is released
        elif event.type == pygame.KEYUP: # Key released
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                # Move the ship to the right
                ship.moving_left = False
            if event.key == pygame.K_UP:
                # Move the ship to the right
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                # Move the ship to the right
                ship.moving_down = False

def update_screen(game_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""

    # Redraw the screen\
    screen.fill(game_settings.bg_color)
    ship.blitme()

    # Make the most recently draw screen visible
    pygame.display.flip()