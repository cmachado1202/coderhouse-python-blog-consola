from .modelos import Autor, ESTADOS, Post


def validar_post(post):
    errores = []
    if not isinstance(post, Post):
        return ["La publicación no es un Post."]
    if not isinstance(post.id, int) or isinstance(post.id, bool) or post.id <= 0:
        errores.append("El ID debe ser un entero positivo.")
    if not isinstance(post.titulo, str) or not post.titulo.strip():
        errores.append("El título no puede estar vacío.")
    if not isinstance(post.contenido, str) or not post.contenido.strip():
        errores.append("El contenido no puede estar vacío.")
    if not isinstance(post.autor, Autor) or not isinstance(post.autor.nombre, str) or not post.autor.nombre.strip():
        errores.append("El autor debe tener un nombre.")
    if not isinstance(post.tags, list) or any(not isinstance(tag, str) or not tag.strip() for tag in post.tags):
        errores.append("Los tags deben ser una lista de textos no vacíos.")
    if post.estado not in ESTADOS:
        errores.append("El estado no es válido.")
    return errores
