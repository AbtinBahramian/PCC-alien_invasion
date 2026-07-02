import pygame

class Ship:
    """Everything about the ship"""
    def __init__(self, ai_game):
        # initialzing the ship and its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #start at the bottm mid
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship at the mid bottom of screen"""
        self.screen.blit(self.image, self.rect)