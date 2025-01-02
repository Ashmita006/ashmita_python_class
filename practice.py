#Iterator
class MyIterator:
    def __init__(self, data):
          self.data = data
          self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        print(f"Getting index : {self.index}")
        value = self.data[self.index] 
        self.index += 1
        return value
    
# 2
my_list= [1, 2, 3, 4, 5]
my_iter = MyIterator(my_list)
for num in my_iter:
    print(num)
    
#from abc import ABC, abstractctmethod 
class Vehicle():
      #@abstractctmethod
      def drive(self):
         print("Vehicle is driving")   
         
      def new_fn(self):
        print("My new fn")
        
class Car(Vehicle):        
    pass

car = Car()
print(car.drive())

#Encapsulation
class BankAccount:
    def __init__(self, name):
        self._balance = 0
        self.name = name
        
    def  deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        self._balance -= amount 
        
    def get_balance(self):
        return self ._balance
    
    def __str__(self):
        return f"Name: {self.name} and Balance: Hidden"
    
ashmita = BankAccount ("Ashmita")
ashmita.deposit(100)
print(ashmita)
print(ashmita.get_balance())
ashmita.withdraw(50)
ashmita.deposit(400)
ashmita.withdraw(100)
print(ashmita.get_balance())
    
#operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def  __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def  __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def  __multi__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __str__(self):
        return f"Vector: ({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = Vector(3, 4)
v4 = Vector(3, 4)
result_vector = v1 + v2
print(result_vector)

#1
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def  __add__(self, *others):
        add_vector = Vector(self.x, self.y)
        for other in others:
            add_vector = Vector(add_vector.x + other.x, add_vector.y + other.y)
        return add_vector 
    
    def  __sub__(self, *others):
        sub_vector = Vector(self.x, self.y)
        for other  in others:
            sub_vector = Vector(sub_vector.x - other.x, sub_vector.y - other.y)
        return sub_vector
    
    def  __mul__(self, *others):
        mul_vector = Vector(self.x, self.y)
        for other in others:
            mul_vector = Vector(mul_vector.x * other.x, mul_vector.y * other.y)
        return mul_vector
              
    def  __str__(self):
        return f"Vector: ({self.x}, {self.y})"          
    
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = Vector(3, 4)
v4 = Vector(3, 4)
result_vector = v1 + v2 + v3 + v4
print(result_vector)               

#example 5.1: handling divisiom by 0
try:
    result = 10/0
except ZeroDivisionError as e: 
    print("Exception: ", e) #Output:Exception: division by zero
#example: 5.2: handling index out of range
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print("Exception: ", e) #Output: Exception: List index out of range

#....................................

class NoMoneyException(Exception):
    pass
class OutOfBudget(Exception):
    pass

balance = int(input("Enter a balance to withdraw: "))
try:
    if balance < 1000:
        raise NoMoneyException("You have no moncey to withdraw")
    elif balance > 10000:
        raise OutOfBudget("You have reached your limit")
except Exception as error:
    print((error))