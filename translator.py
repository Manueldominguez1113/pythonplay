import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Notebook
import requests

class Translator(tk.Tk):
    def translate(self, target_lang = "es", text = None):
        print("Translating...")

        if not text:
            text = self.english_entry.get(1.0, tk.END)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=\"en\"&tl={target_lang}&dt=t&q={text}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            print(response.json())
            self.spanish_translation.set(response.json()[0][0][0])
            messagebox.showinfo("translated", "translation complete.")
        except Exception as e:
            print(str(e))
            messagebox.showerror("translation error", str(e))

    def __init__(self):
        super().__init__()
        self.title("Translator")
        self.Notebook = Notebook(self)
        self.Notebook.pack(fill=tk.BOTH, expand=1)

        english_tab = tk.Frame(self.Notebook)
        self.english_entry = tk.Text(english_tab)
        self.english_entry.pack(side=tk.TOP, expand=1)

        self.translate_button = tk.Button(english_tab, text="Translate",
                                         command=self.translate
                                         )
        self.translate_button.pack(side= tk.BOTTOM, fill=tk.X, expand=1)
        self.Notebook.add(english_tab, text="English")

        spanish_tab = tk.Frame(self.Notebook)
        self.Notebook.add(spanish_tab, text="Spanish")
        self.spanish_translation = tk.StringVar(spanish_tab)
        self.spanish_translation.set("No Translation..")
        self.spanish_label = tk.Label(spanish_tab, textvariable=self.spanish_translation)
        self.spanish_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == '__main__':
    translator = Translator()
    translator.mainloop()