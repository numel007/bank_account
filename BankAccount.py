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

    # def withdraw(self, amount):


    # def get_balance(self):


    # def add_interest(self, balance):


    # def print_receipt(self):
    

person1 = BankAccount("Jackie", 1, 11, 100) 
person2 = BankAccount("Ben", 2, 22, 200 )
person3 = BankAccount("Jeremiah", 3, 33, 300)

print(person1.balance)

person1.deposit(int(input("Input deposit amount here: ")))

print(person1.balance)