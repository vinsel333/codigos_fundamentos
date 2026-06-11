ficha = {}

ficha["nombre"] = input("Ingrese su nombre: ")
ficha["telefono"] = input("Ingrese su teléfono: ")
ficha["gmail"] = input("Ingrese su gmail: ")
ficha["edad"] = input("Ingrese su edad: ")

while True:

    print("\n---MENU---")
    print("1- Ver ficha")
    print("2- Editar dato")
    print("3- Salir")

    opc = int(input("¿Qué opción vas a elegir?: "))

    if opc == 1:
        print(ficha)

    elif opc == 2:
        campo = input("¿Qué dato quieres editar?: ")

        if campo in ficha:
            nuevo_valor = input("Nuevo valor: ")
            ficha[campo] = nuevo_valor
            print("Dato actualizado")
        else:
            print("Ese campo no existe")

    elif opc == 3:
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida")