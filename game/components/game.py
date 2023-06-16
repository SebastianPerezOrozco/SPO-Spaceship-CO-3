import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.components.pause import Pause
from game.components.spaceship import Spaceship

from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.score = 0
        self.death_count = 0
        self.max_score = 0

        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()

        self.menu = Menu("Press any key to start...")

    def run(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu(self)

        pygame.display.quit()
        pygame.quit()

    def play(self):
        self.playing = True
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

            if self.score > self.max_score:
                self.max_score = self.score
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot_bullet(self.bullet_manager)

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)


    def show_menu(self, game):
        if self.death_count > 0:
            self.menu.update_message(f"Final score is: {game.score} points" )
            self.menu.update_max_score_value(game.max_score)
            pause_menu = Pause(self)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key_pressed = event.key

                    if key_pressed == pygame.K_RETURN:
                        pause_menu.restart_game()
                    elif key_pressed == pygame.K_ESCAPE:
                        pause_menu.close_game()
        

        self.menu.draw(game.screen)
        self.menu.event(self.on_close, game.play)

    def on_close(self):
        self.playing = False
        self.running = False