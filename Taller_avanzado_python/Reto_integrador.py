
# Reto Integrador - Sistema de Ventas

ventas = 0
total_antes = 0
total_descuentos = 0
total_recargos = 0
dinero_recibido = 0
venta_mayor = 0
venta_menor = 999999999
pagos_efectivo = 0
pagos_tarjeta = 0
pagos_transferencia = 0
clientes_con_descuento = 0

while True:
    print("\n===== SISTEMA DE VENTAS =====")
    print("1. Registrar una venta")
    print("2. Consultar resumen de ventas")
    print("3. Consultar venta mayor y menor")
    print("4. Definir cierre de caja")
    print("5. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        print("\n--- Registrar Venta ---")
        cliente = input("Nombre del cliente: ")
        
        cantidad = int(input("Cantidad de productos: "))
        while cantidad <= 0:
            print("La cantidad debe ser positiva")
            cantidad = int(input("Cantidad de productos: "))
        
        precio = float(input("Precio de cada producto: "))
        while precio <= 0:
            print("El precio debe ser positivo")
            precio = float(input("Precio de cada producto: "))
        
        subtotal = cantidad * precio
        descuento = 0
        recargo = 0

        if subtotal > 100000:
            descuento = subtotal * 0.10
            clientes_con_descuento += 1
        
        medio = input("Medio de pago (efectivo / tarjeta/transferencia): ").lower()
        
        if medio == "efectivo" and subtotal > 50000:
            descuento = descuento + (subtotal * 0.03)
            if subtotal <= 100000: 
                clientes_con_descuento += 1
        
        if medio == "tarjeta":
            recargo = subtotal * 0.02
            pagos_tarjeta += 1
        elif medio == "efectivo":
            pagos_efectivo += 1
        elif medio == "transferencia":
            pagos_transferencia += 1
        else:
            print("Medio de pago no válido. Se tomará como transferencia.")
            pagos_transferencia += 1
        
        total_pagar = subtotal - descuento + recargo
        ventas += 1
        total_antes += subtotal
        total_descuentos += descuento
        total_recargos += recargo
        dinero_recibido += total_pagar
        
        if total_pagar > venta_mayor:
            venta_mayor = total_pagar
        if total_pagar < venta_menor:
            venta_menor = total_pagar
        
        print("\nVenta registrada con exito")
        print("Subtotal: $", subtotal)
        print("Descuento: $", descuento)
        print("Recargo: $", recargo)
        print("Total a pagar: $", total_pagar)
    
    elif opcion == 2:
        if ventas == 0:
            print("\nAumn no se han registrado ventas.")
        else:
            print("\n====RESUMEN DE VENTAS====")
            print("Cantidad de ventas:", ventas)
            print("Valor total antes de descuentos: $", total_antes)
            print("Total de descuentos: $", total_descuentos)
            print("Total de recargos: $", total_recargos)
            print("Dinero definitivamente recibido: $", dinero_recibido)
            print("Promedio de las ventas: $", dinero_recibido / ventas)
            print("Cantidad de pagos en efectivo:", pagos_efectivo)
            print("Cantidad de pagos con tarjeta:", pagos_tarjeta)
            print("Cantidad de pagos por transferencia:", pagos_transferencia)
            print("Clientes que recibieron descuento:", clientes_con_descuento)
    
    elif opcion == 3:
        if ventas == 0:
            print("\nAun no se han registrado ventas.")
        else:
            print("\nVenta más alta: $", venta_mayor)
            print("Venta más baja: $", venta_menor)
    
    elif opcion == 4:
        if ventas == 0:
            print("\nAun no se han registrado ventas.")
        else:
            print("\n===CIERRE DE CAJA=====")
            print("Total de dinero recibido: $", dinero_recibido)
            print("Total de descuentos : $", total_descuentos)
            print("Total de recargos aplicados: $", total_recargos)
            print("Cantidad de ventas realizaadas:", ventas)
    
    elif opcion == 5:
        print("\nPrograma finalizado.")
        break
    
    else:
        print("Opción no valida. Intente de nuevo")