class Weapon:
    def __init__(self):
        self.name = None
        raise NotImplementedError("Do not create raw weapon objects.")

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5
        self.value = 0


class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust."
        self.damage = 10
        self.value = 2


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing it's age," \
                           "but still has some fight in it."
        self.damage = 20
        self.value = 1


class Sword(Weapon):
    def __init__(self):
        self.name = "Single_Edged Sword"
        self.description = "A sword sharp on one edge. There is a faded relief on the blade."
        self.damage = 5
        self.value = 10


class Axe(Weapon):
    def __init__(self):
        self.name = "Two Headed Axe"
        self.description = "A Two Headed Axe. Engraved in the oak handle is 'The arguments of Kings"
        self.damage = 10
        self.value = 20


class PowerGlove(Weapon):
    def __init__(self):
        self.name = "PowerGlove"
        self.description = "Lucas's Weapon of Choice. Its so bad."
        self.damage = 15
        self.value = 35


class Noisy_Cricket (Weapon):
    def __init__(self):
        self.name = "NoisyCricket"
        self.description = "Chirp, Chirp"
        self.damage = 20
        self.value = 45


class Tanto (Weapon):
    def __init__(self):
        self.name = "Tanto"
        self.description = "Footlong blade of Eastern Origin. It seems more traditional than practical."
        self.damage = 3,
        self.value = 5


class Joyeuse (Weapon):
    def __init__(self):
        self.name = "Joyeuse"
        self.description = "A longsword. It has a regal air and brings to mind Christopher Lee."
        self.damage = 30
        self.value = 100


class Consumable:
    def __init__(self):
        self.healing_value = None
        self.name = None
        raise NotImplementedError("Do not create raw Consumable objects!")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class StaleBread(Consumable):
    def __init__(self):
        self.name = "Stale Bread"
        self.healing_value = 10
        self.value = 0

class HealthPotionMinor(Consumable):
    def __init__(self):
        self.name = "Minor Health Potion"
        self.healing_value = 20
        self.value = 5


class HealthPotion(Consumable):
    def __init__(self):
        self.name = "Health Potion"
        self.healing_value = 40
        self.value = 10


class HealthPotionMajor(Consumable):
    def __init__(self):
        self.name = "Major Health Potion"
        self.healing_value = 60
        self.value = 15
