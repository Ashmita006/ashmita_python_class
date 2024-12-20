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


