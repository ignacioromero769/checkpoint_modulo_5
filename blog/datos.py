from pathlib import Path
import json

archivo_json = Path(__file__).parent.parent / "posts.json"

# Autor
autor_diccionario = {"nombre":"Jose Manuel",
                     "bio":"Programador experto en java",
                     "especialidad":"Java, Javascript y Python",
                     "redes_sociales":["@josemanueljava", "@programacionjavamanu"]}


# Tupla:
estados_post = ("borrador", "publicado", "archivado")

# Set:
etiquetas_blog = {"Python", "Django", "Web", "Backed", "Frontend", "Java",
                  "Python", "Javascript"}

def to_dict(objeto):
    diccionario = {}
    diccionario.update({"id":objeto.id})
    diccionario.update({"titulo":objeto.titulo})
    diccionario.update({"contenido":objeto.contenido})
    diccionario.update({"autor":objeto.autor.to_dict()})
    diccionario.update({"tags":objeto.tags})
    diccionario.update({"estado":objeto.estado})
    return diccionario

def to_obj(diccionario, clase_post, clase_autor):
    autor = clase_autor()
    objeto = clase_post()
    if not isinstance(diccionario, dict):
        return None
    objeto.id = diccionario.get("id")
    objeto.titulo = diccionario.get("titulo")
    objeto.contenido = diccionario.get("contenido")
    objeto.autor = autor.to_obj(diccionario.get("autor"))
    objeto.tags = diccionario.get("tags")
    objeto.estado = diccionario.get("estado")
    return objeto

def guardar_posts_funcion(lista):
    lista_diccionario = []
    for objeto in lista:
        lista_diccionario.append(to_dict(objeto))
    with open(archivo_json, mode="w", encoding="utf-8") as f:
        json.dump(lista_diccionario, f, ensure_ascii=False, indent=4)
    print("Posts guardados")

def cargar_posts_funcion():
    from blog.modelos import Post, Autor
    
    post_diccionario = []
    posts = []

    try:    
        with open(archivo_json, mode="r", encoding="utf-8") as f:
            post_diccionario = json.load(f)
        for diccionario in post_diccionario:
            posts.append(to_obj(diccionario, clase_post=Post, clase_autor=Autor))
        return posts
    
    except json.decoder.JSONDecodeError:
        return post_diccionario

    except FileNotFoundError:
        archivo = open(archivo_json, mode="w", encoding="utf-8")
        archivo.close
            
        return post_diccionario




    
