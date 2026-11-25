import random

# Generar un número secreto aleatorio entre 1 y 10
secret_number = random.randint(1, 10)

print("¡Adivina el número secreto!")
print("Es un número del 1 al 10.")

# Pedir un número al usuario, para que adivine
attempt = int(input("Escribe tu número: "))

# Repetir mientras el usuario no adivine
while attempt != secret_number:
    print("Incorrecto, intenta de nuevo.")
    attempt = int(input("Escribe tu número: "))

print("¡Felicidades! Adivinaste el número.")