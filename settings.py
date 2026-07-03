class Settings:
    """Class for all settings in our game Alien Invasion"""

    def __init__(self):
        # Screen Values
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed = 3.5

        #bullet settings
        self.bullet_speed = 4.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)