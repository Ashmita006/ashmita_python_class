#Input a number -> Double it -> Add 10 -> Halve it -> Subtract original -> Output = 5 
a = float(input("Enter a number: "))
result = ((a* 2) + 10) / 2 - 5
print("The result is:", result)

#to convert temperature Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")

#to convert meter to kilometer
meters = float(input("Enter a length in meter:"))
kilometer = meters / 1000
print(f"{meters}meters is equal to {kilometer}kilometer")

#to convert feet into inches
feet = float(input("Enter length in feet: "))
inches = feet * 12
print(f"{feet} feet is equal to {inches} inches.")

#Currency (using hardcoded exchange rates)
exchange_rates = {
    "USD_TO_INR": 82.5,
    "USD_TO_EUR": 0.91,
    "INR_TO_USD": 0.012,
    "INR_TO_EUR": 0.011,
}

amount = float(input("Enter the amount: "))
conversion_type = input("Enter the conversion (e.g., USD_TO_INR, INR_TO_USD): ").upper()
if conversion_type in exchange_rates:
    converted_amount = amount * exchange_rates[conversion_type]
    print(f"{amount} {conversion_type.split('_TO_')[0]} is equal to {converted_amount:.2f} {conversion_type.split('_TO_')[1]}")
else:
    print("Invalid conversion type. Please try again.")
    
#to calculate simple interest 
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of interest (in %): "))
time = float(input("Enter the time (in years): "))  
simple_interest = (principal*rate*time)/100
print(f"The Simple Interest is: {simple_interest:.2f}")

#Calculate the area and perimeter of shapes (rectangle)
length = float(input("Enter the length of a rectangle: "))
breadth = float(input("Enter the breadth of a rectangle:"))
Area = (length * breadth)
Perimeter = 2 * (length + breadth)
print(f"The Area is:{Area:.2f}")
print(f"The Perimeter is: {Perimeter:.2f}" )

#Calculate the area and perimeter of shapes (Circle)
radius = float(input("Enter the radius of a circle:"))
Area = 22/7 * radius * radius
Perimeter = 2 *22/7 *radius
print(f"The Area is:{Area:.2f}")
print(f"The Perimeter is: {Perimeter:.2f}" )

#Calculate the area and perimeter of shapes (triangle))
a = float(input("Enter the lenght of one side:"))
b = float(input("Enter the base of  triangle:"))
c = float(input("Enter the heigth of triangle:"))
Area=1/2*b*c
Perimeter=a+b+c
print(f"The Area is:{Area:.2f}")
print(f"The Perimeter is: {Perimeter:.2f}" )

#Check if a number is even/odd.
a = float(input("Enter the number:"))
n = a % 2
if n == 0:
              print("Even")
else:
       print("odd")
       
# Determine if a number is prime.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is NOT a Prime number.")
            break
    else:
        print(f"{num} is a Prime number.")
else:
    print(f"{num} is NOT a Prime number.")
    
 #Find whether a number is a multiple of another number.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num2 != 0 and num1 % num2 == 0:
    print(f"{num1} is a multiple of {num2}.")
else:
    print(f"{num1} is NOT a multiple of {num2}.")

