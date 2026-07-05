# Expense Tracker

total = 0

print("=== EXPENSE TRACKER ===")

while True:
    new_expense = float(input("Enter expense amount (0 to stop): "))

    if new_expense == 0:
        break

    total += new_expense

print("Total Spent: ₹", total)