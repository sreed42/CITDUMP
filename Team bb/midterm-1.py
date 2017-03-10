from math import floor
from random import randint


# base class for all heroes and monsters in the game
# It should be noted that all the stats for classes need some tinkering to adjust the difficulty to a level
# that is more enjoyable. As the coding stands the game shows what it can do but you are probably going to get
# slaughtered early by some monster's special attack or get lucky and survive on.


class Entity:
    def __init__(self, lvl, hp_base, atk_base, int_base, hp_mult, atk_mult, int_mult, mp_add, hp_add):
        self.lvl = lvl
        self.hp_base = hp_base
        self.atk_base = atk_base
        self.int_base = int_base
        self.hp_mult = hp_mult
        self.atk_mult = atk_mult
        self.int_mult = int_mult
        self.mp_add = mp_add
        self.hp_add = hp_add
        self.name = ""
        self.special_name = ""
        self.max_hp = 0
        self.hp = 0
        self.atk = 0
        self.int = 0
        self.mp = 100
        self.exp = 0
        self.max_exp = 100
        self.item = 0
        self.dodge = False
        self.dodges = False
        self.counterA = False
        self.counterS = False
# after creating the object with it's level the update function scales it's stats to its level

    def update(self):
        self.max_hp = self.hp_base + floor(self.lvl * self.hp_mult)
        self.atk = self.atk_base + floor(self.lvl * self.atk_mult)
        self.int = self.int_base + floor(self.lvl * self.int_mult)
        self.hp = self.max_hp

    def item_check(self):
        if self.item == 0:
            print("You currently have no item\n")
        elif self.item == 1:
            print("You have a red potion\n")
        elif self.item == 2:
            print("You have a blue potion\n")
        elif self.item == 3:
            print("You have an ether\n")
        elif self.item == 4:
            print("You have a hi-ether\n")

    def info(self):
        print("HP: " + str(self.hp) + "/" + str(self.max_hp) + " MP: " + str(self.mp) + "/100" + " ATK: " + str(
            self.atk) + " INT: " + str(self.int) + " EXP: " + str(self.exp) + "/" + str(self.max_exp))

    def use_item(self):
        if self.item == 0:
            print("You don't have any items\n")
        if self.item == 1:
            print(player.name + " used a red potion\n")
            self.hp += floor(self.max_hp / 5)
            if self.hp > self.max_hp:
                self.hp = self.max_hp
        if self.item == 2:
            print(player.name + " used a blue potion\n")
            self.hp += floor(self.max_hp / 2)
            if self.hp > self.max_hp:
                self.hp = self.max_hp
        if self.item == 3:
            print(player.name + " used an ether\n")
            self.mp += 30
            if self.mp > 100:
                self.mp = 100
        if self.item == 4:
            print(player.name + " used a hi-ether\n")
            self.mp += 60
            if self.mp > 100:
                self.mp = 100
# every round in battle there is an hp and mp regen different for every hero

    def tally_round(self):
        self.mp += self.mp_add
        if self.mp > 100:
            self.mp = 100
        self.hp += self.hp_add
        if self.hp > self.max_hp:
            self.hp = self.max_hp

# called after an enemy monster is killed

    def tally_exp(self, other):
        self.exp += other.exp
        if self.exp >= self.max_exp:
            self.exp -= self.max_exp
            self.lvl += 1
            self.max_exp *= 2
            self.update()
            print(player.name + " grew a lvl")

# HERO CLASSES


class Warrior(Entity):
    def __init__(self, lvl):
        super().__init__(lvl, 20, 3, 1, 3, 3, 1, 4, 3)
        self.name = "Warrior"
        self.special_name = "Overpower"
        self.update()

    def special(self):
        return int(floor(self.atk * 1.5))


class Rogue(Entity):
    def __init__(self, lvl):
        super().__init__(lvl, 16, 2, 2, 1.5, 2.5, 2, 6, 3)
        self.name = "Rogue"
        self.special_name = "Backstab"
        self.dodge = True
        self.update()

    def special(self):
        return self.atk * 2


class Mage(Entity):
    def __init__(self, lvl):
        super().__init__(lvl, 14, 2, 4, 1.2, 1, 3, 10, 2)
        self.name = "Mage"
        self.special_name = "Wizard Bolt"
        self.update()

    def special(self):
        return int(floor(self.int * 2.5))

# MONSTER CLASSES


class Ghoul(Entity):
    def __init__(self, lvl):
        super().__init__(lvl, 6, 2, 1, 1.5, 1.5, 1, 0, 0)
        self.name = "Ghoul"
        self.special_name = "Bite and Chew"
        self.exp = self.lvl * 30
        self.update()

    def special(self):
        self.hp += floor(self.max_hp / 4)
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        return self.atk


class Demon(Entity):
    def __init__(self, lvl):
        super().__init__(lvl, 6, 2, 1, 2, 2, 1, 0, 0)
        self.name = "Demon"
        self.special_name = "Dodge and Strike"
        self.counterA = True
        self.exp = self.lvl * 50
        self.update()

    def special(self):
        return player.atk


class Imp(Entity):
    def __init__(self, lvl):
        super().__init__(lvl, 5, 1, 2, 1.5, 1, 2, 0, 0)
        self.name = "Imp"
        self.special_name = "Firebolt"
        self.exp = self.lvl * 40
        self.dodge = True
        self.update()

    def special(self):
        return int(floor(self.int * 2))


class Golem(Entity):
    def __init__(self, lvl):
        super().__init__(lvl, 10, 3, 1, 3, 2, 1, 0, 0)
        self.name = "Golem"
        self.special_name = "Counter Special"
        self.exp = self.lvl * 70
        self.counterS = True
        self.update()

    def special(self):
        return player.special()


class Wraith(Entity):
    def __init__(self, lvl):
        super().__init__(lvl, 8, 2, 3, 2, 1.5, 3.5, 0, 0)
        self.name = "Wraith"
        self.special_name = "Death's Embrace"
        self.exp = self.lvl * 60
        self.update()

    def special(self):
        return self.int * 2

# Boss called every 10 floors


class Dragon(Entity):
    def __init__(self, lvl):
        super().__init__(lvl, 15, 3, 1, 3, 3, 2, 0, 0)
        self.name = "Dragon"
        self.special_name = "Dragon Breath"
        self.exp = self.lvl * 100
        self.update()

    def special(self):
        return self.atk * 2

# Creates a random monster, or if the current floor is a multiple of 10, creates a dragon
# If the player level is higher than 3, the monster level is random between 3 below or above the player


def gen_monster():
    if current_floor % 10 == 0:
        return Dragon(randint(player.lvl - 3, player.lvl + 3))
    elif player.lvl <= 3:
        mon = randint(1, 5)
        if mon == 1:
            return Ghoul(player.lvl)
        elif mon == 2:
            return Demon(player.lvl)
        elif mon == 3:
            return Imp(player.lvl)
        elif mon == 4:
            return Golem(player.lvl)
        else:
            return Wraith(player.lvl)
    else:
        mon = randint(1, 5)
        if mon == 1:
            return Ghoul(randint(player.lvl - 3, player.lvl + 3))
        elif mon == 2:
            return Demon(randint(player.lvl - 3, player.lvl + 3))
        elif mon == 3:
            return Imp(randint(player.lvl - 3, player.lvl + 3))
        elif mon == 4:
            return Golem(randint(player.lvl - 3, player.lvl + 3))
        else:
            return Wraith(randint(player.lvl - 3, player.lvl + 3))

# dodge chance for the rogue and imp


def dodge_chance():
    chance = randint(1, 4)
    if chance == 1:
        return True
    else:
        return False

# Alright so if I'm being honest here, this is probably way more complicated than it needs to be
# I probably could have found a better way to deal with the battling but I just stuck with this
# since I didn't want to have to redo a lot of things

# action1 is the heroes selected action, action2 is the randomly selected action of the monster


def battle(action1, action2):
    # checks if the player or monster is going to dodge
    if player.dodge:
        player.dodges = dodge_chance()
    if monster.dodge:
        monster.dodges = dodge_chance()

    # I set line1 and line2 up so I wouldn't have to retype too much
    line1 = ""
    line2 = ""
    if action1 == 1 and monster.dodges:
        line1 = player.name + " attacks and Imp dodges"
    else:
        line1 = player.name + " attacks for " + str(player.atk) + " damage"
    if action1 == 3:
        line1 = player.name + " uses " + player.special_name + " for " + str(player.special()) + " damage"

    if action2 == 1 and player.dodges:
        line2 = monster.name + " attacks and Rogue dodges"
    else:
        line2 = monster.name + " attacks for " + str(monster.atk) + " damage"
    if action2 == 3 and not monster.counterA and not monster.counterS:
        line2 = monster.name + " uses " + monster.special_name + " for " + str(monster.special()) + " damage"

    # Here is where things get way more complicated than they need to be
    # I basically just roll through every possible outcome of the choices in actions
    if action1 == 1:
        if action2 == 1:
            if monster.dodges and player.dodges:
                print(line1)
                print(line2)
            elif monster.dodge and not player.dodge:
                print(line1)
                print(line2)
                player.hp -= monster.atk
            elif not monster.dodge and player.dodge:
                print(line1)
                print(line2)
                monster.hp -= player.atk
            elif not monster.dodge and not player.dodge:
                print(line1)
                print(line2)
                player.hp -= monster.atk
                monster.hp -= player.atk
        if action2 == 2:
            print(player.name + " attacks and " + monster.name + " blocks")
        if action2 == 3:
            if monster.counterA:
                print(player.name + " attacks but Demon counters")
                player.hp -= player.atk
            elif monster.counterS:
                print(line1)
                print("Golem counters nothing")
                monster.hp -= player.atk
            else:
                print(line1)
                print(line2)
                monster.hp -= player.atk
                player.hp -= monster.special()
    if action1 == 2:
        if action2 == 1:
            print(monster.name + " attacks but " + player.name + " blocks")
        elif action2 == 2:
            print("You both block")
        elif action2 == 3:
            if monster.counterA:
                print("You block and Demon counters nothing")
            elif monster.counterS:
                print("You block and Golem counters nothing")
            else:
                print("You try to block but " + monster.name + " uses " + monster.special_name + " for " + str(
                    monster.special()) + " damage")
                player.hp -= monster.special()
    if action1 == 3:
        player.mp -= 25
        if action2 == 1:
            if player.dodges:
                print(line1)
                print(line2)
                monster.hp -= player.special()
            else:
                print(line1)
                print(line2)
                monster.hp -= player.special()
                player.hp -= monster.atk
        if action2 == 2:
            print(monster.name + " tries to block but " + player.name + " uses " + player.special_name + " for " + str(
                player.special()) + " damage")
            monster.hp -= player.special()
        if action2 == 3:
            if monster.counterA:
                print("Demon can't do anything")
                print(line2)
                monster.hp -= player.special()
            elif monster.counterS:
                print("Golem counters your " + player.special_name + " for " + str(player.special()) + " damage")
                player.hp -= player.special()
            else:
                print(line1)
                print(line2)
                player.hp -= monster.special()
                monster.hp -= player.special()

# Call this every time a monster is defeated
def item_drop():
    if player.item == 0:
        chance = randint(1, 4)
        if chance == 1:
            random_item = randint(1, 4)
            player.item = random_item
            if random_item == 1:
                print("You found a red potion\n")
            elif random_item == 2:
                print("You found a blue potion\n")
            elif random_item == 3:
                print("You found an ether\n")
            else:
                print("You found a hi-ether\n")

# Keeps track of what level your on
current_floor = 1

# Now that all the prep work is done above the actual game starts here and doesn't take up too much space
while True:
    print("Welcome to the unending dungeon")
    print("Choose your hero\n")
    while True:
        choice = int(input("(1) Warrior (2) Rogue (3) Mage\n"))
        if choice == 1:
            # the heroes all start at level 1
            player = Warrior(1)
            break
        elif choice == 2:
            player = Rogue(1)
            break
        elif choice == 3:
            player = Mage(1)
            break
        else:
            print("You must choose a hero\n")
    player.update()

    # Hero has been created and the next while loop will continue until the player's hp <= 0
    while True:
        print("Current floor: " + str(current_floor))
        choice = int(input("(1) Continue (2) Check stats (3) Check item\n"))
        if choice == 2:
            player.info()
        elif choice == 3:
            player.item_check()
        elif choice == 1:
            monster = gen_monster()
            monster.update()
            print("You ran into a " + monster.name + " LVL: " + str(monster.lvl) + "\n")

            while True:
                print("Your HP: " + str(player.hp) + "/" + str(player.max_hp) + " MP: " + str(
                    player.mp) + "/100 EXP: " + str(player.exp) + "/" + str(player.max_exp))
                print(monster.name + " HP: " + str(monster.hp) + "/" + str(monster.max_hp) + "\n")
                action1 = int(input("(1) Attack (2) Block (3) Special (4) Use item"))
                # the monster's action, action2 is selected at random
                action2 = randint(1, 3)
                if action1 == 3 and player.mp < 25:
                    print("You don't have enough mp\n")
                elif action1 == 4:
                    player.use_item()
                else:
                    battle(action1, action2)
                    # hp and mp regen every round in battle
                    player.tally_round()
                # If the player hp is 0 break out of the loops and end the game
                if player.hp <= 0:
                    break
                if monster.hp <= 0:
                    print("You killed the " + monster.name + "\n")
                    # give the player exp
                    player.tally_exp(monster)
                    # check for item drop chance
                    item_drop()
                    # increase the floor level and repeat
                    current_floor += 1
                    break
        if player.hp <= 0:
            break
    print("\n You're dead. You made it to Floor " + str(current_floor) + " and your lvl was " + str(player.lvl))
    break
