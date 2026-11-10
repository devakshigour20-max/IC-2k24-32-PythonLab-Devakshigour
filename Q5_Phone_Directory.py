# Phone Directory

contacts = {
    "Anita": {"phones": ["9876543210"], "email": "anita@mail.com", "city": "Pune"},
    "Manoj": {"phones": ["9123456780", "9988776655"], "email": "manoj@mail.com", "city": "Delhi"},
    "Zara": {"phones": ["9000011111"], "email": "zara@mail.com", "city": "Pune"}
}

while True:
    print("\n1. Add contact")
    print("2. Add another number")
    print("3. Update email or city")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Reports")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        if name in contacts:
            print("Contact already exists")
        else:
            number = input("Enter 10 digit phone number: ")
            used = [phone for data in contacts.values() for phone in data["phones"]]
            if not number.isdigit() or len(number) != 10:
                print("Invalid phone number")
            elif number in used:
                print("Number already belongs to another contact")
            else:
                email = input("Enter email: ")
                city = input("Enter city: ")
                contacts[name] = {"phones": [number], "email": email, "city": city}
                print("Contact added")

    elif choice == "2":
        name = input("Enter contact name: ")
        if name not in contacts:
            print("Contact not found")
        else:
            number = input("Enter another phone number: ")
            used = [phone for data in contacts.values() for phone in data["phones"]]
            if not number.isdigit() or len(number) != 10:
                print("Invalid phone number")
            elif number in used:
                print("Number already belongs to a contact")
            else:
                contacts[name]["phones"].append(number)
                print("Number added")

    elif choice == "3":
        name = input("Enter contact name: ")
        if name not in contacts:
            print("Contact not found")
        else:
            field = input("Enter email or city: ").lower()
            if field == "email":
                contacts[name]["email"] = input("Enter new email: ")
                print("Email updated")
            elif field == "city":
                contacts[name]["city"] = input("Enter new city: ")
                print("City updated")
            else:
                print("Invalid choice")

    elif choice == "4":
        name = input("Enter contact name: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")

    elif choice == "5":
        search = input("Enter name to search: ").lower()
        found = False
        for name, data in contacts.items():
            if search in name.lower():
                print(name, data)
                found = True
        if not found:
            print("Contact not found")

    elif choice == "6":
        reverse = {phone: name for name, data in contacts.items()
                   for phone in data["phones"]}
        number = input("Enter number for reverse lookup: ")
        print("Owner:", reverse.get(number, "not found"))

        city_groups = {}
        for name, data in contacts.items():
            city_groups.setdefault(data["city"], []).append(name)
        print("Contacts by city:", city_groups)

        print("Contacts with more than one number:",
              {name: data["phones"] for name, data in contacts.items()
               if len(data["phones"]) > 1})

        print("Directory:")
        for name in sorted(contacts):
            print(name, contacts[name])

    elif choice == "7":
        break
    else:
        print("Invalid choice")
