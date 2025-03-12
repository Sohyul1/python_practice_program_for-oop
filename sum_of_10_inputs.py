# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# Create an empty list for storing nums
nums_storage = []

# Ask for user input
for ask in range(1, 11):
    ans = float(input(f"Enter number {ask}: "))
    # Add the inputs in the empty list
    nums_storage.append(ans)

# Get the sum of all of them
total = sum(nums_storage)

# Print the sum 
print(total)