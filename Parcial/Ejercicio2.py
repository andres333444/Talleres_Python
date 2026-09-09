
inventario = [
    (101, "arroz", 1500.0, 5),
    (102, "mais", 2000.0, 4),
    (103, "tomates", 3000.0, 5)
]

def buscar_producto(inventario, codigo):
    for producto in inventario:
        if producto[0] == codigo:
            return producto

def valor_total(inventario):
    suma_total = 0.0
    for producto in inventario:
        subtotal = producto[2] * producto[3] 
        suma_total = suma_total + subtotal
    return suma_total

def actualizar_stock(inventario, codigo, nueva_cantidad):
    for i in range(len(inventario)):
        producto = inventario[i]

        if producto[0] == codigo:
            tupla_modificada = (producto[0], producto[1], producto[2], nueva_cantidad)
            inventario[i] = tupla_modificada
        print(f"stock actualizado para el código {codigo}")
        return

print("inventario actual: ")
print("Codigo\tNombre\tPrecio\tCantidad\tValor Total")

for p in inventario:
    subtotal = p[2] * p[3]
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t\t{subtotal}")

total_general = valor_total(inventario)
print(f"\nValor Total del Inventario: {total_general}")