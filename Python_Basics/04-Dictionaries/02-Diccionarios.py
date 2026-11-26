# create the two lists of the same size
list_of_keys = ['first_name', 'last_name', 'role']
list_of_values = ['Alek', 'Castillo', 'Software Engineer']

#create a new, empty dictionary
new_dictionary = {}

#For each element in the list, we execute the following:
for index in range(len(list_of_keys)):
    # We store the key and value data for each list.
    current_key = list_of_keys[index]
    current_value = list_of_values[index]
    
    #they are inserted into the new key:value dictionary
    new_dictionary[current_key] = current_value


# We are printing the dictionary.
print(new_dictionary)

# We print only the keys using the for loop.
print("Keys: ")
for key in new_dictionary.keys():
    print(key)

print("Values: ")
# We print only the values using the for loop.
for value in new_dictionary.values():
    print(value)
