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
<<<<<<< HEAD:print_the_nums_once.py
        
# Print the numbers
=======
    else:
        non_uniq.append(numbers)

# Print the numbers
print(uniq, non_uniq)
>>>>>>> 00d93a6 (made the non uniq part and print the output, non uniq part still need adjustments):print_all_nums_once.py
