# Enemies list for JJE
# Here you will find details on all of the enemies such as name, health, and damage they cause

class Enemy:
    def __init__(self):
        self.hp = None
        self.name = None
        raise NotImplementedError("Do not create raw Enemy objets.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

class Lich(Enemy):
    def __init__(self):
        self.name = "Lich"
        self.description = "An undead creature"
        self.hp = 30
        self.damage = 10

class Mummy(Enemy):
    def __init__(self):
        self.name = "Mummy"
        self.hp = 80
        self.damage = 13

class ViciousDog(Enemy):
    def __init__(self):
        self.name = "Vicious Dog"
        self.hp = 75
        self.damage = 15

class ScaryClown(Enemy):
    def __init__(self):
        self.name = "Scary Clown"
        self.hp = 100
        self.damage = 7

class JumboRat(Enemy):
    def __init__(self):
        self.name = "Jumbo Rat"
        self.hp = 20
        self.damage = 5
