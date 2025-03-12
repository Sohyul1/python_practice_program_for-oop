# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# Make a count variable
count = 1

# Ask user for the 1st numer
num1 = float(input("Enter number 1: "))

# Use while loop to ask for the remaining numbers
while count < 10:
    rest_nums = float(input(f"Enter number {count + 1}: "))
    count += 1

    # Get the difference
    num1 -= rest_nums

# Print the difference
print(num1)

