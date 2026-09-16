if __name__ == "__main__":
    from blog.datos import posts
    from blog.menu import mostrar_menu
    from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
    from blog.validaciones import validar_post

    while True:
        
        # Mostrar el menu
        opcion = mostrar_menu()
        if not opcion:
            continue

        # Listar posts
        if opcion == 1:
            listar_posts(posts)
            print("\n\n\n")

        # Busqueda por titulo
        elif opcion == 2:
            print("Ingrese el termino de busqueda: ")
            termino = input("Ingrese: ")

            buscar_por_titulo(posts, termino)
            print("\n\n\n")

        # Filtrar por tag            
        elif opcion == 3:
            print("Ingrese el tag: ")
            tag = input("Ingrese: ")
            filtrar_por_tag(posts, tag)
            print("\n\n\n")
            
        # Validar posts
        elif opcion == 4:
            print("Validando posts")
            for post in posts:
                es_valido, info = validar_post(post)

                if es_valido:
                    print(f"Post - '{post['titulo']}' - ID: {post['id']} - {info}")
                    
                elif info == None:
                    print(f"Post - ID: ??? No es un diccionario.")
                
                else:
                    post_id = post.get("id")
                    if not post_id:
                        post_id = "???"
                    print(f"Post - '{post.get('titulo')}' - ID {post_id} - no es valido. {info}")

            print("\n\n\n")
            
        # Salir    
        elif opcion == 5:
            print("Saliendo... ")
            break

        else:
            print("Por favor ingrese un numero valido")

    

