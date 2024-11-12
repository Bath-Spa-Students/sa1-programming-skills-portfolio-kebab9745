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

# Get user input for full name and store it in the variable 'name'
name = input("Enter your full name: ")

# Get user input for hometown and store it in the variable 'hometown'
hometown = input("Enter your hometown: ")

# Start a loop to get valid age from the user
while True:
    try:
        # Prompt user to enter their age, convert it to an integer, and assign it to 'age'
        age = int(input("Enter your age: "))
        
        # If conversion is successful, exit the loop
        break  
    except ValueError:
        # If there was an error (non-numeric value), print a message asking for numerical value 
        print("Please enter a numerical value for age.")

# Create a dictionary called bio_data with keys "Name", "Hometown", and "Age"
bio_data = {
    "Name": name,
    "Hometown": hometown,
    
    # Convert 'age' back into string format before storing as it's easier when printing later.
    "Age": str(age)  
}

# Print header line indicating that biography information follows
print("\nYour Biography:")

# Loop through each key-value pair in bio_data dictionary 
for key, value in bio_data.items():
     # Print each piece of data on its own line using formatted strings (f-strings)
     print(f"{key}: {value}")