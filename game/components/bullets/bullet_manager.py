

import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, SPACESHIP_TYPE


class BulletManager:

    def __init__(self):
        self.bullets: list[Bullet] = []
        self.enemy_bullets: list[Bullet] = []
        
    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break
        
        for bullet in self.bullets:
            bullet.update(self.bullets)
            if bullet.rect.colliderect(game.enemy_manager.enemies[0].rect):
                self.bullets.remove(bullet)
            

            # if bullet.rect.colliderect(game.enemy.rect):
            #     self.bullets.remove(bullet)
            #     game.enemy.remove(self)


    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)
            
        if bullet.owner == SPACESHIP_TYPE:
            self.bullets.append(bullet)
        