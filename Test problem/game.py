import random

# Rename the variable to avoid conflict with the random module
random_number = random.randint(1, 100)
print(random_number)

while True:
    new = int(input("Enter number: "))

    if new == random_number:
        print("Yes, you guessed it!")
        break 
    elif new < random_number:
        print("Too Low")
    else:
        print("Too High")
