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
        self.start_button.pack_forget()
        self.next_button = tk.Button(self.next_con, text="Next", command=self.next)
        self.next_button.pack()
        self.questions = quizloader.get_questions("quiz.csv")
        current_question = self.get_question()
        self.questions_label.config(text=current_question + "?")
        options =  self.get_options()
        for option, index in zip(options, range(len(options))):
            self.option_buttons.append(tk.Radiobutton(
                self.questions_container,
                text=option,
                value=index+1,
                variable=self.user_answer,
            ))
            self.option_buttons[-1].pack()

    def get_question(self):
        return self.questions[self.current_question_index][0]

    def get_options(self):
        return self.questions[self.current_question_index][1:len(self.questions)+1]

    def check_answer(self):
        if str(self.user_answer.get()) == self.questions[self.current_question_index][-1]:
            self.score.set(self.score.get() + 1)

    def next(self):
        if self.current_question_index < len(self.questions):
            self.check_answer()
            self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            next_q = self.get_question()
            self.questions_label.config(text = next_q +"?")

            next_options = self.get_options()
            for option_button, option, index in zip(self.option_buttons, next_options,
                                                    range(len(next_options))
                                                    ):
                option_button.config(text=option, value = index+1)

    def build_gui(self):
        self.questions_container = tk.Frame(self.root)
        self.questions_container.pack()

        self.questions_label = tk.Label(self.questions_container, text="Questions")
        self.questions_label.pack()

        self.buttons_container = tk.Frame(self.root)
        self.buttons_container.pack()
        self.start_button = tk.Button(self.buttons_container, text="Start", command=self.start)
        self.start_button.pack()

        self.next_con = tk.Frame(self.root)
        self.next_con.pack()


        self.option_buttons = []
        self.user_answer = tk.IntVar()

        self.score = tk.IntVar()
        self.score.set(0)
        self.score_label = tk.Label(self.root, textvariable = self.score,
                                    font = ("Helvetica", 20))
        self.score_label.pack()

if __name__ == '__main__':
    App()