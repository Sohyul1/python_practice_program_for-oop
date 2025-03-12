# Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

# Ask for user input 
num1 = float(input("Enter the base number: "))
num2 = float(input("Enter the exponent: "))

# Get the nth-square of the first number (second num is the exponent)
result = num1 ** num2

# Print the value
print(result)