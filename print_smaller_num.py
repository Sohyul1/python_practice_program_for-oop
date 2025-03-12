# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

# Ask for user input
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# Determine the smaller number
small_num = min(num1, num2)

# Print the number
print(small_num)