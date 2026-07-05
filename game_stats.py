class GameStats:
    """keep a record of Alien Invasion stats"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings

        self.high_score = 0

        self.reset_stats()

    def reset_stats(self):
        """initialize stats that can change during game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1