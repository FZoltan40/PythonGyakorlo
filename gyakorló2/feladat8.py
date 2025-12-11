"""
8. feladat – OOP: BankAccount osztály
Készíts egy BankAccount osztályt:
attribútumok: név, egyenleg

metódusok: deposit(), withdraw(), get_balance()
Hozz létre két bankszámla objektumot, és teszteld.
"""

class BankAccount:
    def __init__(self,nev,egyenleg=0):
        self.name = nev
        self.balance = egyenleg

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Nincs elég fedezet.")
    
    def get_balance(self):
       return self.balance

account1 = BankAccount("zoli")
account2 = BankAccount("kata")

account1.deposit(7200)
account1.withdraw(200)
account1.deposit(200000)
account1.withdraw(200000000)

account2.deposit(17200)
account2.withdraw(2300)


print(f"{account1.name} -{ account1.get_balance()}")
print(f"{account2.name} -{ account2.get_balance()}")