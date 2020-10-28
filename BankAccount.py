class BankAccount:

    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance


    def deposit(self, amount):
        print(f"Current balance: ${self.balance}")
        self.balance += amount
        print(f"Amount Deposited: ${amount}")
        print(f"New balance: ${self.balance}")
        return self.balance

    def withdraw(self, amount):
        print(f"Current balance: ${self.balance}")
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

    def add_interest(self):
        print(f"Current balance: ${self.balance}")
        interest = self.balance * 0.00083
        self.balance += interest
        print(f"Interest: ${interest}")
        print(f"New balance: ${self.balance}")

    def print_receipt(self):
        account_num_to_string = str(self.account_number)

        print(f"\n {self.full_name}")
        print(f"Account number: ****{account_num_to_string[-4:]}")
        print(f"Routing number: {self.routing_number}")
        print(f"Balance: ${self.balance}")
    

person1 = BankAccount("Jackie", 11111111, 1111111111, 100) 
person2 = BankAccount("Ben", 22222222, 22222222, 200)
person3 = BankAccount("Jeremiah", 33333333, 33333333, 300)

# person1.deposit(int(input("Input deposit amount: ")))
# person1.withdraw(int(input("Input withdrawal amount: ")))
# person1.get_balance()
# person1.add_interest()
person1.print_receipt()