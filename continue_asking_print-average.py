# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

# Make an empty list
num_list = []
count = 1

# Ask for user input
while True:
    try:
        num = float(input(f"Enter number {count}; "))
        count += 1
    except ValueError:
        break

# Get the average

# Print the average 
