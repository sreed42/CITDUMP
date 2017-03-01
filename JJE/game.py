# This is the new main game file.

from player import Player

def play():
    inventory = [Rock(), Blunt_Sword(), 'Pennies(2)', 'Moldy Bread']
    print("Escape from the abandoned mansion!")
    player = Player()
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            print("Go North!")
        elif action_input in ['s', 'S']:
            print("Go South!")
        elif action_input in ['e', 'E']:
            print("Go East!")
        elif action_input in ['w', 'W']:
            print("Go West young man!")
        elif action_input in ['i', 'I']:
            player.print_inventory()
        else:
            print("Invalid option!")

def get_player_command():
    return input('Action (N, S, E, W, I: ')


play()
