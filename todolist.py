

tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks.extend(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        save_tasks()
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")

def view_tasks():
    if not tasks:
        print("No tasks available!")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if tasks:
        try:
            n = int(input("Enter task number to remove: "))
            if 1 <= n <= len(tasks):
                print("Removed:", tasks.pop(n - 1))
                save_tasks()
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    load_tasks()
    while True:
        print("\n--- TO-DO LIST APP ---")
        print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Thank you for using the app!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

