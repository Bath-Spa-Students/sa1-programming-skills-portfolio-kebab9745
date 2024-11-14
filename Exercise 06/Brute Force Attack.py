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

# Define the correct password
correct_password = "12345"  # Set the correct password that the user needs to enter

# Define the maximum number of attempts allowed
max_attempts = 5  # Set the maximum attempts the user is allowed to try

# Initialize the number of attempts
attempts = 0  # Start the count of attempts at 0, since no attempts have been made yet

# Begin a loop that will continue as long as the number of attempts is less than max_attempts
while attempts < max_attempts:
    # Ask the user for the password
    entered_password = input("Enter the password: ")  # Prompt the user to enter the password
    
    # Check if the entered password is correct
    if entered_password == correct_password:  # Compare the entered password with the correct password
        print("Password accepted! Access granted.")  # If correct, print success message
        break  # Exit the loop, as the password was correct
    else:
        # If the password is incorrect, increment the attempts counter by 1
        attempts += 1  # Increase the attempts count by 1 for each incorrect entry
        
        # Calculate the remaining attempts
        remaining_attempts = max_attempts - attempts  # Subtract the current attempts from max_attempts
        
        # Check if there are any remaining attempts
        if remaining_attempts > 0:  # If the user has attempts left
            # Inform the user of the incorrect password and remaining attempts
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            # If no attempts are left, alert the user that authorities have been notified
            print("Incorrect password. Authorities have been alerted.")
