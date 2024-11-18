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

# Define a function to check if a number is even or odd
def check_even_or_odd(number):
    # See if the number is even
    if number % 2 == 0:  # If dividing by 2 leaves no remainder, it's even
        return f"The number {number} is even."  # Return a message saying it's even
    else:
        return f"The number {number} is odd."  # Otherwise, return a message saying it's odd

# Main function to run the program
def main():
    # Prompt the user to enter a number
    user_number = int(input("Enter a number: "))  # Get input and convert it to an integer
    
    # Call the function to check if the number is even or odd
    result_message = check_even_or_odd(user_number)  # Pass the number to the function
    
    # Print the result from the function
    print(result_message)  # Show if the number is even or odd

# Run the main function only if the script is executed directly
if __name__ == "__main__":
    main()  # Start the program by calling main()
