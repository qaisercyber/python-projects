import json
from datetime import datetime

FILE_NAME = "expenses.json"


# ------------------ Load Expenses ------------------
def load_expenses():

    try:
        with open(FILE_NAME, "r") as file:
            content = file.read().strip()
            if not content:
                return []

            data = json.loads(content)

            # Ensure correct structure
            if isinstance(data, list):
                clean_data = []
                for item in data:
                    if isinstance(item, dict):
                        clean_data.append(item)
                return clean_data

            return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []


# ------------------ Save Expenses ------------------
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# ------------------ Add Expense ------------------
def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print(" Amount must be a number.")
        return

    category = input("Enter category (Food, Travel, etc): ").strip()
    description = input("Enter description: ").strip()

    expense = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses = load_expenses()   # ALWAYS list
    expenses.append(expense)     # SAFE
    save_expenses(expenses)

    print("Expense added successfully.")


# ------------------ Monthly Summary ------------------
def monthly_summary():
    month = input("Enter the month (YYYY-MM): ").strip()

    expenses = load_expenses()
    total = 0

    print("\n MONTHLY EXPENSE SUMMARY")
    print("-" * 45)

    found = False

    for expense in expenses:
        # Extra safety (never crashes)
        if not isinstance(expense, dict):
            continue

        if expense.get("date", "").startswith(month):
            print(
                f"{expense.get('date')} | "
                f"{expense.get('category')} | "
                f"{expense.get('amount')}"
            )
            total += expense.get("amount", 0)
            found = True

    print("-" * 45)

    if found:
        print(f"Total Expense for {month}: {total}")
    else:
        print(f"No expenses found for {month}.")


# ------------------ Menu ------------------
def show_menu():
    print("\nPERSONAL EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. Monthly Summary")
    print("3. Exit")


# ------------------ Main Program ------------------
def main():
    while True:
        show_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            monthly_summary()
        elif choice == "3":
            print("Exiting Expense Tracker.")
            break
        else:
            print(" Invalid choice.")


# ------------------ Entry Point ------------------
if __name__ == "__main__":
    main()
