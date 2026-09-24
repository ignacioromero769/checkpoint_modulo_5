from blog.datos import cargar_posts_funcion, archivo_json, guardar_posts_funcion
from blog.operaciones import crear_post_funcion, listar_posts_funcion, buscar_por_titulo_funcion, filtrar_por_tag_funcion
from blog.validaciones import validar_todos_posts_funcion

class Autor:
    def __init__(self):
        self.nombre = "Sin autor"
        self.bio = ""
        self.especialidad = ""
        self.redes_sociales = []

    def to_dict(self):
        diccionario = {}
        diccionario.update({"nombre":self.nombre})
        diccionario.update({"bio":self.bio})
        diccionario.update({"especialidad":self.especialidad})
        diccionario.update({"redes_sociales":self.redes_sociales})
        return diccionario

    def to_obj(self, diccionario):
        if not isinstance(diccionario, dict):
            return self
        self.nombre = diccionario.get("nombre")
        self.bio = diccionario.get("bio")
        self.especialidad = diccionario.get("especialidad")
        self.redes_sociales = diccionario.get("redes_sociales")
        return self

class Post:
    def __init__(self):
        self.id = 0
        self.titulo = ""
        self.contenido = ""
        self.autor = None
        self.tags = []
        self.estado = ""

class Blog:
    def listar_posts(self, lista):
        listar_posts_funcion(lista)

    def buscar_por_titulo(self, lista):
        print("Ingrese el termino de busqueda: ")
        termino = input("Ingrese: ")

        buscar_por_titulo_funcion(lista, termino)
        print("\n\n\n")

    def filtrar_por_tag(self, lista):
        print("Ingrese el tag: ")
        tag = input("Ingrese: ")
        filtrar_por_tag_funcion(lista, tag)
        print("\n\n\n")

    def crear_post(self, lista, autor):
        print("Creando post")
        print("\n\n\n")
        crear_post_funcion(lista, autor)

    def validar_posts(self, lista):
        print("Validando posts")
        print("\n")
        validar_todos_posts_funcion(lista)

    def cargar_posts(self):
        print("Cargando posts...")
        print("\n")
        posts = cargar_posts_funcion()
        return posts
    
    def guardar_posts(self, lista):
        print("Guardando posts...")
        print("\n")
        guardar_posts_funcion(lista)









        
    
