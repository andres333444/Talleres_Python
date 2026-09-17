
# Ejercicio 2. Sistema de calificaciones.

print("=====SISTEMA DE CALIFICACIONES=====")

aprobados = 0
reprobados = 0
suma_promedios = 0
promedio_mas_alto = 0
promedio_mas_bajo = 5

cantidad = int(input("Ingresela cantidad de estudiantes: "))
for i in range(cantidad):
    print(f"Estudiante {i + 1}")

    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("ingrese la nota 3: "))

    promedio = (nota1 + nota2 + nota3) / 3   
    print("Su promedio es: " + str(promedio))
    if promedio <= 2.9:
        print("Clasificacion: Reprobado.")
        reprobados += 1
    elif promedio <= 3.9:
        print("Clasificacion: Aprobado.")
        aprobados += 1
    elif promedio <= 4.5:
        print("Clasificacion: Sobresaliente.") 
        aprobados += 1   
    elif promedio <= 5.0:
        print("Clasificacion: Exelente.")
        aprobados += 1

    suma_promedios = suma_promedios + promedio
    if promedio > promedio_mas_alto:
       promedio_mas_alto = promedio

    if promedio < promedio_mas_bajo:
       promedio_mas_bajo = promedio 
print("Cantidad de aprobados: " + str(aprobados))
print("Cantidad de reprobados: " + str(reprobados))
print("Promedio general: " + str(suma_promedios / cantidad))    
print("Promedio mas alto: " + str(promedio_mas_alto))
print("Promedio mas bajo: " + str(promedio_mas_bajo))
    