# Team DBZ
# Npc.py holds the code that determines which npcs the player will encounter 
# throughout the game as well as what items they will drop/trade.


import items


class NonPlayableCharacter:
    def __init__(self):
        self.name = None
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):
    def __init__(self):
        super().__init__()
        self.name = "Trader"
        self.gold = 100
        self.inventory = [items.StaleBread(),
                          items.StaleBread(),
                          items.HealthPotionMinor(),
                          items.HealthPotion(),
                          items.HealthPotionMajor()]
