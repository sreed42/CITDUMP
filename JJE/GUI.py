from player import Player
import world
from tkinter import *

class GUI():

    def __init__(self, master):

        root.geometry("2000x1000")
        root.title("Escape from Mansion!")
        Text = Text(height=50, width=100)
        world.parse_world_dsl()
        self.player = Player()

        Button1 = Button(root, text="North", command=self.move_northgui)
        Button2 = Button(root, text="South", command=self.player.move_southgui)
        Button3 = Button(root, text="East", command=self.player.move_eastgui)
        Button4 = Button(root, text="West", command=self.player.move_westgui)
        Button5 = Button(root, text="Heal",)
        Button6 = Button(root, text="Inventory")
        Button7 = Button(root, text="Attack")

        Text.pack(side=LEFT, expand=1)
        Button1.pack(side=RIGHT, padx=10)
        Button2.pack(side=RIGHT, padx=10)
        Button3.pack(side=RIGHT, padx=10)
        Button4.pack(side=RIGHT, padx=10)
        Button5.pack(side=RIGHT, padx=10)
        Button6.pack(side=RIGHT, padx=10)
        Button7.pack(side=RIGHT, padx=10)

    def move_northgui(self):
        self.player.move_north()
        self.refresh()

    def move_southgui(self):
        self.player.move_south()
        self.refresh()

    def move_eastgui(self):
        self.player.move_east()
        self.refresh()

    def move_westgui(self):
        self.player.move_west()
        self.refresh()

    def refresh(self):
        room = world.tile_at(self.player.x, self.player.y)
        print(room.intro_text())
        room.modify_player(Player)
        if not self.player.is_alive():
            print("Your journey has been cut short!")

root = Tk()

GUI = GUI(root)

root.mainloop()

