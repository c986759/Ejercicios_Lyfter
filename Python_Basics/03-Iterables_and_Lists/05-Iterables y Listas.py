
#define the empty list and the variable for the largest number
number_list = []
max_number = 0

#We ask the user for the numbers
print ("Ingrese los 10 numeros")

#The user enters the numbers, and we store them in the list.
for index in range(0,10):
    actual_num = int(input(f"Ingrese el {index + 1} número: "))  
    number_list.append(actual_num)
    #store the largest number
    if actual_num > max_number:
        max_number=actual_num
  
#print all the numbers and display the largest number
print(f"La lista de números ingresados es la siguiente: {number_list}")
print(f"EL número mayor en la lista es el: {max_number} ")

user_data = {
	'full_name': 'John Snow',
	'email': 'j.snow@gmail.com',
}

user_data['password'] = 'WinterIsComing2023'
print(user_data)