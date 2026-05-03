class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    def presentation(self):
    
        return f"Hello, my name is {self.name}, have {self.age} years and job is {self.job}! "
I = Person("Ana Carolina", 27, "developer in cybersecurity")
print(I.presentation())
        


class Animal:
    def __init__(self, type, name, collor):
        self.type = type
        self.name = name
        self.collor = collor
    def complements(self):
        return F'{self.type} / {self.name} / {self.collor}'    
a = Animal('cat', 'sun', 'orange') 
b = Animal('dog',  'Bob', 'black')   
print(a.complements())
print(b.complements())


class Shape:
    def calculate_area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
R = Rectangle(10,2)
print(R.calculate_area())
    
class Bank_account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    def deposit(self, value):
        if value <=0:
            return "ValueError: Deposit must be positive."
        self.balance += value
        return self.balance
    def withdraw(self, value):
        if value > self.balance:
         return "Insufficient funds."
        self.balance -= value
        return self.balance
    def show(self):
        return f"Holder: {self.holder} / balance: R$ {self.balance:.2f}"
conta = Bank_account("Ana", 150.00) 
print(conta.deposit(50))
print(conta.withdraw(30))
print(conta.show())   
        
    