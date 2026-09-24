## Blog consola

El programa contiene una serie de posts y permite mostrarlos en la consola, buscar for titulo, buscar por tag, y validar los posts existentes

## Ejecutar 
Para ejecutar el programa se debe ejecutar el archivo main.py

```
python main.py
```

## Archivos
La carpeta principal es blog_consola, dentro se encuentran:

**main.py**: El archivo principal para la ejecucion del sistema.

**README.md**: Archivo que contiene informacion sobre el programa

**posts.json**: Archivo que guarda los datos de los posts y autor.

**blog/**: Contiene dentro los siguientes archivos:
	
**blog/__init__.py**: Archivo de python que le indica a python que la carpeta es un paquete.

**blog/datos.py**: Contiene los datos del programa: los datos del autor, los estados del post, etiquetas del blog, funciones para convertir objetos a diccionarios y diccionarios a objetos, funciones para guardar y cargar posts 
	
**blog/menu.py**: Se encarga de mostrar el menu y capturar la eleccion del usuario.

**blog/modelos.py**: Contiene las clases principales con sus metodos.
	
**blog/operaciones.py**: Se encarga de las operaciones como la busqueda, busqueda por tag, mostrar todos los posts, crear posts, y la asignacion automatica del autor

**blog/validaciones.py**: Contiene la funcion encargada de validar todos los posts

## Clases:
Las clases son

**Autor**: Contiene los datos del autor, ademas contiene metodos para convertirse a diccionario o de diccionario a objeto

**Post**: Contiene los datos principales de un post

**Blog**: Contiene metodos para realizar las principales operaciones del blog

### Como interactuan las clases con el archivo posts.json

Se guardan las instancias de los posts con el metodo guardar_posts de Blog. Se guardan en un archivo JSON. Para poder guardar objetos en un JSON estos se convierten a diccionarios.

Se cargan las instancias con el metodo cargar_posts. Se cargan desde el JSON. Se convierten los diccionarios a objetos nuevamente.

### Que cambio con respecto al checkpoint anterior
Se paso de usar diccionarios a objetos. Se creo un archivo persistente JSON. Ahora se puede crear posts internamente.