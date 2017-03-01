#This is the code to handle the player.

import items

class Player:
    def __init__(self):
        self.inventory = [items.Rock(),
                          items.Blunt_Sword(),
                          'Pennies(2)',
                          'Moldy Bread']

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item))
        best_weapon = self.strongest_weapon()
        print("Your strongest weapon is your {}".format(best_weapon))

    def strongest_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon
