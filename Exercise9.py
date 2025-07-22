def hello(name="there"):
    """
    Prints a greeting to the given name.
    Defaults to 'there' if no name is provided.
    """
    print(f"Hello, {name}!")


def main():
    """
    Main function to run the program.
    Asks the user for their name and greets them.
    """
    user_name = input("Enter your name: ").strip()
    if not user_name:
        hello()
    else:
        hello(user_name)


if __name__ == "__main__":
    main()