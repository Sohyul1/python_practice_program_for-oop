# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# Make an empty list
num_list = []

# Ask for user input
for ask in range(1,11):
    num = float(input(f"Enter number {ask}: "))

# Make A list of duplicates
dup_nums = []

# Get the number that duplicates
if num_list not in dup_nums:
    dup_nums.append(num_list)
    
# Print the numbers that duplicates
print(dup_nums)
