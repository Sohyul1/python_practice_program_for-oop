# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

# Make an empty list
num_list = []

# make a count variable
count = 1

# Ask for user input
while True:
    try:
        num = float(input(f"Enter number {count}: "))
        num_list.append(num)
        count += 1

    except ValueError:
        break

# Use sort to arrange the 
arranged = num_list.sort()
for num in num_list:
# Print arranged numbers
    print(num)