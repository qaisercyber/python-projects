import bank

def show_menu():
    print("Welcome to Banking System")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show balance")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice:")
        if choice == "1":
            amount = float(input("Enter amount:"))
            success , message = bank.deposit(amount)
            print(success)
            print(message)
        if choice == "2":
            amount = float(input("Enter amount:"))
            success , message = bank.withdraw(amount)
            print(success)
            print(message)
        if choice == "3":
            print(f" Your balance is {bank.show_balance()}")

        if choice == "4":
            print("Thank you for your time and goodbye")
            break
        else:
            print("Please enter a valid choice")

if __name__ == "__main__":
    main()