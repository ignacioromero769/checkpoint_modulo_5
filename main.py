if __name__ == "__main__":
    from blog.menu import mostrar_menu
    from blog.modelos import Blog, Post, Autor
    from blog.operaciones import asignar_autor
    blog = Blog()
    autor = asignar_autor(Autor)
    posts = blog.cargar_posts()

    while True:

        # Mostrar el menu
        opcion = mostrar_menu()
        if not opcion:
            continue

        # Listar posts
        elif opcion == 1:
            blog.listar_posts(posts)

        # Busqueda por titulo
        elif opcion == 2:
            blog.buscar_por_titulo(posts)

        # Filtrar por tag
        elif opcion == 3:
            blog.filtrar_por_tag(posts)
        
        # Crear post
        elif opcion == 4:
            blog.crear_post(posts, autor=autor)

        # Validar posts
        elif opcion == 5:
            blog.validar_posts(posts)

        # Guardar posts
        elif opcion == 6:
            blog.guardar_posts(posts)

        # Salir
        elif opcion == 7:
            print("Saliendo")
            break

        # Opcion invalida
        else:
            print("Por favor ingrese un numero valido")
        print("\n\n\n")

    
    
