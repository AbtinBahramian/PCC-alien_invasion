import pygame
from settings import Settings

class Ship:
    """Everything about the ship"""
    def __init__(self, ai_game):

        self.settings = Settings()
        # initialzing the ship and its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #start at the bottm mid
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x) # a float for ship x 

        #creat a flag for moving right and left
        self.moving_right = False
        self.moving_left = False

        

    def blitme(self):
        """Draw ship at the mid bottom of screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """moves right if the flage is true"""
        #check for lef and right boundaries as well
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x