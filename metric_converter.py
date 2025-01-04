import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

root.title("Metric Converter")

main = ttk.Frame(root, padding="300 300")
main.grid()

feet_value = tk.StringVar()
meters_value = tk.StringVar()

feet_label = ttk.Label(main, text="Feet")
feet_label.grid(column=0, row=1)

feet_display = ttk.Label(main, textvariable=feet_value)
feet_display.grid(column=1, row=1)

meters_label = ttk.Label(main, text="meters")
meters_label.grid(column=0, row=0)

meters_input = ttk.Entry(main, textvariable=meters_value)
meters_input.grid(column=1, row=0)
meters_input.focus()

def convert(event):
    try:
        value = float(meters_input.get())
        feet_value.set("%.3f" % (value * 3.28084))
    except ValueError:
        print("Invalid entry")

convert_button = ttk.Button(main, text="Convert", command = convert)
convert_button.grid(column=0, row=2, columnspan=2)

root.bind("<Return>", convert)

root.mainloop()