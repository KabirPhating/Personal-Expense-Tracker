
expenses = []

while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append({"name": name, "amount": amount})
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            for expense in expenses:
                print(expense["name"], "-", expense["amount"])

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print("Total spending:", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")
