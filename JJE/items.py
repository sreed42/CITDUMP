#items for the JJE game

class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "I guess this is a weapon. " \
                "About the size of your hand."
        self.damage = 1
        self.value = 1

class Blunt_Sword(Weapon):
    def __init__(self):
        self.name = "Blunt Sword"
        self.description = "More useful as a club than a cutting tool."
        self.damage = 5
        self.value = 10

class Pistol(Weapon):
    def __init__(self):
        self.name = "9mm Pistol"
        self.description = "Bang bang!"
        self.damage = 20
        self.value = 15

class Sharp_Sword(Weapon) :
    def __init__(self):
        self.name = "Sharp Sword"
        self.description = "Better for cutting that the Blunt Sword."
        self.damage = 10
        self.value = 20

class Spear(Weapon):
    def __init__(self):
        self.name = "Spear"
        self.description = "Poke 'em with the pointy bit."
        self.damage = 15
        self.value = 25

class Shotgun(Weapon):
    def __init__(self):
        self.name = "Shotgun"
        self.description = "Blow them away!"
        self.damage = 25
        self.value = 30

class Knife(Weapon):
    def __init__(self):
        self.name = "Knife"
        self.description = "Better than the rock."
        self.damage = 7
        self.value = 5

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects!")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self,healing_value)

class Moldy_Bread(Consumable):
    def __init__(self):
        self.name = "Moldy Bread"
        self.healing_value = 10
        self.value = 12
        
class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60
