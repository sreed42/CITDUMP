#Welcome to the world as defined by JJE.
import random
import enemies


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass!!")

class StartTile:
    def intro_text(self):
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
        elif r < 0.80:
            self.enemy = enemies.Lich()
        elif r < 0.95:
            self.enemy = enemies.BatColony()
        else:
            self.enemy = enemies.Mummy()
            
        super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            return "A {} awaits!".format(self.enemy.name)
        else:
            return "You've defeated the {}.".format(self.enemy.name)


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
