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
        print("\n")
        return self.balance

    def withdraw(self, amount):
        print(f"Current balance: ${self.balance}")
        if amount > self.balance:
            self.balance -= 10
            print(f"Insufficient funds to withdraw ${amount}")
            print(f"Overcharge fee: $10")
            print(f"New balance: ${self.balance}")
            print("\n")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")
            print(f"New Balance: ${self.balance}")
            print("\n")

    def get_balance(self):
        print(f"You currently have an account balance of: ${self.balance}")
        print("\n")
        return self.balance

    def add_interest(self):
        print(f"Current balance: ${self.balance}")
        interest = self.balance * 0.00083
        self.balance += interest
        print(f"Interest: ${interest}")
        print(f"New balance: ${self.balance}")
        print("\n")

    def print_receipt(self):
        account_num_to_string = str(self.account_number)

        print(f"{self.full_name}")
        print(f"Account number: ****{account_num_to_string[-4:]}")
        print(f"Routing number: {self.routing_number}")
        print(f"Balance: ${self.balance}")
        print("\n")
    

person1 = BankAccount("Jackie", 11111111, 1111111111, 100) 
person2 = BankAccount("Ben", 22222222, 22222222, 200)
person3 = BankAccount("Jeremiah", 33333333, 33333333, 300)

person1.deposit(int(input(f"Hello {person1.full_name}. Input deposit amount: $")))
person1.withdraw(int(input(f" Hello {person1.full_name}. Input withdrawal amount: $")))
person1.get_balance()
person1.add_interest()
person1.print_receipt()

person2.deposit(int(input(f"Hello {person2.full_name}. Input deposit amount: $")))
person2.withdraw(int(input(f" Hello {person2.full_name}. Input withdrawal amount: $")))
person2.get_balance()
person2.add_interest()
person2.print_receipt()

person3.deposit(int(input(f"Hello {person3.full_name}. Input deposit amount: $")))
person3.withdraw(int(input(f" Hello {person3.full_name}. Input withdrawal amount: $")))
person3.get_balance()
person3.add_interest()
person3.print_receipt()