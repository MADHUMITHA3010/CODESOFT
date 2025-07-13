tasks = []

def show_menu():
    print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")
    elif choice == '2':
        print("\nTo-Do List:")
        for i, task in enumerate(tasks):
            status = "Done" if task["done"] else "Pending"
            print(f"{i + 1}. {task['task']} [{status}]")
    elif choice == '3':
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
