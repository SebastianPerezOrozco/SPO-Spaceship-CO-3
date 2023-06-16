import pygame

class Pause:

    def __init__(self, game):
        self.game = game

    def update(self, user_input):
        pass


    def restart_game(self):
        self.game.death_count = 0
        self.game.is_paused = False

    def close_game(self):
        pygame.quit()
        quit()