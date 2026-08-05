
def welcome():
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
        

