# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

# Make an empty list
odd_list = []

# Ask for user input
for ask in range(1, 11):
    ans = float(input(f"Enter number {ask}: "))
    # Filter out the odd numbers 
    if ans % 2 == 1:
        # Append to the list if odd
        odd_list.append(ans)

# Get the total numbers of odd
total = len(odd_list)

# Print the odd nums 
print(total)