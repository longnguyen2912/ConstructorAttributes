class BankAccount:

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate= 0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            print(f"The balance that include interest: {self.balance}")
        return self
    
myAccount= BankAccount(0.2,100)
myAccount.deposit(2000).withdraw(1000).display_account_info().yield_interest()


