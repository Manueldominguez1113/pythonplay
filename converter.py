import os
from pathlib import Path
from pytubefix import YouTube

import tkinter as tk

class App:
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("YouTube Converter")
        self.root.geometry("500x150")
        self.build_gui()
        self.root.resizable(False, False)

        self.root.mainloop()

    def check_url(self, url, label):
        pass
        if label.cget("text") != "":
            label.config(text="")

        if url.get()== "":
            label.config(text="No url entered!!")
        elif "you" not in url.get():
            label.config(text="Enter a full youtube url!!")
        else:
            print("success! moving to conversion")
            self.conversion(url, label)

    def conversion(self, url, label):
        try:
            # setting up the url string
            yt = YouTube(url.get())
            # extracting the audio only
            video = yt.streams.filter(only_audio=True).first()
            # save location
            destination = str(Path.home()) + "/Downloads/"
            # download file
            outfile = video.download(output_path=destination)

            # renaming the fle to the video+mp3
            base, ext = os.path.splitext(outfile)
            new_file=base+".mp3"
            os.rename(outfile, new_file)

            label.config(text=f"{new_file} has been converted to mp3 and saved!")

        except Exception as e:
            label.config(text=e)

    def exit(self):
        self.root.destroy()

    def build_gui(self):
        title = tk.Label(self.root, text="Hello! Welcome to DZ's private Youtube-to-MP3 downloader")
        title.grid(column=2, row=0, columnspan=3)

        input_label = tk.Label(self.root, text="Enter full YouTube URL")
        input_label.grid(column=1, row=3)

        url = tk.StringVar()
        inputt = tk.Entry(self.root, textvariable=url)
        inputt.focus()

        inputt.grid(column=2, row=3)

        output_label = tk.Label(self.root, text="")
        output_label.grid(row=7, column=2)


        button_container = tk.Frame(self.root)
        button_container.grid(column=4, row=3)

        url_button = tk.Button(button_container, text="Convert", command=lambda: self.check_url(url, output_label))
        url_button.grid(ipadx=20, ipady=10)

        exit_container = tk.Frame(self.root)
        exit_container.grid(column=1, row=5, columnspan=6)
        exit_button = tk.Button(exit_container, text="Exit", command=self.exit)
        exit_button.grid(column=0,columnspan=5, ipadx=20, ipady=5)

        instructions_label = tk.Label(self.root, text="Tips: Press Enter to run, press Esc to quit")
        instructions_label.grid(column=2, row=6)




        self.root.bind("<Return>", lambda event: self.check_url(url,output_label))
        self.root.bind("<Escape>", lambda event : self.exit())


if __name__ == '__main__':
    App()
