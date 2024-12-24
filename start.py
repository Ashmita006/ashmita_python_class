def mul(*args):
    result=1
    for number in args:
        result *=number
    return result
def diff (a,b):
    return a-b
def sum(a,b):
    return a+b
def div (a,b):
    return a/b
print(mul(1,2,3,4,5))


def print_full_name(**ashmita):
    print(ashmita)
    print (f"My full name is {ashmita['firest_name']}{ashmita['last_name']}")
print_full_name(first_name="Ashmita", last_name="shrestha", middle_name="none")
    
def print_result(*args, **kwargs):
    print(args)
    print(kwargs)
    result = 0
    for number in args:
        result += number
        print(f"My full name is{kwargs['first_name']}{kwargs['last_name']}and total marks = {result}")
print_result(10,20,30,40,50, first_name= "Ashmita", last_name="Shrestha")

def make_phone_book():
    x=input("enter your full name")
    if x==adddict["name"]:
        print(adddict)
        
adddict= {
    "name":"Ashmita Shrestha",
    "phone_number":9819716789
}
make_phone_book()


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

    
    
    
    
    
    
    