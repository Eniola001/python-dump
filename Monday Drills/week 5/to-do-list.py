# Problem
# Build a small command-line to-do list. The user should be able to add a task, view all tasks, remove a task, or quit the program.
# Display a menu repeatedly until the user chooses to quit. Number tasks when displaying them so the user can select which task to remove.

# Examples
# Menu choices: add, view, remove, quit
# Example flow: add “Study Python” → view tasks → remove task 1 → quit

# Constraints
# Store tasks in a list.
# Use a loop and if / elif / else to handle menu choices.
# Handle an empty list when viewing or removing tasks.
# Do not import libraries.

# What This Tests
# Lists, loops, input, conditionals, indexing, and combining concepts in a mini project.
# Notes / concepts to review: (Remember to write your weakness it if you have one)


running = True
tasks = []

while running:
    print("\nTo add a task (Enter 1) \nTo view tasks (Enter 2) \nTo remove tasks (Enter 3) \nTo quit (Enter Quit)")
    menu = input("Enter your choice: ").lower()
    
    if menu == "1":
        task = input("Enter a task: ")
        tasks.append(task)
    elif menu == "2":
        if len(tasks) == 0:
            print("Your task list is empty")
        else:
            task_number = 0
            print("Your Tasks")
            for task in tasks:
                task_number += 1
                print(f"{task_number}. {task}")
    elif menu == "3":
        remove = int(input("Enter the number of the task you want to remove: ")) - 1
        if remove < 0 or remove > len(tasks) - 1:
            print("Invalid task number!")
        else:
            tasks.pop(remove)
            print(f"Task {remove + 1} deleted!")
    elif menu == "quit":
        running = False
    else:
        print("Invalid Input! Try again.")
