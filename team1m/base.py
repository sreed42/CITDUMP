class Room(object):
    def __init__(self, exits, treasure):
        self.exits = exits
        self.treasure = treasure

    def setexits(self, exits):
        self.exits = exits

    def settreasure(self, treasure):
        self.treasure = treasure

    def returnexits(self):
        return self.exits

    def sayexits(self):
        if self.exits == 1:
            return "There is a door to your left\n"
        elif self.exits == 2:
            return "There is a door to your left and a door to your right\n"
        elif self.exits == 3:
            return "There is a door to your left, a door to your right and a door in front of you\n"
        else:
           return "error\n"

    def whatis(self):
        if self.treasure == 0:
            return "red shard\n"
        if self.treasure == 1:
            return "blue shard\n"
        if self.treasure == 2:
            return "yellow shard\n"
        if self.treasure == 3:
            return "green shard\n"

    def findtreasure(self):
        return "You found a "+self.whatis()

    def gettreasure(self):
        return self.treasure


class Monster(object):
    nameDict = {0: "Dog", 1: "Cat", 2: "Bat"}
    statDict = {0: [1.2, 0.8], 1: [1.0, 1.0], 2: [0.8, 1.2]}
    damageDict = {0: {0: 1.0, 1: 0.9, 2: 1.0, 3: 1.1}, 1: {0: 1.1, 1: 1.0, 2: 0.9, 3: 1.0},
                  2: {0: 1.0, 1: 1.1, 2: 1.0, 3: 0.9}, 3: {0: 0.9, 1: 1.0, 2: 1.1, 3: 1.0}}

    def __init__(self, lvl, name, color, atk, hpvalue=0.0):
        self.hpvalue = round(self.statDict[name][0]*hpvalue*lvl, 2)
        self.name = self.nameDict[name]
        self.color = color
        self.lvl = lvl
        self.atk = atk*self.statDict[name][1]

    def sethp(self, newhp):
        self.hpvalue = newhp

    def setcolor(self, color):
        self.color = color

    def tellcolor(self):
        if self.color == 0:
            return "Red"
        elif self.color == 1:
            return "Blue"
        elif self.color == 2:
            return "Yellow"
        elif self.color == 3:
            return "Green"
        else:
            return ""

    def returncolor(self):
        return self.color

    def tellname(self):
        return self.name

    def tellhp(self):
        return self.hpvalue

    def setlvl(self, lvl):
        self.lvl = lvl

    def telllvl(self):
        print(self.name+"'s level is", self.lvl, "\n")

    def fight(self):
        return round(self.lvl*self.atk, 2)

    def minushp(self, damage, type):
        damage = round(damage*self.damageDict[type][self.color], 2)
        self.hpvalue -= damage
        return str(damage)


class Player:
    def __init__(self, lvl, name, HP, attack, defense):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.lvl = lvl
        self.defense = defense

    def tellname(self):
        return self.name

    def lvlup(self):
        self.lvl += 1
        if self.lvl < 5:
            self.HP += 10 * self.lvl
        else:
            self.HP += (7 * self.lvl) + 10
        return self.lvl

    def fight(self):
        return self.attack * self.lvl

    def status(self):
        return "You have "+str(round(self.defense[0], 2))+" defense against Red\nYou have "\
               +str(round(self.defense[1], 2))+ " defense against Blue\nYou have "+str(round(self.defense[2], 2))+\
               " defense against Yellow\nYou have "+str(round(self.defense[3], 2))+" defense against Green\n"



    def returnhp(self):
        return round(self.HP, 2)

    def returnatk(self):
        return self.attack

    def updefense(self, color):
        self.defense[color] += 0.1

    def minushp(self, damage, color):
        damage = round(damage / self.defense[color], 2)
        self.HP -= damage
        return str(damage)
