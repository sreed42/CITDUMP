# items for the JJE game
# This is the items of the games such as weapons and health items.

class Weapon:
    def __init__(self):
        self.name = None
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "I guess this is a weapon, " \
                           "about the size of your hand."
        self.damage = 1
        self.value = 1

class Blunt_Sword(Weapon):
    def __init__(self):
        self.name = "Blunt Sword"
        self.description = "More useful as a club than a cutting tool."
        self.damage = 5
        self.value = 20

class Pistol(Weapon):
    def __init__(self):
        self.name = "9mm Pistol"
        self.description = "Bang bang!"
        self.damage = 20
        self.value = 80

class Sharp_Sword(Weapon) :
    def __init__(self):
        self.name = "Sharp Sword"
        self.description = "Better for cutting that the Blunt Sword."
        self.damage = 20
        self.value = 20

class Spear(Weapon):
    def __init__(self):
        self.name = "Spear"
        self.description = "Poke 'em with the pointy bit."
        self.damage = 15
        self.value = 30

class Shotgun(Weapon):
    def __init__(self):
        self.name = "Shotgun"
        self.description = "Blow them away!"
        self.damage = 25
        self.value = 100

class Knife(Weapon):
    def __init__(self):
        self.name = "Knife"
        self.description = "Better than the rock."
        self.damage = 60
        self.value = 30

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumbable objects.")

    def __str__(self):
        return self.name

    def __init__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)

    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, item.Consumable)]
        if not consumables:
            print("You do not have any items to help heal you.")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to help heal you: ")
            print("{}, {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Not a valid choice, try again!")

class MoldyBread(Consumable):
    def __init__(self):
        self.name = "Moldy Bread"
        self.healing_value = 10
        self.value = 12

class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60
