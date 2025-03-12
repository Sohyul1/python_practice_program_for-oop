# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# Make an empty list
num_list = []

# Ask for user input
while True:
    try:
        num = float(input("Enter number: "))
        num_list.append(num)
        
        # Make a dictionary
        num_counts = {}
        
        # Get the most duplicated number
        for nums in num_list:
            if num in num_counts:
               num_counts[num] += 1
            else:
                num_counts[num] = 1

                # Print the number
                print(most_dupli)
    
    except ValueError:
        break



