# NPC for JJE
# Handles players and trade options

import items

class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name

class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.gold = 100
        self.inventory = [items.MoldyBread(),
                          items.MoldyBread(),
                          items.HealingPotion(),
                          items.HealingPotion]

