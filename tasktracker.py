# -------------------------
# Decorator
# -------------------------
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Running '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished '{func.__name__}'.")
        return result

    return wrapper


# -------------------------
# Task storage
# -------------------------
tasks = []


# -------------------------
# Functions
# -------------------------
@log_action
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task added: {task}")


@log_action
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


@log_action
def clear_tasks():
    tasks.clear()
    print("All tasks cleared.")


# -------------------------
# Menu loop
# -------------------------
def show_menu():
    print("\n--- Task Tracker Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Clear Tasks")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        clear_tasks()
    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please select 1-4.")
