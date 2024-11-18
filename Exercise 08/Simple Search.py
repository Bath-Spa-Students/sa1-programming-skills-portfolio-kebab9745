'''
Exercise 8: Simple Search - 30 Marks

Write a program that searches for a specific string within a list of strings. The list
is initialized with specific names (“Jake” “Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
, and your task is to search for “Sam”.

Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.

'''

# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Search for a specific name 
search_name = "Sam"  # Define the name we are looking for

# Check if "Sam" is in the list
if search_name in names:
    print(f"{search_name} found in the list!")  # If "Sam" is in the list it will print a success message
else:
    print(f"{search_name} not found in the list.")  # If "Sam" is not in the list, print a failure message

# Optional Requirement: Allow the user to input a search term
# Ask the user to enter a name to search for
user_search = input("Enter the name you want to search for: ")  # Take user input for the search term

# Implement the search functionality with the user's input
if user_search in names:  # Check if the user's input is in the list
    print(f"{user_search} found in the list!")  # If found, print success message
else:
    print(f"{user_search} not found in the list.")  # If not found, print failure message
