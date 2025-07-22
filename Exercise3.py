def main():
    """
    This function collects user information, validates inputs, 
    stores the data in a dictionary, and displays it nicely.
    """

    print("Welcome! Please provide the following information.\n")

    # Collecting basic input from the user
    name = input("Full Name: ").strip()
    hometown = input("Hometown: ").strip()

    # Ensuring the age is a positive integer
    while True:
        try:
            age = int(input("Age: "))
            if age <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input! Please enter a positive whole number for age.")

    # Collecting more information
    gender = input("Gender (optional): ").strip()
    email = input("Email Address (optional): ").strip()
    phone = input("Phone Number (optional): ").strip()

    # Storing all the information in a dictionary
    user_info = {
        'Name': name,
        'Hometown': hometown,
        'Age': age,
        'Gender': gender if gender else "Not provided",
        'Email': email if email else "Not provided",
        'Phone': phone if phone else "Not provided"
    }

    # Confirm the entered information
    print("\nThank you! Here is the information you entered:\n")
    for key, value in user_info.items():
        print(f"{key}: {value}")

    # Optional: save or continue
    print("\nIf any of the above information is incorrect, please re-run the program to enter it again.")


if __name__ == "__main__":
    main()