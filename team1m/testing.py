import random
import time
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
            return "There is a door to your left"
        elif self.exits == 2:
            return "There is a door to your left and a door to your right"
        elif self.exits == 3:
            return "There is a door to your left,  and a door in front of you"
        else:
           return "error"

    def whatis(self):
        if self.treasure == 0:
            return "red sword"
        if self.treasure == 1:
            return "blue sword"
        if self.treasure == 2:
            return "yellow sword"
        if self.treasure == 3:
            return "green sword"

    def findtreasure(self):
        print("You found a", self.whatis())
        return self.treasure

class Monster(object):
    nameDict = {0: "Dog", 1: "Cat", 2: "Bat"}
    statDict = {0: [1.2, 0.8], 1: [1.0, 1.0], 2:[0.8, 1.2]}
    damageDict = {0: {0: 1.0, 1: 0.9, 2: 1.0, 3: 1.1}, 1: {0: 1.1, 1: 1.0, 2: 0.9, 3: 1.0}, 2: {0: 1.0, 1: 1.1, 2: 1.0, 3: 0.9}, 3: {0: 0.9, 1: 1.0, 2: 1.1, 3: 1.0}}

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
        print(self.name+"'s hp is", round(self.hpvalue,2), "\n")

    def setlvl(self, lvl):
        self.lvl = lvl

    def telllvl(self):
        print(self.name+"'s level is", self.lvl, "\n")

    def fight(self):
        return round(self.lvl*self.atk, 2)

    def minushp(self, damage, type):
        damage = round(damage*self.damageDict[type][self.color], 2)
        print(self.name+" takes", damage, "points of damage\n")
        self.hpvalue -= damage


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
        self.HP += 10 * self.lvl
        return self.lvl

    def fight(self):
        return self.attack * self.lvl

    def status(self):
        print("You have ", round(self.defense[0], 2), " defense against Red")
        print("You have ", round(self.defense[1], 2), " defense against Blue")
        print("You have ", round(self.defense[2], 2), " defense against Yellow")
        print("You have ", round(self.defense[3], 2), " defense against Green\n")

    def returnhp(self):
        return round(self.HP, 2)

    def returnatk(self):
        return self.attack
    def updefense(self, color):
        self.defense[color] += 0.1

    def minushp(self, damage, color):
        damage = round(damage / self.defense[color], 2)
        self.HP -= damage
        return damage
print("Hello, what is your name?\n")
mike = Player(1, input(),random.randint(18,22), random.randint(4,7),[round(random.uniform(0.9, 1.1), 2), round(random.uniform(0.9, 1.1), 2),round(random.uniform(0.9, 1.1), 2),round(random.uniform(0.9, 1.1), 2)])

print("Hello",mike.tellname(), "you are in a terrible dungeon full of horrible monsters. Use your color skills to defeat them.\n"
                              "0 does a red attack, 1 does a blue attack, 2 does a yellow attack and 3 does a green attack\n")
time.sleep(1)
print("You have", mike.returnhp(), "hit points\n")
mike.status()
time.sleep(1)
y = 1
while True:
    room1 = Room(random.randint(1, 3), random.randint(0, 3))
    seth = Monster(y, random.randint(0, 2), random.randint(0, 3), random.randint(5, 6), random.randint(8, 11))
    slime = Monster(y, random.randint(0, 2), random.randint(0, 3), random.randint(5, 6), random.randint(8, 11))
    ben = Monster(y, random.randint(0, 2), random.randint(0, 3), random.randint(5, 6), random.randint(8, 11))
    direction = 'g'
    print(room1.sayexits())
    if room1.returnexits() == 1:
        print("You see a", seth.tellcolor(), seth.tellname(), "to your left\n")
        while direction != 'l':
            direction = input("Which way would you like to go? Type 'l' for left, 'r' for right and 'c' for center\n")
            if direction != 'l':
                print("You cannot go that way\n")
    elif room1.returnexits() == 2:
        print("You see a", seth.tellcolor(), seth.tellname(), "to your left\n and you see a", slime.tellcolor(),
              slime.tellname(), "to your right\n")
        while direction != 'l' and direction != 'r':
            direction = input("Which way would you like to go? Type 'l' for left, 'r' for right and 'c' for center\n")
            if direction != 'l' and direction != 'r':
                print("You cannot go that way\n")
    elif room1.returnexits() == 3:
        print("You see a", seth.tellcolor(), seth.tellname(), "to your left,\n you see a", slime.tellcolor(),
              slime.tellname(), "to your right\n and you see a",ben.tellcolor(), ben.tellname(), "in front of you\n" )
        while direction != 'l' and direction != 'r' and direction != 'c':
            direction = input("Which way would you like to go? Type 'l' for left, 'r' for right and 'c' for center\n")
            if direction != 'l' and direction != 'r' and direction != 'c':
                print("You cannot go that way\n")

    if direction == 'l':
        print("You see a", seth.tellcolor(), seth.tellname(),"\n")
        seth.telllvl()
        while seth.hpvalue > 0:
            seth.tellhp()

            x = 4
            while x != 0 and x != 1 and x != 2 and x != 3:
                print(seth.tellname(),"hits you for", mike.minushp(seth.fight(), seth.returncolor()),"points of damage!\n")
                print("You have", mike.returnhp(), "hit points\n")
                if mike.returnhp() <= 0:
                    break
                try:
                    x = int(input("What attack would you like to use?\n"))
                    if x > 3:
                        print("That is not a valid attack\n")
                except ValueError:
                    print("That is not a valid attack\n")
            if mike.returnhp() <= 0:
                break
            seth.minushp(mike.fight(), x)



    elif direction == 'r':
        print("You see a", slime.tellcolor(), slime.tellname(), "\n")
        slime.telllvl()
        while slime.hpvalue > 0:
            slime.tellhp()

            x = 4
            while x != 0 and x != 1 and x != 2 and x != 3:
                print(slime.tellname(),"hits you for", mike.minushp(slime.fight(), slime.returncolor()),"points of damage!\n")
                print("You have", mike.returnhp(), "hit points\n")
                if mike.returnhp() <= 0:
                    break
                try:
                    x = int(input("What attack would you like to use?\n"))
                    if x > 3:
                        print("That is not a valid attack\n")
                except ValueError:
                    print("That is not a valid attack\n")
            if mike.returnhp() <= 0:
                break
            slime.minushp(mike.fight(), x)



    elif direction == 'c':
        print("You see a", ben.tellcolor(), ben.tellname(), "\n")
        ben.telllvl()
        while ben.hpvalue > 0:
            ben.tellhp()

            x = 4
            while x != 0 and x != 1 and x != 2 and x != 3:
                print(ben.tellname(),"hits you for", mike.minushp(ben.fight(), ben.returncolor()),"points of damage!\n")
                print("You have", mike.returnhp(), "hit points\n")
                if mike.returnhp() <= 0:
                    break
                try:
                    x = int(input("What attack would you like to use?\n"))
                    if x > 3:
                        print("That is not a valid attack\n")
                except ValueError:
                    print("That is not a valid attack\n")
            if mike.returnhp() <= 0:
                break
            ben.minushp(mike.fight(), x)


    if mike.returnhp() <= 0:
        break
    mike.lvlup()
    print("You leveled up!")
    print("You have", mike.returnhp(), "hit points\n")
    mike.returnatk()
    mike.updefense(room1.findtreasure())
    mike.status()

    y += 1

print("You have died\n")
