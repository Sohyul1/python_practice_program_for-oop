# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# Make an empty list
num_list = []

# Ask for user input
for ask in range(1, 11):
    num = float(input(f"Enter number {ask}: "))
    num_list.append(num)

# Make A list of duplicates
dup_nums = []

# Get the number that duplicates
for nums in num_list:
    if num_list.count(nums) > 1:
        dup_nums.append(nums)
    
# Print the numbers that duplicates
print(dup_nums)
