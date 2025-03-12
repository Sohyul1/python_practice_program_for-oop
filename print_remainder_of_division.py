# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

# Ask for user input
num1 = float(input("Enter the dividend: "))
num2 = float(input("Enter the divisor: "))

# Get the reaminder (use %)
quotient_remdr = num1 % num2

# Print the reaminder
print(quotient_remdr)