
# Ejercicio 1
print("Ejercicio 1:\n")
inversion = float(input("Ingrese el dinero a invertir: "))
ganancia_anual = inversion * 0.15
ganacia_mensual = ganancia_anual / 12

print("Ganancia anual: " + str(ganancia_anual))
print("Ganancia mensual: " + str(ganacia_mensual))

print("===================================\n")
print("Ejercio 2:\n")

total_ventas = 0
sueldo_base = float(input("Ingrese su sueldo base: "))
cantidad_de_ventas = 0

for i in range(1, 4):
    venta = float(input(f"ingrese la venta {i}: "))
    print(f"Venta {i}: {venta}")
    total_ventas += venta
    cantidad_de_ventas += 1
comision = total_ventas * 0.10 
sueldo_total = sueldo_base + comision


print(f"Total de ventas: ",{total_ventas})
print(f"Sueldo base: ",{sueldo_base})
print(f"comision: ",{comision})
print(f"sueldo total: ",{sueldo_total})
print("=================================\n")
    
#Ejerecicio 3
print("Ejercicio 3:\n")

compra = float(input("Ingrese el total de su compra: "))
descuento = compra * 0.15
total_con_descuento = compra - descuento
print(f"Total de compra: ",{compra})
print(f"Descuento (15%): ",{descuento})
print(f"Total con decuento: ",{total_con_descuento})
print("===============================================\n")

#Ejercicio 4
print("Ejercicio 4:\n")

print("Ingrese las notas de cada parcal: ")

notas = []
for i in range(1, 4):
    nota = float(input(f"parcial {i}: "))
    notas.append(nota)

nota_examen = float(input("Ingrese la nota de su examen: "))
nota_trabajo_final = float(input("Ingrese la nota de su trabajo final: "))

suma_parciales = sum(notas)
promedio_parciales = suma_parciales / 3
porcentaje_parciales = promedio_parciales * 0.40

porcentaje_examen = nota_examen * 0.50
porcentaje_trabajo_final = nota_trabajo_final * 0.10
nota_definitiva = (porcentaje_parciales + porcentaje_trabajo_final + porcentaje_examen)

print(f"nota parciales: ",{porcentaje_parciales})
print(f"nota examen final: ",{porcentaje_examen})
print(f"nota trabajo final: ",{porcentaje_trabajo_final})
print(f"nota definitiva: ",{nota_definitiva})
print("===============================================\n")

#Ejercicio 5
print("Ejercicio 5:\n")

cantidad_pesos = float(input("Ingrese la cantidad en pesos: "))
tasa_cambio = float(input("Ingrese el valor del dolar: "))

dolares = cantidad_pesos / tasa_cambio

print(f"{cantidad_pesos} pesos equivalen a {dolares} dolares")
print("==============================================\n")

#Ejercicio 6
print("Ejercicio 6:\n")

numero = float(input("Ingrese un número: "))

if numero < 0:
    absoluto = numero * -1
else:
    absoluto = numero

print(f"El valor absoluto de {numero} es {absoluto}")
print("==============================================\n")

#Ejercicio 7
print("Ejercicio 7:\n")

presion = float(input("Ingrese la presion: "))
volumen = float(input("Ingrese el volumen: "))
temperatura = float(input("Ingrese la temperatura: "))

masa = (presion * volumen) / (0.37 * (temperatura + 460))

print(f"La masa de aire es: {masa}")



                                                                      

