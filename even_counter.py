# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

# Make an empty list
even_list = []

# Ask for user input
for ask in range(1, 11):
    answer = float(input(f"Enter number {ask}: "))
    # Filter out the even nums
    if answer % 2 == 0:
        even_list.append(answer)
        
# Get the total number of even
total = len(even_list)

# Print the total
print(total)