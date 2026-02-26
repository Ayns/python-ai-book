# Chapter 7 - Exercise Solutions

# 1. BankAccount with transaction history
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []
    
    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited ${amount:.2f}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return
        self.balance -= amount
        self.history.append(f"Withdrew ${amount:.2f}")
    
    def show_history(self):
        for entry in self.history:
            print(f"  {entry}")
        print(f"  Balance: ${self.balance:.2f}")

acc = BankAccount("Ayyanar", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.show_history()

# 2. Shape hierarchy with area calculation
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(f"{type(s).__name__}: area = {s.area():.2f}")
