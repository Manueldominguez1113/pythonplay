import tkinter as tk
from tkinter import ttk
import random

def exit(root):
    root.destroy()
def randstring(root):
    new_title= ""
    for i in range(5):
        new_title = chr(ord("A") + random.randrange(26))
        root.title(new_title)

def on_click(label):
    label.config(text="Button has been clicked!")

def main():
    root = tk.Tk()

    frame = ttk.Frame(root, padding="500 300")
    frame.grid()

    label = ttk.Label(frame, text="Hello world!")
    label.grid()

    button = ttk.Button(frame, text="Roll title name")
    button.grid()
    button["command"] = lambda: randstring(root)

    exitgr = ttk.Button(frame, text="exit")
    exitgr.grid()

    exitgr["command"] = lambda: exit(root)

    button2 = tk.Button(frame, text="click me!")
    button2.grid()
    button2["command"] = lambda: on_click(label)
    root.mainloop()

main()