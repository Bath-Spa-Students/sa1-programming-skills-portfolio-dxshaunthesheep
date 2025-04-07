# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# The input() function collects user input as a string
search_name = input("Enter a name to search for: ")

#A flag variable is initialized in which the program is to track if a name was found.
#Boolean value set to true if a match is found
found = False

# This for loop will iterate through the list, checking each name one by one.
for name in names:
    #Compares the current name in the list to the one the user inputted
    #Its converted into lowercase to avoid a case-sensitive search
    if name.lower() == search_name.lower():
        # If a match is found, set the boolean flag to True
        found = True
        break

# After all names have been checked or breaking off from the loop early, display all the results
if found:
    # The f-string allows us to insert the variable value directly, which improves efficiency
    print(f"'{search_name}' was found in the list!")
else:
    # If found is still False, print a not-found message
    print(f"'{search_name}' was not found in the list.")


print("\nAvailable names:", ', '.join(names)) #Shows all the names if the search fails
#The join() method combines the list into a single string with commas