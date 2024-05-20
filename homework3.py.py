# Print a welcome message
print("Welcome to the Personal Finance Tracker!")

# Create empty lists to store incomes and expenses
incomes = []
expenses = []

# Main loop for the finance tracker program
while True:
  
    # Prompt the user to choose an action
    action = input("Enter 'i' to add an income, 'e' to add an expense, 's' to view the financial summary, 'q' to quit: ")
    
    # Add an income
    if action == 'i':
        income = float(input("Enter the income amount: "))
        incomes.append(income)
        print("Income added successfully.")
    
    # Add an expense
    elif action == 'e':
        expense = float(input("Enter the expense amount: "))
        expenses.append(expense)
        print("Expense added successfully.")
    
    # View financial summary
    elif action == 's':
        if incomes or expenses:
            total_income = sum(incomes)
            total_expenses = sum(expenses)
            balance = total_income - total_expenses
            
            print("\nFinancial Summary:")
            print(f"Total Income: {total_income}")
            print(f"Total Expenses: {total_expenses}")
            print(f"Remaining Balance: {balance}\n")
        else:
            print("No incomes or expenses recorded yet.")
    
    # Quit the program
    elif action == 'q':
        print("Exiting the program. Goodbye!")
        break
    
    # Error handling for incorrect inputs
    else:
        print("Incorrect input, please try again.")