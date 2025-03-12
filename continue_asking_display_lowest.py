# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

# Make a count varibale
count = 1

# Make a list 
num_list = []

# Ask user for input (break if input is invalid)
while True:
    try:
        number = float(input(f"Enter Number {count}: "))
        count += 1
# Append the numbers in the list
# Print the lowest