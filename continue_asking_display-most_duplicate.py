# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# Make an empty list
num_list = []

# Ask for user input
while True:
    try:
        num = float(input("Enter number: "))
        num_list.append(num)
        
        # Get the most duplicated number
        for nums in num_list:
            if num_list:
                most_dupli = max(num_list)
                # Print the number
                print(most_dupli)
    
    except ValueError:
        break



