# crud operations
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added!")

def view_contacts():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted!")
    else:
        print("Contact not found!")

while True:
    choice = input("1. Add Contact  2. View Contacts  3. Delete Contact  4. Exit\nChoose: ")
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        add_contact(name, phone)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter Name to Delete: ")
        delete_contact(name)
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
# Step 1-Enter Name & Phone
# Step 2-View Contacts
# Step 3-Delete Contact
# Step 4-Exit