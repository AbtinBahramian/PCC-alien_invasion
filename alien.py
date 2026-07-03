import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """Manages everything about one Alien"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #laoding image and geting its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #put it near topleft
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
