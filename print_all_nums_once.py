# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# Make an emptry list
num_list = []

# Ask for user input
for ask in range(1, 11):
    num = float(input(f"Enter number {ask}: "))
    # Append inputs into the list
    num_list.append(num)

# Make another list for non-unique numbers
non_uniq = []

# Make another list for unique numbers
uniq = []

# Filter out the unique and not unique
for numbers in num_list:
    if num_list.count(numbers) == 1:
        uniq.append(numbers)
        
# Print the numbers