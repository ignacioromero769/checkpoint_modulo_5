from blog.datos import estados_post

# Validar
def validar_post(post):

    if not isinstance(post, dict):
        return False, None

    if not post.get("id"):
        return False, "Falta la 'id'."
    if post.get("titulo") == None:
        return False, "Falta key 'titulo'."   
    if post.get("contenido") == None:
        return False, "Falta key 'contenido'."
    if post.get("autor") == None:
        return False, "Falta key 'autor'"
    if post.get("tags") == None:
        return False, "Falta key 'tags'"
    if post.get("estado") == None:
        return False, "Falta key 'estado'"

    if post["titulo"].strip() == "":
        return False, "Titulo vacio"
    if post["contenido"].strip() == "":
        return False, "Contenido vacio"

    if not isinstance(post["autor"], dict):
        return False, "El autor no es un diccionario"

    try:
        post["autor"]["nombre"]

    except KeyError:
        return False, "A autor le faltan keys obligatorias"

    if not isinstance(post["tags"], list):
        return False, "Tags no es una lista"

    if not post["estado"] in estados_post:
        return False, "El estado no es uno de los valores definidos"

    return True, "es valido"
