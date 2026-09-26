import json
from pathlib import Path

from .modelos import Post
from .validaciones import validar_post


ARCHIVO_POSTS = Path(__file__).resolve().parent.parent / "posts.json"


def cargar_posts(ruta=ARCHIVO_POSTS):
    ruta = Path(ruta)
    if not ruta.exists():
        print("No se encontró posts.json. El blog comienza vacío.")
        return []
    try:
        texto = ruta.read_text(encoding="utf-8")
        datos = json.loads(texto)
        if not isinstance(datos, list):
            raise ValueError("La raíz del archivo debe ser una lista.")
        posts = [Post.desde_diccionario(item) for item in datos]
        for post in posts:
            errores = validar_post(post)
            if errores:
                raise ValueError("; ".join(errores))
        return posts
    except (OSError, json.JSONDecodeError, ValueError, TypeError) as error:
        print(f"No se pudieron cargar los posts: {error}. El blog comienza vacío.")
        return []


def guardar_posts(blog, ruta=ARCHIVO_POSTS):
    ruta = Path(ruta)
    for post, errores in blog.validar_posts():
        if errores:
            raise ValueError(f"El post {post.id} tiene errores: {'; '.join(errores)}")
    ruta.write_text(json.dumps([post.a_diccionario() for post in blog.posts],
                              ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
