class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objets.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        self.name = "Giant Spider"
        self.hp = 10
        self.damage = 2

class Lich(Enemy):
    def __init__(self):
        self.name = "Lich"
        self.hp = 30
        self.damage = 10

class BatColony(Enemy):
    def __init__(self):
        self.name = "Colony of Bats"
        self.hp = 100
        self.damage = 4

class Mummy(Enemy):
    def __init__(self):
        self.name = "Mummy"
        self.hp = 80
        self.damage = 15
        