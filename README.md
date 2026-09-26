# Blog por consola

Proyecto modular en Python para administrar publicaciones desde la terminal. Permite listar, buscar por título, filtrar por etiqueta, crear y validar posts, y guardar los cambios en `posts.json`.

## Ejecutar

Se requiere Python 3.10 o posterior. Desde esta carpeta:

```bash
python main.py
```

No hay dependencias externas. Para probar la persistencia, creá un post con la opción 4, guardá con la opción 6, salí y volvé a ejecutar el programa. Si el archivo JSON falta, está vacío o es inválido, el programa avisa y empieza con una lista vacía.

## Organización

- `main.py`: carga los datos, crea el blog y abre el menú.
- `blog/modelos.py`: `Autor` guarda los datos de la persona, `Post` representa cada publicación y `Blog` reúne las operaciones de la colección.
- `blog/datos.py`: convierte los objetos a diccionarios para guardarlos en JSON y reconstruye los objetos al cargar.
- `blog/menu.py`: interacción por consola.
- `blog/operaciones.py`: presentación y entrada de texto.
- `blog/validaciones.py`: reglas para comprobar los posts.
- `posts.json`: publicaciones iniciales y persistencia local.

La versión anterior trabajaba con funciones y diccionarios. Esta versión conserva la separación por módulos y agrega clases, composición entre `Post` y `Autor`, y carga y guardado en JSON.
