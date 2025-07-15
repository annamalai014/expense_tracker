import json
import os

# File to store expenses
FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc.): ")
    amount = float(input("Enter amount: ₹"))
    expenses.append({"date": date, "category": category, "amount": amount})
    save_expenses(expenses)
    print("✅ Expense added!")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    print("\n📒 Your Expenses:")
    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | ₹{exp['amount']}")
    print()

# Show total expenses
def total_expense(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Spent: ₹{total}\n")

# Main program
def main():
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expense(expenses)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
