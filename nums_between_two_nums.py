# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# Ask for user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Print numbers between the two numbers
if num1 < num2:
    for number in range(num1 + 1, num2):
        print(number)
else:
    for number in range(num2 + 1, num1):
        print(number)