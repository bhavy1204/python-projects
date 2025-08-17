import json
import os
from datetime import date

FILE = "habits.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_habit(habits):
    name = input("Enter habit name: ").strip()
    if name not in habits:
        habits[name] = {"streak": 0, "last_done": ""}
        print(f"Habit '{name}' added.")
    else:
        print("Habit already exists.")
    return habits

def mark_done(habits):
    name = input("Which habit did you complete? ").strip()
    today = str(date.today())
    if name in habits:
        if habits[name]["last_done"] == today:
            print("Already marked for today!")
        else:
            habits[name]["streak"] += 1
            habits[name]["last_done"] = today
            print(f"Marked '{name}' as done! Streak: {habits[name]['streak']}")
    else:
        print("Habit not found.")
    return habits

def view_habits(habits):
    if not habits:
        print("No habits yet.")
    for name, info in habits.items():
        print(f"{name}: {info['streak']} days streak (last done: {info['last_done']})")

def main():
    habits = load_data()
    while True:
        print("\nHabit Tracker")
        print("1. Add Habit\n2. Mark Done\n3. View Habits\n4. Quit")
        choice = input("Choose: ")
        if choice == "1":
            habits = add_habit(habits)
        elif choice == "2":
            habits = mark_done(habits)
        elif choice == "3":
            view_habits(habits)
        elif choice == "4":
            save_data(habits)
            print("Goodbye! Keep building habits.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
