perfil_autor = {"nombre": "Carolina Machado", "bio": "Aprendizaje y tecnología", "redes_sociales": ["GitHub"]}
estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"python", "datos", "blog", "python"}
posts = [
    {"id": 1, "titulo": "Empezar con Python", "contenido": "Una primera práctica.", "autor": perfil_autor,
     "categoria": "Programación", "tags": ["python", "aprendizaje"], "estado": estados_post[1]},
    {"id": 2, "titulo": "Ordenar las ideas", "contenido": "Colecciones para el blog.", "autor": perfil_autor,
     "categoria": "Organización", "tags": ["datos", "blog"], "estado": estados_post[0]},
    {"id": 3, "titulo": "Publicar una entrada", "contenido": "Una nota sobre escritura.", "autor": perfil_autor,
     "categoria": "Escritura", "tags": ["blog", "aprendizaje"], "estado": estados_post[1]},
    {"id": 4, "titulo": "Entrada para revisar", "autor": perfil_autor,
     "categoria": "Escritura", "tags": ["blog"], "estado": estados_post[0]},
]


def mostrar_menu():
    print("\n--- MENÚ DEL BLOG ---")
    print("1. Ver todos los posts\n2. Buscar por título\n3. Filtrar por tag\n4. Validar posts\n5. Salir")
    try:
        return int(input("Elegí una opción: "))
    except ValueError:
        print("Ingresá un número del 1 al 5.")
        return 0


def listar_posts(lista):
    for post in lista:
        autor = post.get("autor", {})
        nombre = autor.get("nombre", "Autor desconocido") if isinstance(autor, dict) else "Autor desconocido"
        print(f'{post.get("titulo", "Sin título")} — {nombre}')


def buscar_por_titulo(lista, termino):
    return [post for post in lista if termino and termino.lower() in str(post.get("titulo", "")).lower()]


def filtrar_por_tag(lista, tag):
    return [post for post in lista if tag and isinstance(post.get("tags"), list)
            and any(tag.lower() == str(item).lower() for item in post["tags"])]


def validar_post(post):
    # Se revisa la estructura antes de acceder a sus datos.
    if not isinstance(post, dict):
        return False, "no es un diccionario"
    requeridas = ("id", "titulo", "contenido", "autor", "tags", "estado")
    for clave in requeridas:
        if clave not in post:
            return False, f'falta la clave "{clave}"'
    if not isinstance(post["titulo"], str) or not post["titulo"].strip():
        return False, "el título está vacío o es inválido"
    if not isinstance(post["contenido"], str) or not post["contenido"].strip():
        return False, "el contenido está vacío o es inválido"
    if not isinstance(post["autor"], dict) or not isinstance(post["autor"].get("nombre"), str) or not post["autor"]["nombre"].strip():
        return False, "el autor debe tener un nombre"
    if not isinstance(post["tags"], list):
        return False, "los tags deben ser una lista"
    if post["estado"] not in estados_post:
        return False, "estado desconocido"
    return True, "válido"


if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            listar_posts(posts)
        elif opcion in (2, 3):
            valor = input("Título a buscar: " if opcion == 2 else "Tag a filtrar: ").strip()
            if not valor:
                print("El valor no puede estar vacío.")
                continue
            resultados = buscar_por_titulo(posts, valor) if opcion == 2 else filtrar_por_tag(posts, valor)
            if resultados:
                listar_posts(resultados)
            else:
                print("No se encontraron resultados.")
        elif opcion == 4:
            for numero, post in enumerate(posts, 1):
                valido, mensaje = validar_post(post)
                print(f'Post {numero}: {"válido" if valido else "error - " + mensaje}')
        elif opcion == 5:
            print("Hasta la próxima.")
            break
        elif opcion:
            print("Opción inexistente.")
