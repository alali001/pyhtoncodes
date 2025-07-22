import getpass

def main():
    # Define the correct password
    correct_password = "secure2025"

    # Maximum number of attempts
    max_attempts = 3
    attempts = 0

    print("🔒 Secure Login System")
    print(f"You have {max_attempts} attempts to enter the correct password.\n")

    while attempts < max_attempts:
        # Use getpass to hide the input
        user_input = getpass.getpass("Enter the password: ")

        if user_input == correct_password:
            print("\n✅ Access granted. Welcome!")
            break
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"❌ Incorrect password. You have {remaining} attempt(s) left.\n")
            else:
                print("\n🚨 Maximum attempts reached. Authorities have been alerted.")
                # Optional: add lockout mechanism here

if __name__ == "__main__":
    main()