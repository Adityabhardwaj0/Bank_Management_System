class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def open_account(self, name, balance):
        account = Account(name, balance)
        self.add_account(account)
        return account

    def close_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
        else:
            print("Error: Account not found")

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Error: Insufficient funds")
        else:
            self.balance -= amount

    def check_balance(self):
        return self.balance

