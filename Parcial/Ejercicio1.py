
estudiante = []
def agregrar_estudiante(lista):
    print("====AGREGAR Estudiante")

    nombre = str(input("ingrese su nombre: "))
    edad = int(input("Ingrese su edad: "))
    nota = float(input("Ingrese su nota: "))
  
    estudiante = {
    "nombre": nombre,
    "edad":  edad,
    "nota": nota
    }

    lista.append(estudiante)
    print("Estudiante agrergado a la lista!!")

def promedio_notas(lista): 
    if not lista:
        return 0.0

    suma_notas = sum(estudiante["nota"] for estudiante in lista)
    return suma_notas / len(lista)

agregrar_estudiante(estudiante)

def mejor_estudiante(lista):
    if not lista:
        return None
    mejor = lista[0]
    for alumno in lista:
        if alumno["nota"] > mejor["nota"]:
            mejor = alumno

        return mejor
estudiante_estrella = mejor_estudiante(estudiante)

print(f"promedio general:  {promedio_notas(estudiante)}")
print(f"mejor estdiante: {estudiante_estrella["nombre"]} con una nota de {estudiante_estrella["nota"]}" )