
#Ejercicio 1. Clasificacion de triangulos
#Nombre: YAINER ANDRES BARRIOS YANEZ

print("Ingresa las longitudes de los tres lados: ")
lado1 = float(input("lado 1: "))
lado2 = float(input("lado 2: "))
lado3 = float(input("lado 3: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Error: Todos los lados deben ser positivos!!")
else:
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        print("Los lados si pueden formar un triangulo!!!")
        if lado1 == lado2 == lado3:
            print("TIPO: Equilatero!!")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("TIPO: Isosceles!!")
        else:
            print("TIPO: Escaleno!!")
    else:
         print("Los lados no pueden formar un triangulo!!")



