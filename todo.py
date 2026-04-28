tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    
    for i, t in enumerate(tasks):
        status = "Done" if t["done"] else "Not Done"
        print(f"{i+1}. {t['task']} [{status}]")
    print()

def mark_done():
    view_tasks()
    num = int(input("Enter task number to mark as done: "))
    if 0 < num <= len(tasks):
        tasks[num-1]["done"] = True
        print("Task marked as done!\n")
    else:
        print("Invalid number\n")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    if 0 < num <= len(tasks):
        tasks.pop(num-1)
        print("Task deleted!\n")
    else:
        print("Invalid number\n")

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice\n")