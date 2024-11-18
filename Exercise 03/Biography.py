'''
Exercise 3: Biography - 25 Marks

In this exercise, you’ll create a program that stores and prints your name, home-
town, and age to the console using a Python dictionary.

Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a
dictionary.
2. Print the values on separate lines using a single print() statement.
3. Use variables with appropriate data types for each piece of information.

Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the
values. Try giving both your first and second name when asked for your name.
What happens? How can you handle multiple words in Python? Test the
program by entering a string value for age (e.g., “twenty”). What happens?
How can you prevent this issue?

'''

# Ask the user for their full name and save it in 'name'
name = input("Enter your full name: ")

# Ask the user for their hometown and save it in 'hometown'
hometown = input("Enter your hometown: ")

# Keep asking the user for their age until they enter a valid number
while True:
    try:
        # Prompt for age, then try to convert it to an integer and save it in 'age'
        age = int(input("Enter your age: "))
        
        # If no error occurs, break out of the loop
        break  
    except ValueError:
        # If there's an error, let the user know they need to enter a number
        print("Please enter a numerical value for age.")

# Create a dictionary called bio_data to store the user's name, hometown, and age
bio_data = {
    "Name": name,
    "Hometown": hometown,
    
    # Convert age to a string so it prints nicely later on
    "Age": str(age)  
}

# Print a heading for the user's bio information
print("\nYour Biography:")

# Go through each piece of info in bio_data and print it out
for key, value in bio_data.items():
    # Use an f-string to format each line of the bio
    print(f"{key}: {value}")
