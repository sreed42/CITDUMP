import main

from tkinter import *

root = Tk()
root.geometry("2000x1000")
root.title("Escape from Mansion")
Text = Text(height=50, width=100)
Text.pack(side=LEFT)

button1 = Button(root, text="North")
button2 = Button(root, text="South")
button3 = Button(root, text="East")
button4 = Button(root, text="West")

button5 = Button(root, text="Print Inventory")
button6 = Button(root, text="Attack")
button7 = Button(root, text="Heal")

Text.pack(side=LEFT, expand=1)
button1.pack(side=RIGHT)
button2.pack(side=RIGHT)
button3.pack(side=RIGHT)
button4.pack(side=RIGHT)
button5.pack(side=RIGHT)
button6.pack(side=RIGHT)
button7.pack(side=RIGHT)

root.mainloop()
