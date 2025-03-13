# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

# Make an empty list
num_list = []
count = 1
# Ask for user input
while True:
    try:
        num = float(input(f"Enter number {count}: "))
        count += 1
        num_list.append(num)
    except ValueError:
        break

# Determine the highest number 
highest_num = max(num_list)

# Print the highest number
print(highest_num)
