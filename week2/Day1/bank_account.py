#Create a class BankAccount.
# Attributes: owner, balance (default = 0).
# Methods:
# deposit(amount) → adds to balance.
# withdraw(amount) → subtracts if balance is enough, else print "Insufficient funds".
# Create an account and test deposits/withdrawals.

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount
        return f"After deposit of {amount},new balance is {self.balance}"
    def withdraw(self,amount):
        if amount > self.balance:
           return "Insufficient Balance!"
        else:
            self.balance-=amount
            return f"New balance is {amount}"
owner1 = BankAccount("Ali",1000)
owner2 = BankAccount("Alice",500)

    
print(owner1.deposit(100))
print(owner2.withdraw(600))
print(owner2.deposit(100))