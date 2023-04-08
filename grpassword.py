import random
import string

def generar_contrasena(longitud):
    # Definimos los caracteres que pueden estar en la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Usamos random para elegir caracteres al azar
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

# Pedimos al usuario que indique la longitud de la contraseña que quiere generar
longitud = int(input("Indica la longitud de la contraseña: "))

# Generamos la contraseña y la mostramos al usuario
contrasena_generada = generar_contrasena(longitud)
print("La contraseña generada es: ", contrasena_generada)
    
