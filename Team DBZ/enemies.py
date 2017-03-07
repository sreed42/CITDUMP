class Enemy:
    def __init__(self):
        self.hp = None
        self.name = None
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Giant Spider"
        self.hp = 10
        self.damage = 2


class Ogre(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Ogre"
        self.hp = 30
        self.damage = 10


class BatColony(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Colony of bats"
        self.hp = 100
        self.damage = 4


class RockMonster(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Rock Monster"
        self.hp = 80
        self.damage = 15


class Seth(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Seth Reed"
        self.hp = 200
        self.damage = 20
