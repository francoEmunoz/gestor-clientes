import helpers
import database as db

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("[1] Mostrar clientes    ")
        print("[2] Buscar cliente      ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Mostrando los clientes...\n")
            for c in db.Clientes.lista:
                print(c)


        elif opcion == '2':
            print("Buscando un cliente...\n")

            dni = helpers.leer_texto(
                8, 8, "DNI (8 chars)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado.")


        elif opcion == '3':
            print("Añadiendo un cliente...\n")
          
            dni = None
            while True:
                dni = helpers.leer_texto(
                    8, 8, "DNI (8 chars)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break
            nombre = helpers.leer_texto(
                2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(
                2, 30, "Apellido (de 2 a 30 chars)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")


        elif opcion == '4':
            print("Modificando un cliente...\n")

            dni = helpers.leer_texto(
                8, 8, "DNI (8 chars)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(
                    2, 30, f"Nombre (de 2 a 30 chars) [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(
                    2, 30, f"Apellido (de 2 a 30 chars) [{cliente.apellido}]").capitalize()
                db.Clientes.editar(cliente.dni, nombre, apellido)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")


        elif opcion == '5':
            print("Borrando un cliente...\n")

            dni = helpers.leer_texto(
                8, 8, "DNI (8 chars)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                db.Clientes.borrar(dni)
                print('Cliente borrado correctamente.')
            else:
                print('Cliente no encontrado.')


        elif opcion == '6':
            print("Saliendo...\n")   
            break

        input("\nPresiona ENTER para continuar...")