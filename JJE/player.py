#This is the code to handle the player.

import items

class Player:
    def __init__(self):
        self.inventory = [items.Rock(),
                          items.Blunt_Sword(),
                          'Pennies(2)',
                          items.Moldy_Bread()]
        self.x = 1
        self.y = 2
        self.hp = 100

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

    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]
        if consumables == []:
            print("You have no items that can heal you.")
            return

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

    def attack(self):
        strongest_weapon = self.strongest_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("You use {} against {}!".format(strongest_weapon.name, enemy.name))
        enemy.hp -= strongest_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))
