'''
Exercise 8: Simple Search - 30 Marks

Write a program that searches for a specific string within a list of strings. The list
is initialized with specific names (“Jake” “Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
, and your task is to search for “Sam”.

Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.

'''

# List of names to search through
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Name we want to search for
search_name = "Sam"  # The name we're looking for

# Check if "Sam" is in the list
if search_name in names:
    print(f"{search_name} found in the list!")  # Print a message if "Sam" is found
else:
    print(f"{search_name} not found in the list.")  # Print a message if "Sam" isn't found

# Optional: Let the user enter a name to search for
# Prompt the user to enter a name they want to search for
user_search = input("Enter the name you want to search for: ")  # Get input from the user

# Check if the user's input is in the list
if user_search in names:  # See if the name the user entered is in the list
    print(f"{user_search} found in the list!")  # Print a message if the name is found
else:
    print(f"{user_search} not found in the list.")  # Print a message if the name isn't found

