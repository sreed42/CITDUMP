#This is the main file for the JJE team project.
#It will house most of our code.
#Midterm Jacob, Jaden, Elizabeth
#Text adventure game
#Hope this works

import random
import time

def displayIntro():
    print("You are locked in an abandoned mansion")
    print("There will be a series of options for you to choose from which will determine your fate.")
    print("Can you escape?")
    time.sleep(2)
    print("You come to your first option. Your in a dark room and see 2 doors.")
    print("The first door has a shinning green light from underneath while the 2nd has a red light beaming through.")
    print("Do you want to enter door #1 or door #2?")

def choosedoor():
    door = input('> ')

    if door == "1":
        print("You chose door #1. You walk in and see.....")
        print("What do you want to do?")
        print("Option1: ...........")
        print("Option2: ...........")

        whatyousee = input('>')

        if whatyousee == "1":
            print("...........")

        elif whatyousee == "2":
            print(".........")

    else:
        print(".............")

    elif door == "2":
    print("You chose door #2. You walk in and........")
    print("What are you going to do?")
    print("Option1: ............")
    print("Option2: ............")

    whatyousee2 = input('>')

    if whatyousee2 == "1":
        print(".............")

    elif whatyousee2 == "2":
        print("............")

    else:
        print("...........")

def checkPath():
    print("")

displayIntro()
chooseDoor()

