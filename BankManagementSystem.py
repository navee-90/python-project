class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient funds.")

    def display_account(self):
        print(f"Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder, account_number, initial_balance=0):
        account = BankAccount(account_holder, account_number, initial_balance)
        self.accounts[account_number] = account
        print(f"Account for {account_holder} created successfully.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

# Example Usage
bank = Bank()
bank.create_account("Mahesh", "1001", 500)
bank.create_account("Raghava", "1002", 1000)

alice_account = bank.get_account("1001")
bob_account = bank.get_account("1002")

alice_account.deposit(200)
bob_account.withdraw(500)
alice_account.display_account()
bob_account.display_account()
