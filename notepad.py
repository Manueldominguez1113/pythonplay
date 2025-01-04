import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

root = tk.Tk()

root.title("Notepad")

textarea = ScrolledText(root)
textarea.pack(fill=tk.BOTH, expand=True)

menu = Menu(root)
file= Menu(menu, tearoff=0)

def Open():
    root.filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select File",
        filetypes=(("txt files", "*.txt"), ("all files", "*.*"))
    )
    openfile = open(root.filename)
    textarea.insert("end", openfile.read())

def Save():
    print("Save")
def SaveAs():
    saveFile = filedialog.asksaveasfile(mode="w",defaultextension=".txt", initialdir="/", title="ssssssssssssacve File")
    if saveFile:
        textToSave = textarea.get("1.0", tk.END)

        try:
            saveFile.write(textToSave)
            saveFile.close()
        except Exception as e:
            messagebox.showerror("Error", f"error saving file: {e}")

def Quit():
    message = messagebox.askquestion("WAIT!", "do you want to save???")
    if message == "yes":
        SaveAs()
    else:
        root.destroy()
file.add_command(label="Open", command=Open)
file.add_command(label="Save", command=Save)
file.add_command(label="Save As", command=SaveAs)
file.add_separator()
file.add_command(label="Exit", command=Quit)
menu.add_cascade(label="File", menu=file)

root.config(menu=menu)


root.mainloop()
