El programa contiene una serie de posts y permite mostrarlos en la consola, buscar for titulo, buscar por tag, y validar los posts existentes

Para ejecutar el programa se debe ejecutar el archivo main.py

La carpeta principal es blog_consola, dentro se encuentran:

main.py: El archivo principal para la ejecucion del sistema.

README.md: Archivo que contiene informacion sobre el programa

blog/: Contiene dentro los siguientes archivos:
	
	datos.py: Contiene la base de datos del programa. posts, autor, tags, estados, etc.
	
	menu.py: Se encarga de mostrar el menu y capturar la eleccion del usuario.
	
	operaciones.py: Se encarga de las operaciones como la busqueda, busqueda por tag y mostrar todos los posts
	
	validaciones.py: Contiene la funcion encargada de validar todos los posts

El menu tiene las siguientes funciones:
	1. Ver todos los posts.
	2. Buscar por titulo.
	3. Filtrar por tag.
	4. Validar posts
	5. Salir

Para inciar el sistema ejecute main.py