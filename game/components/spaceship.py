import pygame
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP


class Spaceship(Sprite):

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500

    def move_left(self):
        self.rect.x -= 10
        # if self.rect.right < 0:
        #     self.rect.x = SCREEN_WIDTH

    def move_right(self):
        self.rect.x += 10
        # if self.rect.left > SCREEN_WIDTH:
        #     self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 50:
            self.rect.y += 10

    def update(self, user_input):

        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()

        # elif user_input[pygame.K_LEFT] and user_input[pygame.K_UP]:
        #     self.move_left() 
        #     self.move_up()
        # elif user_input[pygame.K_LEFT] and user_input[pygame.K_DOWN]:
        #     self.move_left()
        #     self.move_down()
        # elif user_input[pygame.K_RIGHT] and user_input[pygame.K_UP]:
        #     self.move_right()
        #     self.move_up()
        # elif user_input[pygame.K_RIGHT] and user_input[pygame.K_DOWN]:
        #     self.move_right()
        #     self.move_down()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

        if self.rect.left < 0:
            screen.blit(self.image, (self.rect.left + SCREEN_WIDTH, self.rect.y))

        elif self.rect.right > SCREEN_WIDTH:
            screen.blit(self.image, (self.rect.left - SCREEN_WIDTH, self.rect.y))
