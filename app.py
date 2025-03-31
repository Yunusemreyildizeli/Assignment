print("SmartBudgetTracker initialized successfully")
app_version = "v0.1"
print(f"Running SmartBudgetTracker {app_version}")

# The following section will contain user input simulation
# This is a placeholder for future user interaction logic

# Simulate basic user input
user_name = input("Please enter your name: ")
user_balance = float(input("Enter your initial balance: "))

print(f"Welcome, {user_name}! Your starting balance is ${user_balance:.2f}")

# Simulate a single transaction input
transaction_type = input("Enter transaction type (income/expense): ").strip().lower()
amount = float(input("Enter transaction amount: "))
category = input("Enter transaction category: ")

print(f"Transaction recorded: {transaction_type} of ${amount:.2f} under '{category}' category.")

# Update balance based on transaction type
if transaction_type == "income":
    user_balance += amount
elif transaction_type == "expense":
    user_balance -= amount

print(f"Your updated balance is: ${user_balance:.2f}")

# Simulate a second transaction input
transaction_type_2 = input("Enter another transaction type (income/expense): ").strip().lower()
amount_2 = float(input("Enter the second transaction amount: "))
category_2 = input("Enter the second transaction category: ")

print(f"Transaction recorded: {transaction_type_2} of ${amount_2:.2f} under '{category_2}' category.")

# Update balance again
if transaction_type_2 == "income":
    user_balance += amount_2
elif transaction_type_2 == "expense":
    user_balance -= amount_2

print(f"Final balance after second transaction: ${user_balance:.2f}")

# Initialize transaction list
transactions = []