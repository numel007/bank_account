class BankAccount:

    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 10
            print(f"Insufficient funds to withdraw ${amount}")
            print(f"Overcharge fee: $10")
            print(f"New balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")
            print(f"New Balance: ${self.balance}")

    def get_balance(self):
        print(f"You currently have an account balance of: ${self.balance}")
        return self.balance

    # def add_interest(self, balance):


    # def print_receipt(self):
    

person1 = BankAccount("Jackie", 1, 11, 100) 
person2 = BankAccount("Ben", 2, 22, 200)
person3 = BankAccount("Jeremiah", 3, 33, 300)

print(person2.balance)

person2.withdraw(int(input("Input withdrawal amount here: ")))

person2.get_balance()