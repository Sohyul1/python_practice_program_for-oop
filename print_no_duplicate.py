# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Make an empty list 
num_list = []

# Ask for user input 
for ask in range(1, 11):
    nums = float(input(f"Enter number {ask}: "))
    # Append the number in the list 
    num_list.append(nums)

# Make another lis for unique numbers
unique_list = []

# Filter out numbers that appear only once 
if num_list.count(nums)== 1:
    unique_list.append(nums)
    # Print the numbers that appear only once
    print(unique_list)