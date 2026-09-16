# Listar posts:
def listar_posts(lista):
    for post in lista:
        try:
            print(f"- {post['titulo']} | Autor: {post['autor']['nombre']}")
        except TypeError:
            print(f"- El post ID: {post['id']} no se pudo mostrar correctamente.")
        except KeyError:
            print(f"- El post ID: {post['id']} no se pudo mostrar correctamente.")
    print("\n\n\n")

# Busqueda:
def buscar_por_titulo(lista, termino):
    busqueda = termino.lower()
    busqueda = busqueda.strip()
    encontro = False
    if busqueda == "":
        print("Por favor ingrese un termino de busqueda")
        return
    for post in lista:
        try:
            if busqueda in post["titulo"].lower():
                encontro = True
                print(post["titulo"])
        except KeyError:
            continue
    if not encontro:
        print("No se encontraron resultados")

    print("\n\n\n")

# Filtrar: 
def filtrar_por_tag(lista, tag):
    tag_eleccion = tag.lower()
    tag_eleccion = tag_eleccion.strip()
    encontro = False
    if tag_eleccion == "":
        print("El tag esta vacio")
        return

    print (f"Posts con el tag {tag_eleccion}")
    for post in lista:
        try:
            for key_tag in post["tags"]:
                if tag_eleccion in key_tag.lower():
                    encontro = True
                    print(f"- {post['titulo']}")
        except KeyError:
            continue
    if not encontro:
        print("No se encontraron resultados")
    print("\n\n\n")
