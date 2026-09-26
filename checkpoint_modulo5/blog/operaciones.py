from .validaciones import validar_post


def listar_posts(lista):
    if not lista:
        print("No se encontraron posts.")
    for post in lista:
        print(f'{post.get("titulo", "Sin título")} — {post.get("autor", {}).get("nombre", "Autor desconocido")}')


def buscar_por_titulo(lista, termino):
    return [post for post in lista if termino.lower() in post.get("titulo", "").lower()]


def filtrar_por_tag(lista, tag):
    return [post for post in lista if any(tag.lower() == item.lower() for item in post.get("tags", []))]


def validar_posts(lista):
    for numero, post in enumerate(lista, 1):
        valido, mensaje = validar_post(post)
        print(f"Post {numero}: {mensaje if valido else 'error - ' + mensaje}")
