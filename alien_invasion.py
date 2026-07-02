import sys
import pygame 
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall clas of the game"""
    def __init__(self):
        """initialize the game window and its resources"""
        pygame.init()
        self.settings = Settings() # creating an instance of Settings to use its attributes
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) #creating ship and sending self


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #wait for event like keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            # make the recent screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()