class ATM:
    def __init__(self, balance):
        self.balance = balance
        self.pin = "1234"  # Default PIN

    def check_balance(self):
        print(f"Your balance is: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"You have withdrawn ${amount}. New balance is ${self.balance}.")

    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited ${amount}. New balance is ${self.balance}.")

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("Your PIN has been successfully changed.")

def atm_interface():
    atm = ATM(1000)  # Initial balance is $1000
    print("Welcome to the ATM Interface")
    
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change PIN")
        print("5. Exit")
        
        choice = input("Please choose an option (1-5): ")
        
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to deposit: "))
            atm.deposit(amount)
        elif choice == '4':
            new_pin = input("Enter the new PIN: ")
            atm.change_pin(new_pin)
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the ATM interface
atm_interface()
