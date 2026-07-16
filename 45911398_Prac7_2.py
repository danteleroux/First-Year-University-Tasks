# Dante le Roux 45911398_Prac7_2

# Defining name_list
name_list = ["John", "Anna", "John", "Mike", "Anna", "Paul"]

# Allowing program to continue running until it is purposely stopped
while True:

# Asking user to input a name
    name_input= input("Please type in a name (enter exit to stop program): ")

# Condition for program to stop running
    if name_input == "exit":
        break

# Initializing name_count for each input
    name_count = 0

# Forloop to count occurences of name entered in the the name list
    for name in name_list:
        if name == name_input:
            name_count = name_list.count(name_input)

# Defining what should be printed, depending on the "count"
    if name_count >= 2:
        print(f"The name {name_input} appears {name_count} or more times in the list.")
    else:
        print(f"The name {name_input} does not appear 2 times in the list")

    