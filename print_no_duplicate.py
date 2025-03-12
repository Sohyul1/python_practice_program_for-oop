# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Make an empty list 
unique_num = []

# Ask for user input 
for ask in range(1, 11):
    nums = float(input(f"Enter number {ask}: "))
    # Append the number in the list 
    unique_num.append(nums)

# Filter out numbers that appear only once 
# Print the numbers that appear only once