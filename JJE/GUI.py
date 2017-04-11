import main

from Tkinter import *


root = Tk()
root.title("Escape from Mansion!")

root.mainloop()

NorthButton = Button(root, text="North")
SouthButton = Button(root, text="South")
EastButton =  Button(root, text="East")
WestButton =  Button(root, text="West")

HealButton =  Button(root, text="Heal")
InventoryButton = Button(root, text="Inventory")
AttackButton = Button(root, text="Attack")

Text = Entry(root)
listbox = Listbox(root)

Text.pack()
NorthButton.pack()
SouthButton.pack()
EastButton.pack()
WestButton.pack()
HealButton.pack()
InventoryButton.pack()
AttackButton.pack()
