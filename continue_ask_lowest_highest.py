# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

# Make a count variable 
count = 1

# Make an empty list
num_list = []

# Ask user for input (break if input is invalid)
while True:
    try:
        number = float(input(f"Enter Number {count}: "))
        count += 1

        # Append the numbers into the list
        num_list.append(number)

        # Sort the list
        num_list.sort()

    except ValueError:
        # Print the sorted list
        print(num_list)
        print("Bye!")
        break
      