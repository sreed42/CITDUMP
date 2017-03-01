# This is the new main game file.


def play():
    inventory = [Rock(), Blunt_Sword(), 'Pennies(2)', 'Moldy Bread']
    print("Escape from the abandoned mansion!")
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
            print("Inventory: ")
            for item in inventory:
                print('* ' + str(item))
        else:
            print("Invalid option!")

def get_player_command():
    return input('Action (N, S, E, W, I: ')

def strongest_weapon(inventory):
    max_damage = 0
    best_weapon = None
    for item in inventory:
        try:
            if item.damage > max_damage:
                best_weapon = item
                max_damage = item.damage
        except AttributeError:
            pass
    return best_weapon

play()
