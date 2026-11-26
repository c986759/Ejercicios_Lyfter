print("---- Clasificador de Edad ----")

# Pedimos los datos al usuario
name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")
age = int(input("¿Cual es tu edad? "))


# Evaluar las condiciones hasta que calce en una
if age <= 4:
    message = "¡Eres un bebe, como hiciste para teclear genio!!!"
elif age <= 9:
    message = "Ya eres un niño"
elif age <= 12:
    message = "Eres un preadolescente"
elif age <= 18:
    message = "Eres un Adolescente"
elif age <= 40:
    message = "Eres un Adulto joven"
elif age <= 60:
    message = "Eres un Adulto"    
else:
    message = "Eres un Adulto Mayor"

# Mostramos su clasificación
print(f"{name}, tu clasificación es: ")
print(message)