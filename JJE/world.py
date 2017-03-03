#Welcome to the world as defined by JJE.
import random
import enemies


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass!!")

    def modify_player(self, player):
        pass

class StartTile(MapTile):
    def intro_text(Self):
        return """
        You are locked in an abandoned mansion.
        There are a few paths to travel.
        Can you survive?
        """

class BoringTile(MapTile):
    def intro_text(self):
        return """
        Not much is happening here.
        """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            self.alive_text = "A giant spider falls from the ceiling in front of you."
            self.dead_text = "As the spider dies, it curls up and flips to its back."
        elif r < 0.80:
            self.enemy = enemies.Lich()
            self.alive_text = "A Lich appears before you."
            self.dead_text = "The Lich vanishes in a flash of light."
        elif r < 0.95:
            self.enemy = enemies.BatColony()
            self.alive_text = "As you enter the area a black mass flies towards you." \
                              "Suddenly you are engulfed by a swarm of bats!"
            self.dead_text = "Hundreds of dead bats now litter the ground."
        else:
            self.enemy = enemies.Mummy()
            self.alive_text = "A shambling horror approaches."
            self.dead_text = "The Mumy vanishes and all that is left are rotten bandages on the ground."
            
        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP left.".format(self.enemy.damage, player.hp))


class VictoryTile(MapTile):
    def intro_text(self):
        return """
        Escape is in your grasp!
        You survived!!!!
        """

world_map = [
    [None, VictoryTile(1, 0), None],
    [None, EnemyTile(1, 1), None],
    [EnemyTile(0, 2), StartTile(1, 2), EnemyTile(2, 2)],
    [None, EnemyTile(1, 3), None]
]

def tile_at(x,y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
