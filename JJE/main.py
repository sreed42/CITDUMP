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

def choosePath():
    door = input('> ')
    if door == "1":
        print("You chose door #1 the green light is far less intimidating.")
        print("You walk in and see a flash light and a hammer.")
        print("What do you want to do?")
        print("Option1: Take the flashlight")
        print("Option2: Take the hammer.")

        tools = input('>')

        if tools == "1":
            print("You choose to take the flashlight.")
            print("You can now see which ways you can go, but you have nothing to protect you.")

        elif tools == "2":
            print("You choose the hammer. You can't see but you do have a weapon.")

        else:
            print("Your a rebel you take both and continue on your journey.")

    elif door == "2":
        print("You chose door #2. You walk in and see a clown standing in the corner.")
        print("What are you going to do?")
        print("Option1: Walk up to the clown and touch him.")
        print("Option2: Continue on to the next room hoping he doesn't follow.")

        clown = input('>')

        if clown == "1":
            print("Your feeling brave so you choose to walk up to the clown.")
            time.sleep(3)
            print("As you lift your hand to touch him he grabs you.")

        elif clown == "2":
            print("You got scarred and tried to go around the clown.")
            print("He feeds on fear. He hunts you down and grabs you.")

        else:
            print("You didn't know what to do so you stared at the clown he eventually faded away.")

    return door

def checkPath(chosenPath):
    print("That was scary")

    correctPath = random.randint(1,2)

    if chosenPath == correctPath:
        print("What a relief")
        print("I don't know how you did it but you managed to escape")
        print("Good job")

    else:
        print("That was horrible you couldn't escape")
        print("Better luck next time")

playAgain = "yes"
while playAgain == "yes":
    displayIntro()
    choice = choosePath()
    checkPath(choice)
    playAgain = input("Would you like to play again? Type yes if so")
