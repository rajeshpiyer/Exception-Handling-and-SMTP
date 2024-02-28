#BANK SIMULATION
class NegativeBalance(Exception):

    def __init__(self, balance: int):
        self.balance = balance
    def __str__(self) -> str:
        return f"\n!!!Negative Balance not allowed!!!\nCurrent Balance : {self.balance}"
    
class BankAccount:
    
    def __init__(self) -> None:
        self.balance = 2500
    def withdraw(self):
        amount = int(input("Enter amount to withdraw : "))
        if (self.balance-amount)>=0:
            self.balance -= amount
        else:
            raise NegativeBalance(self.balance)
    def showBalance(self):
        print("\nCurrent Balance : ",self.balance)
    def getBalance(self):
        return self.balance

account = BankAccount()
while(int(account.getBalance())>0):
    try:
        account.showBalance()
        account.withdraw()
    except NegativeBalance as e:
        print(e)
        continue
account.showBalance()
print("Cannot withdraw anymore!")


    
