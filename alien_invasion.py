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
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        #wait for event like keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() #drawing ship
        # make the recent screen visible
        pygame.display.flip()

    def _check_keydown_events(self, event):
        """checks keypresses events and manages them"""
        if event.key == pygame.K_RIGHT:
            #only change the flag to True
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q: #for quting faster :)
            sys.exit()

    def _check_keyup_events(self, event):
        """check key releases events and manages them"""
        if event.key == pygame.K_RIGHT:
            #set the flag to False
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            #set the flag to False
            self.ship.moving_left = False

if __name__ == "__main__":
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()