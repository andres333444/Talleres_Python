
# Ejercicio 10: Patrón numérico

n = int(input("Ingrese un nmero entre 3 y 10: "))

for i in range(1, n +  1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print() 

for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()