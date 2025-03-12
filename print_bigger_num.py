# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

# Ask for user input
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# Determine the bigger number
bigger = max(num1, num2)

# Print the bigger number
print(f"{bigger} is the bigger number.")