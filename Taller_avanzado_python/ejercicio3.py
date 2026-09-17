# Ejercicio 3. Numero primo

numero = int(input("Ingrese un numero mayor que 1: "))

divisores = []

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

print("Divisores: ", end=" ")
for d in divisores:
    print(d, end=" ")

print()

if len(divisores) == 2:
    print("El numero ", numero, "es primo")
else:
    print("El numero ", numero, "no es primo")