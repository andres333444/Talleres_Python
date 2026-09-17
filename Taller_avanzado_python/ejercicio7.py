
# Ejercicio 7. Conversion decimal a binario.

numero = int(input("Ingrese un número entero positivo: "))
original = numero
binario = ""

while numero > 0:
    residuo = numero % 2         
    binario = str(residuo) + binario 
    numero = numero // 2
    
print("Número decimal:", original)
print("Resultado binario:", binario)