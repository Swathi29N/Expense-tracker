import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    """Create the CSV file with headers if it does not exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    """Add a new expense to the CSV file."""
    date = input("Enter date (YYYY-MM-DD) or press Enter for today's date: ")

    if date.strip() == "":
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, f"{amount:.2f}"])

    print("Expense added successfully!")


def view_expenses():
    """Display all recorded expenses."""
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("\nNo expenses recorded.")
        return

    print("\n" + "=" * 75)
    print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>15}")
    print("=" * 75)

    for expense in expenses:
        print(
            f"{expense['Date']:<15}"
            f"{expense['Category']:<15}"
            f"{expense['Description']:<25}"
            f"₹{float(expense['Amount']):>13.2f}"
        )

    print("=" * 75)


def calculate_total():
    """Calculate and display the total amount spent."""
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        total = sum(float(row["Amount"]) for row in reader)

    print(f"\nTotal Expenses: ₹{total:.2f}")


def category_summary():
    """Display total expenses for each category."""
    summary = {}

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            summary[category] = summary.get(category, 0) + amount

    if not summary:
        print("\nNo expenses recorded.")
        return

    print("\nCategory-wise Expenses")
    print("-" * 35)

    for category, amount in summary.items():
        print(f"{category:<20} ₹{amount:.2f}")


def search_expenses():
    """Search expenses by category or description."""
    keyword = input("\nEnter category or description to search: ").strip().lower()

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        results = [
            row for row in reader
            if keyword in row["Category"].lower()
            or keyword in row["Description"].lower()
        ]

    if not results:
        print("No matching expenses found.")
        return

    print("\nMatching Expenses")
    print("=" * 75)
    print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>15}")
    print("=" * 75)

    for expense in results:
        print(
            f"{expense['Date']:<15}"
            f"{expense['Category']:<15}"
            f"{expense['Description']:<25}"
            f"₹{float(expense['Amount']):>13.2f}"
        )

    print("=" * 75)


def main():
    """Main menu for the Expense Tracker."""
    initialize_file()

    while True:
        print("\n" + "=" * 40)
        print("        EXPENSE TRACKER")
        print("=" * 40)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Category-wise Summary")
        print("5. Search Expenses")
        print("6. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            search_expenses()

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
