import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

# Variable to set frame rate
clock = pygame.time.Clock()

def run_game():
    # Initialize game and create screen object.
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # Start the main loop for the game
    while True:
        clock.tick(60)
        gf.check_events(ship)
        ship.update()
        gf.update_screen(game_settings=game_settings, screen=screen, ship=ship)

run_game()