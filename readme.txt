empty_list = [] #add to list
empty_list.append("apple")
empty_list.append("banana")
empty_list.append("apple")
empty_list.append("banana")

for index, fruit in enumerate(empty_list):
    print(f"Item position: {index}and value: {fruit}")

fruits = ("apple", "banana", "cherry", "kiwi", "raspberry")
print(fruits[1]) #print second iteam
(*green, yellow, red) = fruits
print(green, yellow, red)

fruits = {"apple", "banana", "cherry", "kiwi", "raspberry"}
for item in fruits:
    print(item)
    fruits.add("kiwi")
    print(fruits)
    
    #battery basket
batteries = [50, 30, 4, 45,12,18,30] #battery basket
minimum_battery_power = 20 #battery use minimum 20% charge
usable_battery_power = 0 #battery 0 power 0
usable_battery_count = 0 # usable battery 0
for battery in batteries: #check every battery
    if battery > minimum_battery_power: #check if battery is over charge 20% to use
        usable_battery_power += battery #if yes use power added
        usable_battery_count += 1 #if yes use battery count add
print(f"There are {usable_battery_count} batteries which can be used to generate {usable_battery_power}")  

#alien message
alien_message = "Hi human how are you. I am an alien"
print(f"""
      Alien message = {alien_message}
      Now, Human message = {alien_message[::-1]} #reserve string
      """)

#Resource( Allocation
available_food =[
"apple",
"Cherry",
"banana",
"watermelon",
"chocolate",
"berries",
"pizza",
"water",
]
available_crews = 3
each_crew_food  = len(available_food) // available_crews
remaining_food_count =  len(available_food) % available_crews
print(f"Each crew get {each_crew_food} food and Remaining food count = {remaining_food_count}")
