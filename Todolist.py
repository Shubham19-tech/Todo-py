import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        # Task input field and buttons
        self.task_input_field = tk.Entry(self.root, width=30)
        self.task_input_field.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=40, height=10)
        self.task_listbox.pack(pady=20)

    def add_task(self):
        task = self.task_input_field.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_input_field.delete(0, tk.END)  # Clear input field
        else:
            messagebox.showwarning("Input Error", "Please enter a task!")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
