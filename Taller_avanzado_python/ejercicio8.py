# Ejercicio 8. Serie de Fibonacci

cantidad = int(input("Ingresee la cantidd de numeros: "))
a = 0
b = 1

suma = 0
pares = 0
impares = 0

print("\nSerie de Fibonacci:")
for i in range(cantidad):
    print(a, end=" ")
    suma = suma + a
    if a % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    
    siguiente = a + b
    a = b
    b = siguiente

print("\n")
print("Suma de los términos:", suma)
print("Términos pares:", pares)
print("Términos impares:", impares)