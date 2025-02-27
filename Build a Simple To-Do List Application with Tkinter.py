import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")


def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass


def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = listbox_tasks.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")


# Setup the main application window
root = tk.Tk()
root.title("To-Do List")

# Create the task list frame
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Entry widget to add tasks
entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=5)

# Buttons for task operations
button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack(pady=2)

button_delete_task = tk.Button(root, text="Delete Selected Task", width=48, command=delete_task)
button_delete_task.pack(pady=2)

button_save_tasks = tk.Button(root, text="Save Tasks", width=48, command=save_tasks)
button_save_tasks.pack(pady=2)

button_load_tasks = tk.Button(root, text="Load Tasks", width=48, command=load_tasks)
button_load_tasks.pack(pady=2)

root.mainloop()


# Why? This snippet creates a simple To-Do List GUI using Tkinter. It demonstrates basic GUI components—such as
# Listbox, Entry, and Buttons—and integrates file operations for saving and loading tasks. It’s a practical way to
# get started with desktop app development in Python!
