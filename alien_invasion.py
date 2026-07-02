import sys
import pygame 

class AlienInvasion:
    """Overall clas of the game"""
    def __init__(self):
        """initialize the game window and its resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #wait for event like keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # make the recent screen visible
            pygame.display.flip()

if __name__ == "__main__":
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()