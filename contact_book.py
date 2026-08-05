
contacts = []
while True:
    print("\n==== CONTACT BOOK====")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    try:

     choice = int(input("Choose an option: "))
    except ValueError:
      print("The choice input should be integer!")
      break

    if choice == 1:
        name = input("Enter the name: ")
        phone = input("Enter phone number: ")

        contact = {
          "name": name,
          "phone":  phone
        }
        print(contact)
        contacts.append(contact)
        print("Contact added successfully!")
    if choice == 2:
       if len(contacts) == 0:
          print("No contacts found.")
       else:
          for contact in contacts:
             print(contact)
    if choice == 3:
       search_name = input("Enter name to search: ")
       found = False
       for contact in contacts:
          if contact["name"] == search_name:
             print(contact["name"], "-", contact["phone"])
             found = True
             if not found: 
                print("Contact not found.")
    if choice == 4:
       delete_name = input("Enter name to delete: ")
       found = False
       for contact in contacts:
          if contact["name"] == delete_name:
             contacts.remove(contact)
             print("Contact deleted")
             found = True
             break
          if not found:
             print("Contact not found")
    if choice == 5:
       print("See ya! ")
       break
       

