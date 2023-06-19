import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2


class EnemyManager:

    ENEMIES = [ENEMY_1, ENEMY_2]
    OPTIONS = [1, 2]
    def __init__(self):
        self.enemies: list[Enemy] = []

    def update(self, game):
        if not self.enemies: # [] {} "" -> Valores Falsos 
            self.create_enemies()
            self.increase_enemies(game)
        
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def create_enemies(self):
        self.choise = random.choice(self.OPTIONS)
        if self.choise == 1:
            for enemy_type in self.ENEMIES:
                self.enemies.append(Enemy(enemy_type))
        else:
            self.enemy_type = random.choice(self.ENEMIES)
            self.enemies.append(Enemy(self.enemy_type))

    def increase_enemies(self, game):
        if game.score == 5 or game.score == 15 or game.score == 25:
           self.ENEMIES.append(ENEMY_1)
           
        elif game.score == 10 or game.score == 20 or game.score == 30:
            self.ENEMIES.append(ENEMY_2)

    def reset(self):
        self.enemies.clear()