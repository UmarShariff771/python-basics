# Problem 1: Bank Account
# Create a base class Bank account with attributes like account_number, balance, and methods like deposit()
# and withdraw(). Inherit from this class to create subclass SavingsAccount and CurrentAccount. The SavingsAccount
# should have an interest rate and a method to calculate interest. The CurrentAccount should have a minimum
# balance requirement.
# Implement encapsulation to protect the account balance and ensure that with drawl cannot exceed the balance
# or minimum balance requirement.

# Base class for common bank account features
class Bank_account():
    # Constructor to initialize account number and balance
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    # Method to access the private balance
    def get_balance(self):
        return self.__balance

    # Method to print the current balance
    def account_balance(self):
        print(f"The account balance is {self.__balance}")

    # Method to deposit money into account
    def deposit(self, amount):
        self.__balance += amount

    # Method to withdraw money from account
    def withdraw(self, amount):
        self.__balance -= amount


# Method to withdraw money from account
class Savings_account(Bank_account):
    # Interest rate for savings account
    interest_rate = 8

    # Constructor calling parent constructor and updates the rate in super class
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.rate = 0

    # Method to calculate interest for a given amount
    def calculate_interest(self, amount):
        rate = amount * (self.interest_rate / 100)
        print(f"The interest rate for the amount is {rate}")
        super().deposit(rate)
        return rate

    # Overriding withdraw method to prevent withdrawing more than balance
    def withdraw(self, amount):
        remaining_balance = self.get_balance() - amount
        if (remaining_balance < 0):
            print(f"Cannot withdraw {amount} since the balance is {self.get_balance()}")
        else:
            super().withdraw(amount)


# Current account class inheriting from Bank_account
class Current_Account(Bank_account):
    # Minimum balance that must be maintained
    minimum_balance = 1000

    # Overriding withdraw method to check minimum balance condition
    def withdraw(self, amount):
        remaining_balance = self.get_balance() - amount
        if (remaining_balance < self.minimum_balance):
            print(f"Cannot withdraw {amount} since the balance is {self.get_balance()}")
        else:
            super().withdraw(amount)


# Creating savings and current account objects
savings = Savings_account(1001, 5000)
current = Current_Account(2001, 6000)

# Checking initial balances
print("Initial Balances")
savings.account_balance()
current.account_balance()

# Depositing money into both accounts
print("\nDepositing Money")

savings.deposit(1000)
current.deposit(2000)

savings.account_balance()
current.account_balance()

# Applying interest to savings account
print("\nApplying Interest")

savings.calculate_interest(2000)
savings.account_balance()

# Applying interest again
print("\nApplying Interest")

savings.calculate_interest(2000)
savings.account_balance()

# Trying to withdraw more than available balance
savings.withdraw(100000)

# Withdrawing from current account
print("\nCurrent Account Withdrawal")

current.withdraw(2000)
current.account_balance()

# Another withdrawal from current account
print("\nCurrent Account Withdrawal")

current.withdraw(2000)
current.account_balance()

# Trying to violate minimum balance rule
current.withdraw(7000)

# Final balances after all operations
print("\nFinal Balances")

savings.account_balance()
current.account_balance()
