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

class Blunt_Sword(Weapon):
    def __init__(self):
        self.name = "Blunt Sword"
        self.description = "More useful as a club than a cutting tool."
        self.damage = 5

class Pistol(Weapon):
    def __init__(self):
        self.name = "9mm Pistol"
        self.description = "Bang bang!"
        self.damage = 20
