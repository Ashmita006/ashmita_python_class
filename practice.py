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
    