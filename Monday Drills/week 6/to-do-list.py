# Problem
# Build a small command-line to-do list.
# The user should be able to add a task, view all tasks (numbered), remove a task by its number, mark a task as done, and quit the program. 
# Display a menu repeatedly until the user chooses to quit. When viewing, show each task’s number, its text, and whether it is done (e.g., [ ] or [x]).

# Examples
# Menu: add | view | remove | done | quit

# > add Study Python
# Task added.
# > add Practice loops
# Task added.
# > view
# 1. [ ] Study Python
# 2. [ ] Practice loops
# > done 1
# Task 1 marked as done.
# > view
# 1. [x] Study Python
# 2. [ ] Practice loops
# > remove 2
# Task removed.
# > view
# 1. [x] Study Python
# > quit
# Goodbye!


print("Menu: add | view | remove | done | quit")
running = True
tasks = []

while running:
    action = list(map(str, input("> ").split()))
    if action:
        action[0] = action[0].lower()
        
    task_undone = "[ ]"
    task_done = "[x]"

    if not action or action[0] not in ["add", "view", "remove", "done", "quit"]:
        print("Invalid Input!")

    elif action[0] == "add":
        task = task_undone
        for i in range(1, len(action)):
            task += " " + action[i]
        tasks.append(task)
        print("Task added.")

    elif action[0] == "view":
        if not tasks:
            print("No tasks!")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif action[0] == "remove":
        index_removed = int(action[-1]) - 1
        tasks.pop(index_removed)
        print("Task removed.")

    elif action[0] == "done":
        index_done = int(action[-1]) - 1
        tasks[index_done] = f"{task_done} {tasks[index_done][4:]}"
        print(f"Task {index_done + 1} marked as done.")

    elif action[0] == "quit":
        print("Goodbye!")
        running = False