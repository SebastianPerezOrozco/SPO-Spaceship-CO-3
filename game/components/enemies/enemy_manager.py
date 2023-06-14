from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2


class EnemyManager:

    ENEMIES = [ENEMY_1, ENEMY_2, ENEMY_1, ENEMY_2, ENEMY_2]

    def __init__(self):
        self.enemies: list[Enemy] = []

    def update(self):
        if not self.enemies: # [] {} "" -> Valores Falsos 
            self.create_enemies()
        
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def create_enemies(self):
        for enemy_type in self.ENEMIES:
            self.enemies.append(Enemy(enemy_type))