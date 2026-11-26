my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Recorremos la lista al revés (desde el último índice hasta el 0)
#para evitar el desface a la hora de eliminar un item
for i in range(len(my_list) - 1, -1, -1):
    # Verificamos si el número en la posición 'i' es impar
    if my_list[i] % 2 != 0:
        # Usamos pop(i) para eliminar el elemento en esa posición específica
        my_list.pop(i)

print(my_list)
