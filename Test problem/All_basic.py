# Input-Output
print("Enter a number: ")
num = int(input())

# Operator and Math
squared = num ** 2
cubed = num ** 3
print(f"Square of {num} is {squared}")
print(f"Cube of {num} is {cubed}")

# Control Statement (if-else)
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Switch Case (Using Dictionary)
def switch_case(option):
    switcher = {
        1: "Option 1 selected.",
        2: "Option 2 selected.",
        3: "Option 3 selected."
    }
    return switcher.get(option, "Invalid option.")

print(switch_case(1))

# Loop and Series
print("First 5 natural numbers using loop:")
for i in range(1, 6):
    print(i)

# Pattern
print("Pattern using loop:")
for i in range(1, 6):
    print("*" * i)

# Array (List)
array = [1, 2, 3, 4, 5]
print(f"Array elements: {array}")

# String Manipulation
text = "hello"
reversed_text = text[::-1]
print(f"Original text: {text}")
print(f"Reversed text: {reversed_text}")

# Function and Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

fact = factorial(5)
print(f"Factorial of 5 is {fact}")

# File Handling
filename = "example.txt"
with open(filename, "w") as file:
    file.write("Hello, this is a test file.")
with open(filename, "r") as file:
    content = file.read()
    print(f"Content of file: {content}")

# Structure (Class)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

student = Student("John", 20)
student.display()

# Pointer (Using Reference)
def increment(value):
    value += 1
    return value

number = 10
number = increment(number)
print(f"Incremented value: {number}")
