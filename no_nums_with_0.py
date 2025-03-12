# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

# Make a for loop
for nums in range(0,101):
    # filter out the numbers with 0
    if nums % 2 != 0 and nums % 5 != 0:
        # Print all the numbers
        print(nums)