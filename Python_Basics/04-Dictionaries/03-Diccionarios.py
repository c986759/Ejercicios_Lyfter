# We created the dictionary.
employee = {
    "name": "John",
    "email": "john@ecorp.com",
    "access_level": 5,
    "age": 28
}

# We created the list.
delete_list = ["access_level","age"]

#We go through the list and delete those values ​​from the dictionary,
for index in range(len(delete_list)):
    deleted_item = employee.pop(delete_list[index])

# We are printing the dictionary.
print(employee)


