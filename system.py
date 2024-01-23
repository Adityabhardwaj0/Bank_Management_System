from bank import Bank
bank = Bank()
while True:
    print("1. Open account")
    print("2. Close account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check balance")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter your name: ")
        balance = float(input("Enter your initial balance: "))
        account = bank.open_account(name, balance)
        print("Account opened successfully. Your account number is", id(account))
    elif choice == "2":
        account_id = int(input("Enter your account number: "))
        account = next((a for a in bank.accounts if id(a) == account_id), None)
        if account:
            bank.close_account(account)
            print("Account closed successfully.")
        else:
            print("Error: Account not found")
    elif choice == "3":
        account_id = int(input("Enter your account number: "))
        account = next((a for a in bank.accounts if id(a) == account_id), None)
        if account:
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
            print("Deposit successful. Your new balance is", account.check_balance())
        else:
            print("Error: Account not found")
    elif choice == "4":
        account_id = int(input("Enter your account number: "))
        account = next((a for a in bank.accounts if id(a) == account_id), None)
        if account:
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
            print("Withdrawal successful. Your new balance is", account.check_balance())
        else:
            print("Error: Account not found")
    elif choice == "5":
        account_id = int(input("Enter your account number: "))
        account = next((a for a in bank.accounts if id(a) == account_id), None)
        if account:
            print("Your balance is", account.check_balance())
        else:
            print("Error: Account not found")
    elif choice == "6":
        break
    else:
        print("Invalid choice")
