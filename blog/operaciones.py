from blog.datos import autor_diccionario

# Listar posts:
def listar_posts_funcion(lista):
    if lista:
        for post in lista:
            try:
                print(f"- {post.titulo} | Autor: {post.autor.nombre} | Estado: {post.estado}")
            except AttributeError:
                try:
                    print(f"- El post ID {post.id} no se puede mostrar correctamente.")
                except AttributeError:
                    print(f"- El post ID ??? no se puede mostrar correctamente.")
    else:
        print("No hay posts para mostrar")
    
# Busqueda:
def buscar_por_titulo_funcion(lista, termino):
    busqueda = termino.lower()
    busqueda = busqueda.strip()
    encontro = False
    if busqueda == "":
        print("Por favor ingrese un termino de busqueda")
        return
    for post in lista:
        try:
            if busqueda in post.titulo.lower():
                encontro = True
                print(f"{- post.titulo})
        except AttributeError:
            continue
        except TypeError:
            continue
    if not encontro:
        print("No se encontraron resultados")

    print("\n\n\n")

# Filtrar: 
def filtrar_por_tag_funcion(lista, tag):
    tag_eleccion = tag.lower()
    tag_eleccion = tag_eleccion.strip()
    encontro = False
    if tag_eleccion == "":
        print("El tag esta vacio")
        return

    print (f"Posts con el tag {tag_eleccion}")
    for post in lista:
        try:
            for elemento_tag in post.tags:
                if tag_eleccion in elemento_tag.lower():
                    encontro = True
                    print(f"- {post.titulo}")
                    break
        except AttributeError:
            continue
        except TypeError:
            continue
    if not encontro:
        print("No se encontraron resultados")
    print("\n\n\n")

# Crear post
def crear_post_funcion(lista, autor):
    from blog.modelos import Post

    # Recolectar los datos del usuario
    print("Ingrese el titulo: ")
    titulo = input("Ingrese: ")
    print()
    print("Ingrese el contenido: ")
    contenido = input("Ingrese: ")
    print()
    tags = []
    while True:
        print("Ingrese un tag: ")
        print("Ingrese 'seguir' para continuar")
        print()
        eleccion_tag = input("Ingrese un tag, 'seguir' para continuar: ")
        if eleccion_tag == "seguir":
            break
        if eleccion_tag.strip() == "":
            continue
        else:
            tags.append(eleccion_tag)
    print()
    while True:
        print("Elija que hacer con el post: ")
        print()
        print("1. Dejar en borrador")
        print("2. Publicar")
        print("3. Archivar")
        print()
        eleccion_estado = input("Ingrese un numero: ")
        if eleccion_estado == "1":
            estado = "borrador"
            break
        elif eleccion_estado == "2":
            estado = "publicado"
            break
        elif eleccion_estado == "3":
            estado = "archivado"
            break
        else:
            print("No se entendio la eleccion.")

    # Agregar los datos al objeto
    lista_de_ids = []
    for objeto in lista:
        if not objeto.id:
            continue
        elif isinstance(objeto.id, int):
            lista_de_ids.append(objeto.id)

    objeto_post = Post()

    if lista_de_ids:     
        objeto_post.id = max(lista_de_ids) + 1
    else:
        objeto_post.id = 1

    if titulo.strip() == "":
        titulo = "Post sin titulo"
    objeto_post.titulo = titulo
    objeto_post.contenido = contenido
    objeto_post.autor = autor
    objeto_post.tags = tags
    objeto_post.estado = estado
    lista.append(objeto_post)
    print("Post creado.")

def asignar_autor(clase_autor):
    autor = clase_autor()
    autor.nombre = autor_diccionario["nombre"]
    autor.bio = autor_diccionario["bio"]
    autor.especialidad = autor_diccionario["especialidad"]
    autor.redes_sociales = autor_diccionario["redes_sociales"]
    return autor






