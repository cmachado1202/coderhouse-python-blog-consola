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
]

while True:
    print("\n--- MENÚ DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por título")
    print("3. Filtrar por tag")
    print("4. Salir")
    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        for post in posts:
            print(f'{post["titulo"]} — {post["autor"]["nombre"]}')
    elif opcion == "2":
        termino = input("Título a buscar: ").strip().lower()
        resultados = [post for post in posts if termino and termino in post["titulo"].lower()]
        for post in resultados:
            print(f'{post["titulo"]} — {post["autor"]["nombre"]}')
        if not resultados:
            print("No se encontraron posts con ese título.")
    elif opcion == "3":
        tag = input("Tag a filtrar: ").strip().lower()
        resultados = [post for post in posts if tag and any(tag == item.lower() for item in post["tags"])]
        for post in resultados:
            print(f'{post["titulo"]} — {post["autor"]["nombre"]}')
        if not resultados:
            print("No se encontraron posts con ese tag.")
    elif opcion == "4":
        print("Hasta la próxima.")
        break
    else:
        print("Opción inválida. Elegí un número del 1 al 4.")
