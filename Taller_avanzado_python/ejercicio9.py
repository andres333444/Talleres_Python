# Ejercicio 9. Tabla de multiplicar avamzada

pares = 0
impares = 0
mayores_50 = 0

for i in range(1, 11):
    print(f"\nTABLA DEL {i}")
    
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
        
        if resultado % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
        if resultado > 50:
            mayores_50 = mayores_50 + 1

print("\n===== RESUME====")
print("Resultados pares:", pares)
print("Resultados impares:", impares)
print("Resultados mayores que 50:", mayores_50)