from tkinter import *

class Display(Frame):

    mGui = Tk()
    mGui.geometry("500x500-500-300")
    mGui.title("Haunted Mansion!")
    mlabel = Label(mGui,text = "You are locked in an abandoned mansion.\n"
                             "There are a few paths you can travel.\n"
                             "Can you survive?").pack()

if __name__ == '__main__':
  Display().mainloop()
