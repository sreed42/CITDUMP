import player
import world
from tkinter import *

root = Tk()
root.geometry("2000x1000")
root.title("Escape from Mansion!")


Button1 = Button(root, text="North")
Button2 = Button(root, text="South")
Button3 = Button(root, text="East")
Button4 = Button(root, text="West")
Button5 = Button(root, text="Heal")
Button6 = Button(root, text="Inventory")
Button7 = Button(root, text="Attack")


Button1.pack(side=RIGHT)
Button2.pack(side=RIGHT)
Button3.pack(side=RIGHT)
Button4.pack(side=RIGHT)
Button5.pack(side=RIGHT)
Button6.pack(side=RIGHT)
Button7.pack(side=RIGHT)

def move_northgui(self):
    self.move(dx=0, dy=-1)
    refresh()

def move_southgui(self):
    self.move(dx=0, dy=1)
    refresh()

def move_eastgui(self):
    self.move(dx=1, dy=0)
    refresh()

def move_westgui(self):
    self.move(dx=-1, dy=0)
    refresh()

def refresh():
    room = world.tile_at(player.x, player.y)
    print(room.intro_text())
    room.modify_player(player)
    if not player.is_alive():
        print("Your journey has been cut short!")


root.mainloop()
