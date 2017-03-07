# Team DBZ
# Items.py holds all the code for the various items within the game 
# which includes weapons, currency and consumables such as food and health potions.


class Weapon:
    def __init__(self):
        self.name = None
        raise NotImplementedError("Do not create raw weapon objects.")

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5


class Dagger(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Dagger"
        self.description = "A small dagger with some rust."
        self.damage = 10


class RustySword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Rusty Sword"
        self.description = "This sword is showing it's age," \
                           "but still has some fight in it."
        self.damage = 20


class Consumable:
    def __init__(self):
        self.healing_value = None
        self.name = None
        raise NotImplementedError("Do not create raw Consumable objects!")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class StaleBread(Consumable):
    def __init__(self):
        super().__init__()
        self.name = "Stale Bread"
        self.healing_value = 10


class HealthPotionMinor(Consumable):
    def __init__(self):
        super().__init__()
        self.name = "Minor Health Potion"
        self.healing_value = 20


class HealthPotion(Consumable):
    def __init__(self):
        super().__init__()
        self.name = "Health Potion"
        self.healing_value = 40


class HealthPotionMajor(Consumable):
    def __init__(self):
        super().__init__()
        self.name = "Major Health Potion"
        self.healing_value = 60
