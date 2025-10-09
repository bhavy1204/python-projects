import json
import os

DATA_FILE = "expenses.json"

# Load data if file exists
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save data to file
def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

# Add a new expense
def add_expense(expenses):
    try:
        name = input("Enter expense name: ").strip()
        category = input("Enter category (e.g. Food, Travel, etc.): ").strip()
        amount = float(input("Enter amount: ₹"))
        expenses.append({"name": name, "category": category, "amount": amount})
        save_expenses(expenses)
        print(f"✅ Expense '{name}' added successfully!")
    except ValueError:
        print("⚠️ Invalid input. Please enter a valid number for amount.")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- All Expenses ---")
    total = 0
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['name']} - {exp['category']} - ₹{exp['amount']}")
        total += exp['amount']
    print(f"--------------------\nTotal Spent: ₹{total}\n")

# View total expenses by category
def view_by_category(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Expenses by Category ---")
    categories = {}
    for exp in expenses:
        categories[exp["category"]] = categories.get(exp["category"], 0) + exp["amount"]
    for cat, total in categories.items():
        print(f"{cat}: ₹{total}")
    print("-----------------------------")

# Main program loop
def main():
    expenses = load_expenses()
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            print("💾 Saving and exiting. Goodbye!")
            save_expenses(expenses)
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
