'''
Exercise 6: Brute Force Attack - 30 Marks
Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the
correct one is entered.
3. Output an appropriate message when the correct password is entered.

Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the
user enters the wrong password, inform them of the remaining attempts. If the
maximum number of attempts is reached, inform the user that the authorities
have been alerted.

'''

# Set the correct password
correct_password = "12345"  # The password the user needs to enter

# Set the maximum number of allowed attempts
max_attempts = 5  # Limit of tries the user can make

# Track the number of attempts the user has made
attempts = 0  # Start with zero attempts

# Start a loop to let the user keep trying as long as they have attempts left
while attempts < max_attempts:
    # Ask the user to enter the password
    entered_password = input("Enter the password: ")  # Prompt the user
    
    # Check if the entered password matches the correct one
    if entered_password == correct_password:  # Compare passwords
        print("Password accepted! Access granted.")  # If correct, grant access
        break  # Exit the loop since the password is correct
    else:
        # If the password is wrong, add 1 to the attempt count
        attempts += 1  # Increase attempts by 1
        
        # Calculate how many attempts are left
        remaining_attempts = max_attempts - attempts  # Figure out the remaining tries
        
        # Let the user know how many tries they have left, or alert them if they've run out
        if remaining_attempts > 0:  # If they still have attempts
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Incorrect password. Authorities have been alerted.")  # No attempts left
