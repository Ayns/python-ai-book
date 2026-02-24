# Contact Book - Chapter 4

contacts = {}

while True:
    print()
    print("1. Add Contact")
    print("2. View Contact")
    print("3. View All")
    print("4. Search")
    print("5. Delete")
    print("6. Exit")
    choice = input("\nChoice: ")

    if choice == "1":
        name = input("Name: ")
        clean_name = name.strip().title()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()
        contacts[clean_name] = {"phone": phone, "email": email}
        print(f"{clean_name} added!")
    elif choice == "2":
        name = input("Name: ").strip().title()
        info = contacts.get(name)
        if info:
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
        else:
            print(f"{name} not found.")
    elif choice == "3":
        if contacts:
            for name, info in contacts.items():
                print(f"{name} | {info['phone']}")
        else:
            print("No contacts yet.")
    elif choice == "4":
        search_text = input("Search: ").lower()
        found = False
        for name in contacts:
            if search_text in name.lower():
                print(f"{name} | {contacts[name]['phone']}")
                found = True
        if not found:
            print("No matches found.")
    elif choice == "5":
        name = input("Name to delete: ").strip().title()
        if name in contacts:
            del contacts[name]
            print(f"{name} deleted.")
        else:
            print(f"{name} not found.")
    elif choice == "6":
        print("Goodbye!")
        break
