
import random
import pygame
from game.components.powerups.shield import Shield
from game.utils.constants import SPACESHIP, SPACESHIP_SHIELD


class Manager:

    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint (10000, 15000)
        self.duration = 5000
        self.shield_start_time = 0
    def generate_power_up(self):
        shield = Shield()
        self.when_appears += random.randint(10000, 15000)
        self.power_ups.append(shield)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                self.shield_start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_up_time = self.shield_start_time + self.duration
                game.player.set_image((70, 50), SPACESHIP_SHIELD)
                self.power_ups .remove(power_up)

        if game.player.has_power_up and current_time >= game.player.power_up_time:
            game.player.has_power_up = False
            game.player.power_up_type = None
            game.player.set_image((60, 40), SPACESHIP)
            game.player.shield_start_time = 0

    def draw (self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
       now = pygame.time.get_ticks()
       self.power_ups = []
       self.when_appears = random.randint(now + 10000, now + 15000)


