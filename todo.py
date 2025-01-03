import tkinter as tk

class TaskList(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.title("Task List")
        instructions = tk.Label(self, text="please enter tasks into the list", bg="black", fg="white")
        self.tasks.append(instructions)

        for task in self.tasks:
            task.pack(fill=tk.BOTH, expand=True)
        self.addTask = tk.Text(self, height=4)
        self.addTask.pack(fill= tk.X)
        self.addTask.focus_set()

        self.bind("<Return>", self.add_task)
        self.colors = [
            {
                "bg": "black",
                "fg": "white",
            },
            {
                "bg": "grey",
                "fg": "light green",
            }
        ]

    def add_task(self, event=None):
        task_text = self.addTask.get(1.0, tk.END).strip()

        task_label = tk.Label(self, text=task_text)
        _, task_color = divmod(len(self.tasks), 2)

        task_label.configure(bg=self.colors[task_color]["bg"], fg=self.colors[task_color]["fg"])
        task_label.pack(fill=tk.BOTH, expand=True)
        self.tasks.append(task_label)
        self.addTask.delete(1.0, tk.END)

if __name__ == "__main__":
    app = TaskList()
    app.mainloop()