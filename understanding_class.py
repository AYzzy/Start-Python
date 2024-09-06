from decimal import Decimal
class Akant:

    # constructors: are special method in a class that initialize the instance attribute of a class
    def __init__(self, name: str, pin: str, balance: Decimal = 0.00,number : int = 0) -> None:
        self.name = name.upper()
        self.pin = pin
        self.balance = balance
        self.number = number

    def deposit(self, amount):
        if amount < Decimal(0.00):
            raise ValueError(f"Amount deposited is an invalid")
        self.balance += amount
        return self.balance

    def withdraw(self, amount, pin):
        if Decimal(0.00) > amount > self.balance:
            raise ValueError(f"Insufficient funds to withdraw or Insufficient balance")
        if not pin == self.pin:
            raise ValueError(f"Incorrect Pin")
        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"Name: {self.name}, Pin: {self.pin}"

    def check_balance(self, pin):
        return None