import json
contacts = []

def load_contacts():
    with open("contacts.json", "r") as file:
        return json.load(file)

    
contacts = load_contacts()

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

while True:
    print("=== CONTACT BOOK ===")
    if len(contacts) == 0:
        print("No Contacts found")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")
   
    try:
            choice = int(input("Choose an option: "))
    except ValueError:
             print("The choice input should be integer!")
             continue
   
    if choice == 1:
       name = input("Enter the name: ")
       phone = input("Enter phone number: ")
   
       contact = {
          "name": name,
          "phone":  phone
          }
       contacts.append(contact)
       print("Contact added successfully!")
       save_contacts(contacts)

    if choice == 2:
       search_name = input("Enter name to search: ")
       found = False
       for contact in contacts:
           if contact["name"].lower() == search_name.lower():
               print(contact["name"], "-", contact["phone"])
               found = True
               break

       if not found: 
             print("Contact not found.")

    if choice == 3:
       delete_name = input("Enter name to delete: ")
       found = False

       for contact in contacts:
           if contact["name"].lower() == delete_name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted")
            found = True
            break

       if not found:
            print("Contact not found")

    if choice == 4:
            print("Goodbye! ")
            break
    
