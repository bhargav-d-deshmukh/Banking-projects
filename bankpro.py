class BankAccount:
    
    
    
    
    
    
    
    
    
    
    
    def __init__(self, account_number, name, pin, balance=0):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +₹{amount:.2f}")
            print(f"₹{amount:.2f} deposited successfully.")
        else:
            print("Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -₹{amount:.2f}")
            print(f"₹{amount:.2f} withdrawn successfully.")

    def credit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Credit: +₹{amount:.2f}")
            print(f"₹{amount:.2f} credited successfully.")
        else:
            print("Amount must be greater than 0.")

    def debit(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Debit: -₹{amount:.2f}")
            print(f"₹{amount:.2f} debited successfully.")

    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance:.2f}")

    def account_details(self):
        print("\n========== ACCOUNT DETAILS ==========")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.name}")
        print(f"Balance        : ₹{self.balance:.2f}")
        print("=====================================")

    def transaction_history(self):
        print("\n========== TRANSACTION HISTORY ==========")

        if not self.transactions:
            print("No transactions yet.")
        else:
            for i, transaction in enumerate(self.transactions, 1):
                print(f"{i}. {transaction}")

        print("==========================================")


class BankingSystem:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001

    def create_account(self):
        print("\n========== CREATE ACCOUNT ==========")

        name = input("Enter your name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        pin = input("Create a 4-digit PIN: ")

        if len(pin) != 4 or not pin.isdigit():
            print("PIN must contain exactly 4 digits.")
            return

        try:
            initial_deposit = float(input("Enter initial deposit: ₹"))

            if initial_deposit < 0:
                print("Deposit cannot be negative.")
                return

        except ValueError:
            print("Please enter a valid amount.")
            return

        account_number = self.next_account_number
        self.next_account_number += 1

        account = BankAccount(
            account_number,
            name,
            pin,
            initial_deposit
        )

        if initial_deposit > 0:
            account.transactions.append(
                f"Initial Deposit: +₹{initial_deposit:.2f}"
            )

        self.accounts[account_number] = account

        print("\nAccount created successfully!")
        print(f"Your Account Number is: {account_number}")

    def login(self):
        print("\n========== LOGIN ==========")

        try:
            account_number = int(input("Enter account number: "))
        except ValueError:
            print("Invalid account number.")
            return None

        if account_number not in self.accounts:
            print("Account not found.")
            return None

        pin = input("Enter PIN: ")

        account = self.accounts[account_number]

        if pin == account.pin:
            print(f"\nWelcome, {account.name}!")
            return account
        else:
            print("Incorrect PIN.")
            return None

    def account_menu(self, account):
        while True:
            print("\n================================")
            print("          BANK MENU")
            print("================================")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Credit")
            print("4. Debit")
            print("5. Check Balance")
            print("6. Account Details")
            print("7. Transaction History")
            print("8. Logout")
            print("================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    amount = float(input("Enter deposit amount: ₹"))
                    account.deposit(amount)
                except ValueError:
                    print("Please enter a valid amount.")

            elif choice == "2":
                try:
                    amount = float(input("Enter withdrawal amount: ₹"))
                    account.withdraw(amount)
                except ValueError:
                    print("Please enter a valid amount.")

            elif choice == "3":
                try:
                    amount = float(input("Enter credit amount: ₹"))
                    account.credit(amount)
                except ValueError:
                    print("Please enter a valid amount.")

            elif choice == "4":
                try:
                    amount = float(input("Enter debit amount: ₹"))
                    account.debit(amount)
                except ValueError:
                    print("Please enter a valid amount.")

            elif choice == "5":
                account.check_balance()

            elif choice == "6":
                account.account_details()

            elif choice == "7":
                account.transaction_history()

            elif choice == "8":
                print("Logged out successfully.")
                break

            else:
                print("Invalid choice. Please try again.")

    def run(self):
        while True:
            print("\n")
            print("========================================")
            print("       WELCOME TO VIJAY BANK")
            print("========================================")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            print("========================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()

            elif choice == "2":
                account = self.login()

                if account:
                    self.account_menu(account)

            elif choice == "3":
                print("\nThank you for using VIJAY Bank!")
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    bank = BankingSystem()
    bank.run()

