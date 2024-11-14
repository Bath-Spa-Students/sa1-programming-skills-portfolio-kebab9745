'''
Exercise 10: Is it even? - 35 Marks
Write a program that tests if a value is even or odd. Follow the instructions
outlined below:

Instructions:
• The program should ask the user for a number from within the main
function.
• The entered number should be passed to a function that determines if the
value is even or odd.
• The function should return a message indicating whether the number is
even or odd.
• The message returned by the function should be printed from within the
main function.

'''

# Function to check if a number is even or odd
def check_even_or_odd(number):
    # Check if the number is even
    if number % 2 == 0:  # If the remainder when divided by 2 is 0, it's even
        return f"The number {number} is even."  # Return a message indicating the number is even
    else:
        return f"The number {number} is odd."  # Otherwise, return a message indicating the number is odd

# Main function to run the program
def main():
    # Ask the user for a number
    user_number = int(input("Enter a number: "))  # Convert user input to an integer
    
    # Call the function to determine if the number is even or odd
    result_message = check_even_or_odd(user_number)  # Pass the number to the function
    
    # Print the message returned by the function
    print(result_message)  # Display whether the number is even or odd

# Only run the main function if the script is executed directly
if __name__ == "__main__":
    main()  # Run the main function to start the program
