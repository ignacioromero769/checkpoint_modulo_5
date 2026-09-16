def mostrar_menu():
    print("--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
         opcion = int(input("Ingrese un numero: "))
    except ValueError:
        print("Por favor ingrese un numero")
        return
    return opcion
