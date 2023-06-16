import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_manager import BulletManager

from game.utils.constants import SPACESHIP_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite):

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500
        self.type = SPACESHIP_TYPE
        
     
        

    def move_left(self):
        self.rect.x -= 10
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH

    def move_right(self):
        self.rect.x += 10
        if self.rect.left > SCREEN_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 50:
            self.rect.y += 10

    def shoot_bullet(self, bullet_manager):
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)

    def update(self, user_input, game):

        if user_input[pygame.K_LEFT]:
            self.move_left()

        if user_input[pygame.K_RIGHT]:
            self.move_right()

        if user_input[pygame.K_UP]:
            self.move_up()

        if user_input[pygame.K_DOWN]:
            self.move_down()
        
        if user_input[pygame.K_SPACE]:
            self.shoot_bullet(game.bullet_manager)


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

        # if self.rect.left < 0:
        #     screen.blit(self.image, (self.rect.left + SCREEN_WIDTH, self.rect.y))
            
        # if self.rect.right > SCREEN_WIDTH:
        #     screen.blit(self.image, (self.rect.left - SCREEN_WIDTH, self.rect.y))
