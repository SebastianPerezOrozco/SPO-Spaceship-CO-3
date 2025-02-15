import pygame

from game.utils.constants import FONT_STYLE, GAME_OVER, SCREEN_HEIGHT, SCREEN_WIDTH

class FinalMenu:

    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
 
    def __init__(self):
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.game_over = pygame.transform.scale(GAME_OVER, (800, 200))
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
        
        self.decision_font = pygame.font.Font(FONT_STYLE, 15)
        self.decision  = self.decision_font.render("Press  [SPACE]  to Reset Game  |  Press  [RETURN]  to Exit the Game", True, (255, 255, 0))
        self.decision_rect = self.decision.get_rect()
        self.decision_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)
        
        self.max_score_value = 0


    def event(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) : 
                on_close()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                on_start()

        

    def update(self, game):
    
        if game.score > self.max_score_value:
            self.max_score_value = game.score
        self.max_score_message = self.font.render(f"The highest score is: {self.max_score_value} points", True, (255, 255, 255))
        self.max_score_message_rect = self.max_score_message.get_rect()
        self.max_score_message_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)

    def draw (self, screen):
         screen.fill((0, 0, 0))
         screen.blit(self.max_score_message,  self.max_score_message_rect)
         screen.blit(self.game_over, self.game_over_rect)
         screen.blit(self.decision, self.decision_rect)
         pygame.display.update()

        