import tkinter as tk
from tkinter import messagebox
from tkinter import font

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("500x430")
        self.tasks = []
        self.root.configure(bg="dark blue")

        self.heading_frame = tk.Frame(root, bg="black")
        self.heading_frame.pack(fill=tk.X)

        font_style = font.Font(size=12)

        self.task_label = tk.Label(self.heading_frame, text="Enter your task:", fg="black", bg="light blue", font=font_style)
        self.task_label.pack(side=tk.TOP)

        self.task_entry = tk.Entry(self.heading_frame, font=font_style)
        self.task_entry.pack(side=tk.BOTTOM)

        self.add_button = tk.Button(self.heading_frame, text="Add Task", command=self.add_task, font=font_style, bg="Blue",fg = "white")
        self.add_button.pack(side=tk.RIGHT)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=font_style)
        self.task_listbox.pack(pady=15)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task,fg="black", font=font_style, bg="light green")
        self.update_button.pack(side=tk.RIGHT)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, fg="black", bg="orange", font=font_style)
        self.delete_button.pack(side=tk.RIGHT)

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks, fg="black", bg="light yellow", font=font_style)
        self.save_button.pack(side=tk.LEFT)

        self.load_button = tk.Button(root, text="Open Saved Tasks", command=self.load_tasks, fg="black", bg="light yellow", font=font_style)
        self.load_button.pack(side=tk.LEFT)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.task_entry.get()
            if selected_task:
                self.tasks[selected_index[0]] = selected_task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index[0], selected_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a task to update.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index[0])

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                self.tasks = [task.strip() for task in tasks]
                self.task_listbox.delete(0, tk.END)
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            messagebox.showerror("Error", "No saved tasks found.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    todo_list.run()
