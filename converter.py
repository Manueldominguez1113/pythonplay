from pytube import YouTube
import tkinter as tk

class App:
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("YouTube Converter")
        self.root.geometry("500x300")
        self.build_gui()
        self.root.mainloop()

    def build_gui(self):
        title = tk.Label(self.root, text="Hello! Welcome to DZ's private Youtube-to-MP3 downloader")
        title.grid(column=2, row=0, columnspan=3)

        input_label = tk.Label(self.root, text="Enter YouTube URL")
        input_label.grid(column=1, row=2)

        url = tk.StringVar()
        input = tk.Entry(self.root, textvariable=url)
        input.focus()

        input.grid(column=2, row=2)

        # make button to begin, and bind Return key to button function.




if __name__ == '__main__':
    App()