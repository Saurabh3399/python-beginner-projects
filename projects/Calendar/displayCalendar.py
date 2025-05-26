import calendar
from datetime import datetime # Added: Import datetime module for current date

def display_cal(year_input, month_input):
    """
    Display a calendar for the desired year and month, highlighting today's date.

    Parameters:
    year_input (int): The year for which the calendar is to be displayed.
    month_input (int): The month for which the calendar is to be displayed.

    """
    # Get today's date details
    today = datetime.now()
    current_year = today.year
    current_month = today.month
    current_day = today.day

    # Create a TextCalendar instance.
    # calendar.MONDAY means weeks start on Monday (0=Monday, 6=Sunday).
    # You can change this to calendar.SUNDAY if you prefer.
    cal = calendar.TextCalendar(calendar.MONDAY)

    # Print month and year header, centered for a standard calendar look
    print(f"\n      {calendar.month_name[month_input]} {year_input}")
    # Print weekday header (Mo Tu We Th Fr Sa Su, assuming Monday start)
    print("Mo Tu We Th Fr Sa Su")

    # Iterate through the weeks and days of the specified month
    # monthdayscalendar returns a list of lists, where each inner list is a week.
    # Days from previous/next months are represented as 0.
    for week in cal.monthdayscalendar(year_input, month_input):
        week_str = ""
        for day in week:
            if day == 0:  # If the day is 0, it's a blank space for days from prev/next month
                week_str += "   " # Three spaces to maintain alignment
            else:
                # Check if the current day in the loop matches today's actual date
                # AND if the displayed month/year match the current month/year
                if (day == current_day and
                    month_input == current_month and
                    year_input == current_year):
                    # Apply ANSI escape codes for Bold Blue text
                    # \033[1m makes text bold
                    # \033[94m sets text color to bright blue
                    # \033[0m resets text formatting
                    week_str += f"\033[1m\033[94m{day:2d}\033[0m "
                    # Alternative if ANSI codes don't work well on a specific terminal:
                    # week_str += f"*{day:2d}* " # Surround with asterisks
                else:
                    # Format day to take 2 characters, followed by a space (e.g., " 1 ", "10 ")
                    week_str += f"{day:2d} "
        print(week_str.strip()) # .strip() removes any trailing space from the last day of the week
    print() # Add an extra newline for better visual spacing after the calendar


def fetch_year():
    """
    Prompts the user for a valid year and returns the year as an integer.
    """
    while True:
        try:
            year_input = int(input("Enter year: "))
            if year_input < 0:
                print("Year cannot be negative.") # Changed: More specific error message
                continue
            return year_input
        except ValueError:
            print("Invalid input. Please enter a whole number for the year.") # Changed: More specific error message


def fetch_month():
    """
    Function that asks the user to enter a month, validates the input, and returns the valid month.
    """
    while True:
        try:
            month_input = int(input("Enter month (1-12): ")) # Changed: Added hint for range
            if month_input < 1 or month_input > 12:
                print("Month must be between 1 and 12.") # Changed: More specific error message
                continue
            return month_input
        except ValueError:
            print("Invalid input. Please enter a whole number for the month.") # Changed: More specific error message


# --- Main execution of the program ---
# These lines are unchanged from your original code.
year_input = fetch_year()
month_input = fetch_month()

display_cal(year_input, month_input)