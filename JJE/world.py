#Welcome to the world as defined by JJE.
#This determines where the player is on the map.

import random
import enemies
import npc

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass

class StartTile(MapTile):
    def intro_text(self):
        if __name__ == '__main__':
            if __name__ == '__main__':
                return """
                You are locked in an abandoned mansion.
                There are a few paths to travel.
                Can you survive!
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
            self.enemy = enemies.ScayClown()
            self.alive_text = "A Scary Clown jumps out the corner " \
                              "It's in front of you!"
            self.dead_text = "The corpse of a dead clown " \
                             "rots on the ground."
        elif r < 0.80:
            self.enemy = enemies.ViciousDog()
            self.alive_text = "A vicious dog is blocking your path!"
            self.dead_text = "A dead dog reminds you your alive."

        elif r < 0.95:
            self.enemy = enemies.BatColony()
            self.alive_text = "You hear a squeaking noise growling louder " \
                              "...hundreds of bats swarm around you!"
            self.dead_text = "The bats lay scattered on the ground."
        else:
            self.enemy = enemies.JumboRat()
            self.alive_text = "You've awaken a Jumbo Rat."
            self.dead_text = "The rat scattered in fear."
        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.hp))

class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
              Escape is in you grasp!
              You Survived!!!
               """

class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def intro_text(self):
        return """
        A creature awaits in the corner.
        He looks willing to trade.
        """

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Pennies".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice -1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.pennies = seller.pennies + item.value
        buyer.pennies = buyer.pennies - item.value
        print("Trade complete!")

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)

class FindPenniesTile(MapTile):
    def __init__(self, x, y):
        self.pennies = random.randint(1, 50)
        self.pennies_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.pennies_claimed:
            self.pennies_claimed = True
            player.pennies = player.pennies + self.pennies
            print("+{} pennies added.".format(self.pennies))

    def intro_text(self):
        if self.pennies_claimed:
            return """
            Another unremarkable part of the cave. You must forge onwards.
            """
        else:
            return """
            Someone dropped some pennies. You pick it up.
            """

world_dsl = """
|EN|EN|VT|EN|EN|
|EN|  |  |  |EN|
|EN|FG|EN|  |TT|
|TT|  |ST|FG|EN|
|FG|  |EN|  |FG|
"""

world_map = []

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None

start_tile_location = None

def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


tile_type_dict = {
    "VT": VictoryTile,
    "EN": EnemyTile,
    "ST": StartTile,
    "FG": FindPenniesTile,
    "TT": TraderTile,
    "  ": None}
