# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# Make an empty list
num_list = []

# Ask for user input
while True:
    try:
        num = float(input("Enter number: "))
        num_list.append(num)
        
    except ValueError:
        break

# Make a dictionary
num_counts = {}
        
# Count how many times the number appeared
for nums in num_list:
    if nums in num_counts:
        num_counts[nums] += 1
    else:
        num_counts[nums] = 1
        
# Get the most duplicated number
max_count = 0
most_dupli = None
for nums in num_counts:
        if num_counts[nums] > max_count:
            most_dupli = nums
            max_count = num_counts[nums]

# Print the number
print(f"{most_dupli} occured {max_count} times.")



