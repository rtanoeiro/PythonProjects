from re import L
from turtle import screensize
import pygame

class Ship():
    """Characteristics of the ship"""

    def __init__(self, screen) -> None:
        """Initialize the ship and start it's position"""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('Alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx =  self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom - self.rect.bottom/2  ## Self.rect.bottom/2 will adjust the image up just a bit, so it's entirely in the screen

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the ship's position based on movement flag"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1

    def blitme(self):
        """Draw the ship at it's current location"""

        self.screen.blit(self.image, self.rect)