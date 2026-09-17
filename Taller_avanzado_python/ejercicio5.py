# Ejercicio 3. Factura de supermercado.
cantidad = int(input("Ingrese la cantidad de productos: "))

total_antes_del_descuento = 0
total_descuentos = 0
for i in range(cantidad):
    print(f"Producto {i + 1}")

    nombre_producto = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad: "))
    tipo = input("Tipo de producto(aseo/alimento/otro): ").lower

    subtotal = precio * cantidad
    descuento = 0

    if tipo == "alimento":
        descuento = subtotal * 0.05
    elif tipo == "aseo":
        if cantidad >= 3:
            descuento = subtotal * 0.10
    print("Subtotal: ",subtotal)
    print("Decuento: ",descuento)

    total_antes_del_descuento += subtotal
    total_descuentos += descuento

    descuento_adicional = 0
    if total_antes_del_descuento > 300000:
        descuento_adicional = total_antes_del_descuento * 0.05
        total_descuentos = total_descuentos + descuento_adicional
        print("\nSe aplicó un 5% adicional por superar $300.000")

    total_definitivo = total_antes_del_descuento - total_descuentos

    print("\n========== FACTURA ==========")
    print("Total antes de descuentos: $", total_antes_del_descuento)
    print("Total de descuentos: $", total_descuentos)
    print("Total definitivo a pagar: $", total_definitivo)