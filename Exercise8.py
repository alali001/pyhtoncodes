# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

print("📋 Current list of names:")
print(", ".join(names))

# Ask the user for a name to search
search_term = input("\nEnter the name you want to search for: ").strip()

if not search_term:
    print("⚠️ You did not enter a name.")
else:
    # Perform case-insensitive search
    found_names = [name for name in names if name.lower() == search_term.lower()]

    if found_names:
        print(f"✅ {found_names[0]} was found in the list!")
    else:
        print(f"❌ {search_term} was NOT found in the list.")