# Example: Variables in Python
# This file demonstrates how to create and use variables

# Creating variables
myCardPin = 1234
userName = "PythonLearner"
accountBalance = 1500.50
isActive = True

# Printing variables
print("=== Bank Account Information ===")
print("PIN:", myCardPin)
print("Username:", userName)
print("Balance: $" + str(accountBalance))
print("Account Active:", isActive)

# You can change variable values
accountBalance = accountBalance - 100
print("\nAfter withdrawal:")
print("New Balance: $" + str(accountBalance))

