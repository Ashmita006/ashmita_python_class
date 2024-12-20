
def store_contact(name, number, contacts={}):
    contacts[name] = number
    return contacts

def phone_book():
    contacts = {}
    while True:
        name=input("enter  name")
        number = input("enter number")
        contacts = store_contact(name, number,contacts)
        user_choice = input("""
       Do you want to exit ?
       1. Yes
       2. No
       """)
        if user_choice == "1":
           return contacts

my_contact_book = phone_book ()

def get_phone_number(name, contacts):
    return contacts.get(name.lower())

user_name = input("Enter name to find phone number")
print (get_phone_number(user_name, my_contact_book))

    
    
    
    
    
    
    