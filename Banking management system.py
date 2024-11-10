# A dictionary to store accounts by account number
accounts = {}

while True:
    print("\nBanking System Menu:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Delete Account")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Create Account
        name = input("Enter account holder's name: ")
        acc_number = input("Enter account number: ")

        if acc_number in accounts:
            print("Account number already exists.")
        else:
            initial_deposit = float(input("Enter initial deposit amount: "))
            # Store account details in the dictionary with account number as key
            accounts[acc_number] = {'name': name, 'balance': initial_deposit}
            print(f"Account created successfully for {name}.")

    elif choice == "2":
        # Deposit money
        acc_number = input("Enter account number: ")
        if acc_number in accounts:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                accounts[acc_number]['balance'] += amount
                print(f"Deposited: ${amount}. New balance: ${accounts[acc_number]['balance']}")
            else:
                print("Deposit amount must be positive.")
        else:
            print("Account not found.")

    elif choice == "3":
        # Withdraw money
        acc_number = input("Enter account number: ")
        if acc_number in accounts:
            amount = float(input("Enter withdrawal amount: "))
            if amount > 0 and amount <= accounts[acc_number]['balance']:
                accounts[acc_number]['balance'] -= amount
                print(f"Withdrew: ${amount}. New balance: ${accounts[acc_number]['balance']}")
            elif amount > accounts[acc_number]['balance']:
                print("Insufficient balance.")
            else:
                print("Withdrawal amount must be positive.")
        else:
            print("Account not found.")

    elif choice == "4":
        # Check balance
        acc_number = input("Enter account number: ")
        if acc_number in accounts:
            print(f"Current balance: ${accounts[acc_number]['balance']}")
        else:
            print("Account not found.")

    elif choice == "5":
        # Delete account
        acc_number = input("Enter account number: ")
        if acc_number in accounts:
            del accounts[acc_number]
            print(f"Account {acc_number} has been deleted.")
        else:
            print("Account not found.")

    elif choice == "6":
        # Exit
        print("Exiting the banking system.")
        break

    else:
        print("Invalid choice. Please try again.")
