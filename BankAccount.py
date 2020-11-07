from random import randint

# BankAccount class creation
class BankAccount:

    # BankAccount instance variables
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = 0

    # ------------------ Methods ------------------

    def deposit(self, amount):
        """Deposit user-defined amount"""
        print(f"Current balance: ${self.balance}")
        self.balance += amount
        print(f"Amount Deposited: ${amount}")
        self.balance -= atmUsageFee
        print(f"ATM fee: ${atmUsageFee}")
        print(f"New balance: ${self.balance}")
        print("\n")
        return self.balance

    def withdraw(self, amount):
        """Withdraw user-defined amount or subtract $10 on overdraft"""
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
            self.balance -= atmUsageFee
            print(f"ATM fee: ${atmUsageFee}")
            print(f"New Balance: ${self.balance}")
            print("\n")

    def get_balance(self):
        """Returns user's current balance"""
        print(f"You currently have an account balance of: ${self.balance}")
        print("\n")
        return self.balance

    def add_interest(self):
        """Adds 1 month's interest to user's balance, calculated from current balance at rate of 0.00083"""
        print(f"Current balance: ${self.balance}")
        interest = self.balance * 0.00083
        self.balance += round(interest, 2)
        print(f"Interest: ${round(interest, 2)}")
        print(f"New balance: ${self.balance}")
        print("\n")

    def print_receipt(self):
        """Print's user's account information, censors first 4 digits of acc. number"""
        account_num_to_string = str(self.account_number)

        print(f"Account Holder: {self.full_name}")
        print(f"Account number: ****{account_num_to_string[-4:]}")
        print(f"Routing number: {self.routing_number}")
        print(f"Balance: ${self.balance}")
        print("\n")


# Called to create an 8 digit account number
def createAccNum():
    acc_num = ""
    for i in range(8):
        acc_num += str(randint(0, 9))
    return int(acc_num)

# ------------------ ATM Functions ------------------

# Deposit function for atmOptions
def deposit(user, acc_num):
    """Selects from list of known users and runs deposit method"""
    while True:
        if user == Tom.full_name and acc_num == Tom.account_number:
            Tom.deposit(
                float(input(f"Hello {Tom.full_name}. Input deposit amount: $")))
            break
        elif user == Bob.full_name and acc_num == Bob.account_number:
            Bob.deposit(
                float(input(f"Hello {Bob.full_name}. Input deposit amount: $")))
            break
        elif user == Hubert.full_name and acc_num == Hubert.account_number:
            Hubert.deposit(
                float(input(f"Hello {Hubert.full_name}. Input deposit amount: $")))
            break
        else:
            print("No matching user found")
            continue
    print("Exiting ATM")

# Withdraw function for atmOptions
def withdraw(user, acc_num):
    """Selects from list of known users and runs withdrawal method"""
    while True:
        if user == Tom.full_name and acc_num == Tom.account_number:
            Tom.withdraw(
                float(input(f"Hello {Tom.full_name}. Input withdrawal amount: $")))
            break
        elif user == Bob.full_name and acc_num == Bob.account_number:
            Bob.withdraw(
                float(input(f"Hello {Bob.full_name}. Input withdrawal amount: $")))
            break
        elif user == Hubert.full_name and acc_num == Hubert.account_number:
            Hubert.withdraw(
                float(input(f"Hello {Hubert.full_name}. Input withdrawal amount: $")))
            break
        else:
            print("No matching user found")
            continue
    print("Exiting ATM")

# Balance function for atmOptions
def balance(user, acc_num):
    """Selects from list of known users and runs get_balance method"""
    while True:
        if user == Tom.full_name and acc_num == Tom.account_number:
            Tom.get_balance()
            break
        elif user == Bob.full_name and acc_num == Bob.account_number:
            Bob.get_balance()
            break
        elif user == Hubert.full_name and acc_num == Hubert.account_number:
            Hubert.get_balance()
            break
        else:
            print("No matching user found")
            continue
    print("Exiting ATM")

# Account details function for atmOptions
def accDetails(user, acc_num):
    """Selects from list of known users and runs get_balance method"""
    while True:
        if user == Tom.full_name and acc_num == Tom.account_number:
            Tom.print_receipt()
            break
        elif user == Bob.full_name and acc_num == Bob.account_number:
            Bob.print_receipt()
            break
        elif user == Hubert.full_name and acc_num == Hubert.account_number:
            Hubert.print_receipt()
            break
        else:
            print("No matching user found")
            continue
    print("Exiting ATM")

# Decides which function to call on the input account
def atmOptions():
    while True:
        option_selected = int(input(
            "Enter an option\n\n1) Deposit\n2) Withdraw\n3) Current Balance\n4) Account Details\n\nOption selected: "))
        if option_selected == 1:
            print("Deposit selected")
            print("--------------------\n")
            deposit(input("Input name: "), int(
                input("Input account number: ")))
            break
        elif option_selected == 2:
            print("Withdrawal selected")
            print("--------------------\n")
            withdraw(input("Input name: "), int(
                input("Input account number: ")))
            break
        elif option_selected == 3:
            print("Current Balance selected")
            print("--------------------\n")
            balance(input("Input name: "), int(
                input("Input account number: ")))
            break
        elif option_selected == 4:
            print("Account details selected")
            print("--------------------\n")
            accDetails(input("Input name: "), int(
                input("Input account number: ")))
            break
        else:
            print("Invalid option")
            print("--------------------\n")
            continue


# ------------------ Testing methods ------------------

# Initialize 3 users with predefined BankAccount variables
Tom = BankAccount("Tom Hanks", createAccNum(), 1111111111, 0)
Bob = BankAccount("Bob Ross", createAccNum(), 22222222, 0)
Hubert = BankAccount("Hubert Blaine Wolfeschlegel­steinhausen­bergerdorff­vor­altern­waren­gewissenhaft­schafers­wessen­schafts­waren­wohl­gefuttern­und­sorgfaltigkeit­beschutzen­vor­angreifen­durch­ihr­raubgierig­fiends Sr.", createAccNum(), 33333333, 0)
atmUsageFee = 2

# Give each account a starting balance so test methods and functions can be called
Tom.balance = 100
Bob.balance = 200
Hubert.balance = 300


# Experimenting below with try/except in below method calls. I am aware of the poor implementation.

#Tom method calls
try:
    Tom.deposit(float(input(f"Hello {Tom.full_name}. Input deposit amount: $")))
    Tom.withdraw(float(input(f"Hello {Tom.full_name}. Input withdrawal amount: $")))
    Tom.get_balance()
    Tom.add_interest()
    Tom.print_receipt()
except ValueError:
    print("Invalid input")

# # Bob method calls
# try:
#     Bob.deposit(float(input(f"Hello {Bob.full_name}. Input deposit amount: $")))
#     Bob.withdraw(float(input(f"Hello {Bob.full_name}. Input withdrawal amount: $")))
#     Bob.get_balance()
#     Bob.add_interest()
#     Bob.print_receipt()
# except ValueError:
#     print("Invalid input")

# # Hubert method calls
# try:
#     Hubert.deposit(float(input(f"Hello {Hubert.full_name}. Input deposit amount: $")))
#     Hubert.withdraw(float(input(f"Hello {Hubert.full_name}. Input withdrawal amount: $")))
#     Hubert.get_balance()
#     Hubert.add_interest()
#     Hubert.print_receipt()
# except ValueError:
#     print("Invalid input")


# Run ATM simulation - uncomment to use
# print(Bob.account_number)
# atmOptions()