#we create my_list
my_list = ['a','b','c','d','e','f']

#determine the first and last data points
first_element=my_list[0]
last_element= my_list [-1]

#delete and insert the values
my_list.pop(0)
my_list.insert(0, last_element)
my_list.pop()
my_list.insert(len(my_list), first_element)

#print the new my_list
print(my_list)