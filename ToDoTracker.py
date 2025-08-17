import json, os

FILE = "todo.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks):
    task = input("Enter new task: ").strip()
    tasks.append({"task": task, "done": False})
    print(f"Task added: {task}")
    return tasks

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✘"
        print(f"{i}. [{status}] {t['task']}")

def complete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Mark which task done? #: ")) - 1
        tasks[idx]["done"] = True
        print("Task marked complete.")
    except:
        print("Invalid choice.")
    return tasks

def delete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Delete which task? #: ")) - 1
        removed = tasks.pop(idx)
        print(f"Deleted: {removed['task']}")
    except:
        print("Invalid choice.")
    return tasks

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do Manager")
        print("1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Quit")
        choice = input("Choose: ")
        if choice == "1": tasks = add_task(tasks)
        elif choice == "2": view_tasks(tasks)
        elif choice == "3": tasks = complete_task(tasks)
        elif choice == "4": tasks = delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye! Stay productive ✨")
            break
        else: print("Invalid option.")

if __name__ == "__main__":
    main()
