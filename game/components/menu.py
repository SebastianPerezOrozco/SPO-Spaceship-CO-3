import pygame
from game.utils.constants import FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

    def __init__(self, message, text_size = 30):

        self.font = pygame.font.Font(FONT_STYLE, text_size)
        self.icon = pygame.transform.scale(ICON, (120, 80))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
        self.update_message(message)
        self.max_score_value = 0
        self.max_score_message = self.font.render("", True, (0, 0, 0))
        self.max_score_message_rect = self.max_score_message.get_rect()

    def event(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type == pygame.KEYDOWN:
                on_start()



    def draw (self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.icon, self.icon_rect)
        screen.blit(self.max_score_message, self.max_score_message_rect )
        pygame.display.update()
    
    def update_max_score_value(self, max_score):
        if max_score > self.max_score_value:
            self.max_score_value = max_score

        self.max_score_message = self.font.render(f"The highest score is: {self.max_score_value} points", True, (0, 0, 0))
        self.max_score_message_rect = self.max_score_message.get_rect()
        self.max_score_message_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)
        
        

    def update_message(self, message):
        self.message = message
        self.text = self.font.render(self.message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center= (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    
