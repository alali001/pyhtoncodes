def is_leap_year(year: int) -> bool:
    """
    Returns True if the given year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    # Dictionary mapping month numbers to days (non-leap year)
    month_days = {
        1: 31,
        2: 28,  # Will adjust for leap year if needed
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    print("📅 Welcome! Find out how many days are in a given month.\n")

    try:
        month = int(input("Enter the month number (1-12): "))
        if not (1 <= month <= 12):
            print("❌ Invalid month number. Please enter a number between 1 and 12.")
            return

        # Optional: ask for year if February
        year = None
        if month == 2:
            year_input = input("Do you want to enter a year to check for leap year? (yes/no): ").strip().lower()
            if year_input in ['yes', 'y']:
                while True:
                    try:
                        year = int(input("Enter the year (e.g., 2024): "))
                        break
                    except ValueError:
                        print("Please enter a valid year.")

            if year and is_leap_year(year):
                print(f"✅ February {year} has 29 days (leap year).")
            else:
                print(f"📆 February has 28 days." if year is None else f"📆 February {year} has 28 days.")
        else:
            print(f"📆 Month {month} has {month_days[month]} days.")

    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()