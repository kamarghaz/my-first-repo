# Simple To-Do List

tasks = []

while True:
    print("\n==== To-Do List ====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print(f"Added: {task}")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for idx, t in enumerate(tasks, start=1):
                status = "✔" if t["done"] else "✘"
                print(f"{idx}. [{status}] {t['task']}")

    elif choice == "3":
        num = int(input("Enter task number to mark as done: "))
        if 0 < num <= len(tasks):
            tasks[num-1]["done"] = True
            print(f"Marked task {num} as done.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please select 1-4.")
