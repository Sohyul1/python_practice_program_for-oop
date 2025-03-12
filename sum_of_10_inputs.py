# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# Create an empty list for storing nums
nums = []

# Ask for user input
for ask in range (1,11):
    ans = float(input(f"Enter number{ask}:"))
    # Add the inputs in the empty list
    nums.append(ans)

# Get the sum of all of them
sum(nums)

# Print the sum 
print(sum)