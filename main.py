import tkinter as tk


def read_items():
    with open('items.txt', 'r') as file:
        stream = file.read()
        todos = stream.split('/')
    return todos


def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)


def add_task_file():
    task = task_entry.get()
    with open('items.txt','a') as file:
        file.write('/'+task)
    task_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)


def complete_task():
    selected_task_indices = task_listbox.curselection()
    for index in selected_task_indices[::-1]:  # Reverse to avoid index shifting issues
        task_listbox.delete(index)


# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Create an entry widget for new tasks
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Create a button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Create button to save task in file
add_task2file = tk.Button(root, text="Save New Task", command=add_task_file)
add_task2file.pack(pady=5)

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.MULTIPLE)
task_listbox.pack(pady=10)

# Create a button to delete tasks
complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack(pady=5)

# Show tasks in file
items = read_items()
for current_item in items:
    task_listbox.insert(tk.END, current_item)

# Start the Tkinter event loop
root.mainloop()