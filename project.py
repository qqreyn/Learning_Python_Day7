print("Task Manager")

task_manager = []

while True:
    print("\nWhat do you want to do?")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Mark task done (remove by number)")
    print("4. Count tasks")
    print("5. Clear all")
    print("6. Exit")
    
    try:
        choice = int(input("Choose option (1-6): "))
    except ValueError:
        print("Please enter a number from 1 to 6.")
        continue

    if choice == 1:
        task = input("Enter task you want to add:")
        task_manager.append(task)
        print(task, "was added to task manager")

    elif choice == 2:
        if not task_manager:
            print("No tasks in the manager.")
        else:
            print("Current tasks:")
            for i, task in enumerate(task_manager, start=1):
                print(i, task)
    
    elif choice == 3:
        try:
            mark_done = int(input("What task number you want to mark as done: "))
                if 1 <= mark_done <= len(task_manager):
                    print(task_manager[mark_done - 1], "Task marked as done")
                    task_manager.pop(mark_done - 1)
                else:
                    ("Invalid task number")
        except ValueError:
            print("Please enter a valid number")
    
    elif choice == 4:
        print(len(task_manager), "Tasks in the manager")
    
    elif choice == 5:
        print("Are you sure? y/n")
        confirm = input()
        if confirm == "y":
            task_manager.clear()
            print("Task manager cleared!")
    
    elif choice == 6:
        print("Goodbye")
        break

    else:
        print("Invalid option")