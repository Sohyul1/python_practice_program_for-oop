# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display "Unique" after input when the inputted number don't have duplicate. 
# Display "Duplicate" after input when the inputted number have duplicate.

# Make a list and count
count = 0
nums = []
# Input a number until the input is invalid
while True:
    try:
        number = float(input(f"Enter Number {count}: "))
        count += 1
# Print Unique if it don't have duplicate
# Print Duplicate if it is