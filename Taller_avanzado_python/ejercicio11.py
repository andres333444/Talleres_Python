

import random

print("====JUEGO DE ADIVINANZA==")
print("1. Facil (1-20) - 6 intentos")
print("2. Intermedio (1-50) - 5 intentos")
print("3. Difiicil (1-100) - 4 intentos")

opcion = int(input("Elija la dificultad: "))

if opcion == 1:
    maximo = 20
    intentos = 6
elif opcion == 2:
    maximo = 50
    intentos = 5
elif opcion == 3:
    maximo = 100
    intentos = 4
else:
    print("Opción no válida")
    exit()

secreto = random.randint(1, maximo)
print(f"\nHe pensado un número entre 1 y {maximo}. ¡Adivina!")

while intentos > 0:
    print(f"\nTe quedan {intentos} intentos")
    adivinanza = int(input("Ingresa tu nuumero: "))

    if adivinanza == secreto:
        print("¡Número correcto!")
        puntaje = intentos * 20
        print("Tu puntaje es:", puntaje)
        break
    elif adivinanza < secreto:
        print("El numero secreto es mayor")
    else:
        print("El número secreto es menor")
    
    intentos = intentos - 1

if intentos == 0:
    print("\nSe acabaron los intentos.")
    print("El número secreto era:", secreto)
    print("Tu puntaje es: 0")
