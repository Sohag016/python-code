# Class and Object
class Animal:
    def __init__(self, name, species):
        self.name = name       # Attribute
        self.species = species  # Attribute

    def make_sound(self):       # Method
        return "Some sound"

    def info(self):
        print(f"{self.name} is a {self.species}")

# Inheritance
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Calling the parent class constructor
        self.breed = breed

    def make_sound(self):  # Overriding method
        return "Bark"

    def info(self):  # Method Overriding
        print(f"{self.name} is a {self.breed} breed dog.")

# Polymorphism
class Cat(Animal):
    def make_sound(self):  # Overriding method
        return "Meow"

# Encapsulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner            # Public attribute
        self.__balance = balance       # Private attribute (Encapsulated)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid or insufficient balance.")

    def get_balance(self):  # Public method to access private attribute
        return self.__balance

# Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract Base Class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Usage of Classes and Objects

# Creating Objects
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Cat")

# Polymorphism in Action
animals = [dog, cat]
for animal in animals:
    print(f"{animal.name} says {animal.make_sound()}")

# Accessing Methods
dog.info()
cat.info()

# Encapsulation in Action
account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
print(f"Final balance: {account.get_balance()}")

# Working with Abstraction
rectangle = Rectangle(3, 4)
circle = Circle(5)

print(f"Rectangle area: {rectangle.area()}, perimeter: {rectangle.perimeter()}")
print(f"Circle area: {circle.area()}, perimeter: {circle.perimeter()}")
