import csv

def display_menu():
    print("Expense Tracker Menu")
    print("1. Add sample expenses")
    print("2. Display expenses")
    print("3. Exit")

def add_sample_expense(file_path):
    sample_expenses = [
        ["Date", "Description", "Amount"],
        ["21/05/2024", "Groceries", 50.00],
        ["22/05/2024", "Rent", 800.00],
        ["23/05/2024", "Utilities", 150.00],
        ["24/05/2024", "Transport", 40.00]
    ]

    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            for expense in sample_expenses:
                writer.writerow(expense)
        print("Sample expenses added successfully.")
    except IOError:
        print("An error occurred when writing to the file.")

def display_expenses(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            expenses = list(reader)
            if len(expenses) == 0:
                print("No expenses found.")
                return
        for row in expenses:
            print(','.join(row))
    except FileNotFoundError:
        print("No expenses found. Please add some expenses first.")
    except IOError:
        print("An error occurred while reading the file.")

def main():
    path = "expenses.csv"

    while True:
        display_menu()
        try:
            choice = int(input("Please enter your choice (1, 2, or 3): "))
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
            continue

        if choice == 1:
            add_sample_expense(path)
        elif choice == 2:
            display_expenses(path)
        elif choice == 3:
            print("Exiting expense tracker. Thank you!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()