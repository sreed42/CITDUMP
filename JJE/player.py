#This is the code to handle the player.

import items

class Player:
    def __init__(self):
        self.inventory = [items.Rock(),
                          items.Blunt_Sword(),
                          'Pennies(2)',
                          'Moldy Bread']
        self.x = 1
        self.y = 2

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item))
        best_weapon = self.strongest_weapon()
        print("Your strongest weapon is your {}".format(best_weapon))

    def strongest_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon
