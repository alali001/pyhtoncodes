# Function to check if a number is even or odd
def check_even_odd(number):
    if number == 0:
        return "0 is neither even nor odd."
    elif number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."


# Main function
def main():
    print("🔷 Even/Odd Number Checker 🔷")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter a number: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break

        try:
            num = int(user_input)
            result = check_even_odd(num)
            print(result + "\n")
        except ValueError:
            print("⚠️ Please enter a valid integer or type 'exit' to quit.\n")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()