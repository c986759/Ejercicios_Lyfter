# Pedir los tres números al usuario
number_one = int(input("Escribe el primer número: "))
number_two = int(input("Escribe el segundo número: "))
number_three = int(input("Escribe el tercer número: "))

# Comparar para encontrar el larger_number
if number_one >= number_two and number_one >= number_three:
    larger_number = number_one
elif number_two >= number_one and number_two >= number_three:
    larger_number = number_two
else:
    larger_number = number_three
# Mostrar el numero larger_number
print("El número mayor es:", larger_number)

