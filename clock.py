import tkinter as tk
import time
current_time_previous = "0"

root = tk.Tk()
root.title("Clock")
root.geometry("500x200")
clock = tk.Label(root, text="Clock",font=("Helvetica", 50), pady= 50)
clock.pack()

def tick():
    global current_time_previous

    # current_time = time.strftime("%H:%M:%S")
    current_time = time.strftime("%I:%M:%S %p")


    if current_time_previous != current_time:
        current_time_previous = current_time
        clock.config(text=current_time)
    clock.after(1000, tick)

tick()
root.mainloop()