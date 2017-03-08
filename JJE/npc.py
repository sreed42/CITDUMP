import items

class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __init__(self):
        return self.name

class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.pennies = 100
        self.inventory = [items.MoldyBread(),
                          items.MoldyBread(),
                          items.HealingPotion()]
