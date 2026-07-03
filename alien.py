import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """Manages everything about one Alien"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        #laoding image and geting its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #put it near topleft
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    def check_edges(self):
        """return True when alien is at edge"""
        return (self.rect.right > self.screen_rect.right or self.rect.left <= 0)
        
    def update(self):
        """move aliens to the right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x