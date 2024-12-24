#List
my_list = [1, 2, 3, 'a', 'b', 'c']
my_list.append('d')
my_list.remove(2)
print(len(my_list))
print(my_list)

#tuples
my_tuple = [10, 20, 30, 40, 50]
print(my_tuple[1])
thistuple = list(my_tuple)
thistuple[3] = 35
my_tuple = tuple(thistuple)
print(my_tuple)

#Sets
my_set = {1, 2, 2, 3, 4, 4, 5,}
my_set.add(6)
my_set.remove(3)
print(my_set)
if "4" in my_set:
    print("yes")

#Dictionaries
my_dict = {'name' : 'Jhon' , 'age' : 25 , 'city' : 'New York'}
my_dict['job'] = 'Engineer'
my_dict['age'] = 26
my_dict.pop('city', None)  
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Dictionary:", my_dict)

#Check for palindrome
def is_palindrome(a):
    return a == a[::-1]
print(is_palindrome("aca"))
print(is_palindrome("aabbaa"))
print(is_palindrome("abbbb"))
print(is_palindrome("baabbb"))

#Area of circle
def area_circle(a):
 return 3.14 * radius * radius
radius = float(input("Enter the radius of the circle: "))
area = area_circle(radius)
print(f"The area of the circle with radius {radius} is: {area}")
    
#prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


    
    