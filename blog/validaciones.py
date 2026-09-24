from blog.datos import estados_post

# Validar
def validar_post_funcion(post, clase_post, clase_autor):
    
    es_valido = True
    errores = []

    if not isinstance(post, clase_post):
        return False, None

    try:
        if not post.id:
            es_valido = False
            errores.append("Falta la ID.")
        elif not isinstance(post.id, int):
            es_valido = False
            errores.append("La ID no es un int")
    except AttributeError:
        es_valido = False
        errores.append("Falta el atributo: id.")
    try:
        if post.titulo == None:
            es_valido = False
            errores.append("Falta el titulo.")
    except AttributeError:
        es_valido = False
        errores.append("Falta el atributo: titulo.")
    try:
        if post.contenido == None:
            es_valido = False
            errores.append("Falta el contenido")
        elif not isinstance(post.contenido, str):
            es_valido = False
            errores.append("El contenido no es una string.")
        elif post.contenido.strip() == "":
            es_valido = False
            errores.append("El contenido esta vacio.")
    except AttributeError:
        es_valido = False
        errores.append("Falta el atributo: contenido.")
    # Validaciones de autor
    try:
        if not isinstance(post.autor, clase_autor):
            es_valido = False
            errores.append("El autor no es un objeto Autor.")
        else:
            try:
                if post.autor.nombre == None:
                    es_valido = False
                    errores.append("Falta el nombre del autor.")
                elif not isinstance(post.autor.nombre, str):
                    es_valido = False
                    errores.append("El nombre del autor no es una string.")
                elif post.autor.nombre.strip() == "" or post.autor.nombre == "Sin autor":
                    es_valido = False
                    errores.append("El post no tiene autor")
                if post.autor.bio == None:
                    es_valido = False
                    errores.append("La bio del autor es none")
                elif not isinstance(post.autor.bio, str):
                    es_valido = False
                    errores.append("La bio del autor no es una string")
                if post.autor.especialidad == None:
                    es_valido = False
                    errores.append("La especialidad del autor es none")
                elif not isinstance(post.autor.especialidad, str):
                    es_valido = False
                    errores.append("La especialidad del autor no es una string")
                if post.autor.redes_sociales == None:
                    es_valido = False
                    errores.append("Las redes sociales del autor son none")
                elif not isinstance(post.autor.redes_sociales, list):
                    es_valido = False
                    errores.append("Las redes sociales del autor no son una lista")
            except AttributeError:
                es_valido = False
                errores.append("Faltan atributos en autor")
    except AttributeError:
        es_valido = False
        errores.append("Falta el atributo: autor.")

    # Resto de las validaciones
    try:
        if post.tags == None:
            es_valido = False
            errores.append("Tags es None")
        elif not isinstance(post.tags, list):
            es_valido = False
            errores.append("Tags no es una lista.")
    except AttributeError:
        es_valido = False
        errores.append("Falta el atributo: tags.")
    try:
        if post.estado == None:
            es_valido = False
            errores.append("Falta el estado")
        elif not isinstance(post.estado, str):
            es_valido = False
            errores.append("Estado no es una string.")
        elif not post.estado in estados_post:
            es_valido = False
            errores.append("Estado no es uno de los estados validos")
    except AttributeError:
        es_valido = False
        errores.append("Falta el atributo: estado.")

    if es_valido:
        return True, "es valido"
    else:
        return False, errores

def validar_todos_posts_funcion(lista):
    from blog.modelos import Post, Autor
    
    for post in lista:
        es_valido, info = validar_post_funcion(post, clase_post=Post, clase_autor=Autor)
        if not es_valido:
            if info == None:
                print("Post ID ??? no es valido. No es una instancia de Post.")
                print()
            elif "Falta el atributo: titulo." in info:
                print(f"Post ID {post.id} no es valido.")
                for error in info:
                    print(f"-   {error}")
                print()
            else:
                print(f"Post ID {post.id} - {post.titulo} - no es valido")
                for error in info:
                    print(f"-   {error}")
                print()
                
        else:
            print(f"Post ID {post.id} - {post.titulo} es valido")
            print()









    
