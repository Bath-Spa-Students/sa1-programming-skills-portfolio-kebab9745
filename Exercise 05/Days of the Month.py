def get_days_in_month(month, year=None):
    # Dictionary mapping month numbers to the number of days
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # Check if the input month is valid
    if month < 1 or month > 12:
        return "Invalid month number."
    
    # Adjust February days for leap year
    if month == 2:
        if year:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29  # Leap year
        return month_days[month]  # Normal February
    
    return month_days[month]  # For other months

# Input Handling
month = int(input("Enter the month number (1-12): "))
year = None

if month == 2:
    year_input = input("Is it a leap year? (yes/no): ").strip().lower()
    if year_input == 'yes':
        year = int(input("Enter the year: "))

# Output Handling
days = get_days_in_month(month, year)
if isinstance(days, int):
    print(f"The number of days in month {month} is: {days}")
else:
    print(days)  # Output the error message if invalid month number
