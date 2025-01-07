import tkinter as tk
import quizloader

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.current_question_index = 0
        self.build_gui()
        self.root.geometry("500x300")
        self.root.mainloop()


    def start(self):
        self.questions = quizloader.get_questions("quiz.csv")
        current_question = self.questions[self.current_question_index][0]
        self.ques_label = tk.Label(self.root, text=current_question)
        self.ques_label.grid(row=2, column=3)
    def next(self):
        print("Hello World")

    def build_gui(self):
        self.questions_container = tk.Frame(self.root)
        self.questions_container.grid(column=0, row=1)

        self.questions_label = tk.Label(self.questions_container, text="Questions")
        self.questions_label.grid(column=0, row=0)

        self.buttons_container = tk.Frame(self.root)
        self.buttons_container.grid(column=0, row=3)
        self.start_button = tk.Button(self.buttons_container, text="Start", command=self.start)
        self.start_button.grid()

        self.next_con = tk.Frame(self.root)
        self.next_con.grid(column=3, row=4)

        self.next_button = tk.Button(self.next_con, text="Next", command=self.next)
        self.next_button.grid()

if __name__ == '__main__':
    App()