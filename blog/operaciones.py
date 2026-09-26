def mostrar_posts(posts):
    if not posts:
        print("No se encontraron posts.")
        return
    for post in posts:
        print(f"{post.id}. {post.titulo} — {post.autor.nombre} ({post.estado})")


def pedir_texto(etiqueta):
    valor = input(etiqueta).strip()
    if not valor:
        raise ValueError("Este campo no puede quedar vacío.")
    return valor
