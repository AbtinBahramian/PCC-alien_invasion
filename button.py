import pygame.font

class Button:
    """Creating a button"""
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #set dimensions and attributes of button
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_colot = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #build button rect and center it
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center

        #button message
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """turn message to a rendered image and put on button"""
        self.msg_image = self.font.render(msg, True, self.text_colot, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)