# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# Make a for loop
for num in range(0,101):
    # Filter out the number ending with 0 and 5
    if num % 10 != 0 and num % 5 != 0:
        # Print the rest of the numbers
        print(num)
