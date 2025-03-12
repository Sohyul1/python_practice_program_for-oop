# Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

# Make an empty list
odd_list = []

# Make a counter
count = 1

# Make the while loop
while count <= 100:
    # Filter out the odd numbers
    if count % 2 == 1:
        # Append odd numbers in the list
        odd_list.append(count)
    
    count += 1

# Print the odd numbers
print(odd_list)