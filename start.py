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
    