from email.policy import default
from tkinter import *

root = Tk()
root.title("Form")
root.geometry("500x500")

fields = "Name", "Age", "Sex", "favorite color"
default_font = "helvetica", 20

def build_form(root, fields):
    entries = []
    for field in fields:
        frame = Frame(root)
        label = Label(frame, text=field, font=default_font, pady=20)
        entry = Entry(frame)
        label.pack(side=LEFT)
        frame.pack(side=TOP)
        entry.pack(side=RIGHT)
        entries.append((field, entry))
    return entries

entries = build_form(root, fields)

def print_form(entries):
    for entry in entries:
        print(f"{entry[0]}:{entry[1].get()}")

button = Button(root, text="Print", command=(lambda e = entries: print_form(e)), font=default_font)

button.pack(side=BOTTOM)
root.mainloop()