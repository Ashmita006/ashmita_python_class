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

#Fibonacci Number
def fibonacci_sequence_and_sum(max_num):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= max_num:
            sequence.append(sequence[-1] + sequence[-2])
    sequence_sum = sum(sequence)
    formatted_sequence = "+".join(map(str, sequence))    
    print(f"{formatted_sequence} = {sequence_sum}")
max_num = int(input("Enter the maximum number for Fibonacci sequence:"))
fibonacci_sequence_and_sum(max_num)

#Simple Interest
def calculate_simple_interest(principal, time, rate):
    interest = (principal * time * rate) / 100
    return interest
principal = float(input("Enter the principal amount:"))
time = float(input("Enter the time in years:"))
rate = float(input("Enter the rate of interest:"))
simple_interest = calculate_simple_interest(principal, time, rate )
print(f"The Simple Interest is: {simple_interest:.2f}")

#Multiplication Table
def multiplication_table(num):
      print(f"Multiplication Table of {num}:")
      for i in range(1, 11):
          print(f"{num} * {i} = {num * i}")
num = int(input("Enter s number to print its multiplication table:"))
multiplication_table(num)

#Leap Year
def  is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return False
year = int(input("Enter a year to check if it's a leap year:"))
if is_leap_year(year):
    print(f"{year} is a leap year.") 
else:
    print(f"{year} is not a leap year.") 
    
#Vowels in a string