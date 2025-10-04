print("Welcome to the Python ATM!")
pin = "1234"  # Stored PIN
balance = 1000.00

entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin == pin:
    print("\nLogin successful!")
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Your current balance is: ${balance:.2f}")
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: $"))
            if amount > 0 and amount <= balance:
                balance -= amount
                print(f"Withdrawal successful. New balance: ${balance:.2f}")
            else:
                print("Invalid amount or insufficient funds.")
        elif choice == '3':
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                balance += amount
                print(f"Deposit successful. New balance: ${balance:.2f}")
            else:
                print("Invalid deposit amount.")
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Incorrect PIN. Access denied.")