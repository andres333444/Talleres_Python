# Ejercicio 4. Cajero automatico.

saldo = 1500000
contador_depositos = 0
contador_retiros = 0
comision = 4500

while True:
    print("====MENU====")
    print("1. Consultar saldo.")
    print("2. Depositar dinero.")
    print("3. Retirar dinero.")
    print("4. Ver moovimientos realizados.")
    print("5. Salir.")

    opcion = int(input("Elija una opcion: "))

    if opcion == 1:
        print("Usted tiene ", saldo, "en su cuenta.\n")

    if opcion == 2:
        deposito = float(input("Cuanto dinero desea depositar?: "))
        if deposito < 0:
            print("\n¡ERROR! No se permiten depositos negativos!\n")
        else:
            saldo_total = saldo + deposito
            print("\n[¡¡Deposito realizado!! ahora tienes: ", saldo_total, "en tu cuenta!!]\n")
            contador_depositos += 1

    if opcion == 3:
        retiro = float(input("Cuanto dinero desea retirar?: "))
        if retiro < 10000:
            print("\n¡ERROR! No se puede retirar menos de $10.000!\n")
        else:
            saldo = saldo - retiro - comision
            retiro_mas_comision = retiro + comision
            contador_retiros += 1

            print("\ndinero retirado: $",retiro)
            print("Comision: $",comision)
            print("Total retirado: ",retiro_mas_comision)
            print("Saldo actual: ",saldo,"\n")

    if opcion == 4:
        print("Cantidad de depositos: ",contador_depositos)
        print("Cantidad de retiros: ",contador_retiros,"\n")

    if opcion == 5:
        print("SALIENDO DEL CAJERO...")