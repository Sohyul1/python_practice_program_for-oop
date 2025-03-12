# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# Make an emptry list
num_list = []

# Ask for user input
for ask in range(1, 11):
    num = float(input(f"Enter number {ask}: "))
    # Append inputs into the list
    num_list.append(num)

# Make another list for unique numbers
uniq = []

# Filter out the unique and not unique
for numbers in num_list:
    if numbers not in uniq:
        uniq.append(numbers)

# Print the numbers
print(f"{uniq} are the unique numbers")

# Sir idk kung ano napindot ko kanina kung bakit naging ganon yung na push ko po
# This last push po ay I removed the non uniq list and then modifief the for loop so that once lang ma aappend yung nums, and then print
