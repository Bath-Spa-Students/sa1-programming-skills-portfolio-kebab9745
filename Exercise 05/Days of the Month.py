'''
Exercise 5: Days of the Month - 30 Marks
Write a program that tells a user how many days there are in a specific month.
Use a dictionary to map the month numbers (1-12) to the number of days in
each month.

Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month num-
bers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For
February, ask the user if the year is a leap year and adjust the number of days
accordingly.

'''

def get_days_in_month(month, year=None):
    # Define a dictionary that maps each month to its number of days
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # Make sure the month is a valid number between 1 and 12
    if month < 1 or month > 12:
        return "Invalid month number."
    
    # Check if it's February, then adjust for leap years
    if month == 2:
        if year:
            # Determine if the year is a leap year
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29  # Return 29 for a leap year
        return month_days[month]  # Return 28 for a normal year in February
    
    return month_days[month]  # Return the days for other months

# Ask the user to enter the month number
month = int(input("Enter the month number (1-12): "))
year = None

# If it's February, ask if the user wants to check for a leap year
if month == 2:
    year_input = input("Is it a leap year? (yes/no): ").strip().lower()
    if year_input == 'yes':
        year = int(input("Enter the year: "))  # Get the specific year if needed

# Get the number of days and display the result
days = get_days_in_month(month, year)
if isinstance(days, int):
    print(f"The number of days in month {month} is: {days}")
else:
    print(days)  # Print an error message if the month number is invalid
