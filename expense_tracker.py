from datetime import datetime

class FinanceManager:
    def __init__(self):
        self.balance = 0
        self.transactions = []  # List to store income and expense transactions

    def add_income(self, amount):
        self.balance += amount
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(("Income", amount, timestamp))
        print(f"Income of ₹{amount} added on {timestamp}.")
        print(f"Current Balance: ₹{self.balance}")

    def add_expense(self, amount, category):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.transactions.append(("Expense", amount, category, timestamp))
            print(f"Expense of ₹{amount} deducted on {timestamp}.")
            print(f"Current Balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def show_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            if transaction[0] == "Income":
                print(f"Income of ₹{transaction[1]} on {transaction[2]}")
            else:
                print(f"Expense of ₹{transaction[1]} in {transaction[2]} on {transaction[3]}")

def main():
    manager = FinanceManager()

    while True:
        print("\nFinance Manager")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Check Balance")
        print("4. Show Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            manager.add_income(amount)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            manager.add_expense(amount, category)
        elif choice == '3':
            manager.check_balance()
        elif choice == '4':
            manager.show_transactions()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!!. Please try again.")


if __name__ == "__main__":
    main()
