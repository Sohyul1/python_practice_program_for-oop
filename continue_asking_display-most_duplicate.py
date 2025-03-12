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
        
        # Count how many times the number appeared
        for nums in num_list:
            if num in num_counts:
               num_counts[num] += 1
            else:
                num_counts[num] = 1
        
        # Get the most duplicated number
        max_count = 0
        for num in num_counts:
                if num_counts[num] > max_count:
                    most_dupli = num
                    max_count = num_counts[num]
                # Print the number
                print(f"{most_dupli} occured {num_counts}")
    
    except ValueError:
        break



