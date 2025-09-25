# fns_and_dsa/explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days):
    
    # Use today's date (date portion only) and add a timedelta
    future_date = datetime.now().date() + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Part 1: display current date and time
    display_current_datetime()

    # Part 2: ask the user for number of days and calculate future date
    while True:
        try:
            days_input = input("Enter the number of days to add to the current date: ").strip()
            days = int(days_input)
            break
        except ValueError:
            print("Please enter a valid integer for the number of days.")

    calculate_future_date(days)

if __name__ == "__main__":
    main()
