# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

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

# Get the average
average = sum(num_list) / len(num_list)

# Print the average 
print(f"{average:.2f}")  