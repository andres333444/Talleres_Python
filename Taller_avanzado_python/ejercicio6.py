# Ejercicio 6. Estadisticas de numeros.

print("ingrese numeros enteros(El ceroo para terminar): ")

cantidad = 0
positivos = 0
negativos = 0
pares = 0
impares = 0
suma = 0
mayor = None
menor = None

while True:
    numero = int(input("Ingrese un número: "))
    
    if numero == 0:
        break
    cantidad = cantidad + 1
    suma = suma + numero

    if numero > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    if mayor is None or numero > mayor:
        mayor = numero
    if menor is None or numero < menor:
        menor = numero

print("\n===== RESULTADOS =====")

if cantidad == 0:
    print("No se ingresó ningún número (solo puso 0).")
else:
    print("Cantidad de números ingresados:", cantidad)
    print("Positivos:", positivos)
    print("Negativos:", negativos)
    print("Pares:", pares)
    print("Impares:", impares)
    print("Suma total:", suma)
    print("Promedio:", suma / cantidad)
    print("Número mayor:", mayor)
    print("Número menor:", menor)