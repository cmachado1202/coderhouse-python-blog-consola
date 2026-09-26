perfil_autor = {
    "nombre": "Carolina Machado",
    "bio": "Escribe sobre aprendizaje y tecnología.",
    "redes_sociales": ["GitHub", "LinkedIn"],
}

estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"python", "datos", "python", "blog", "aprendizaje"}

posts = [
    {"id": 1, "titulo": "Empezar con Python", "contenido": "Una primera práctica en consola.",
     "autor": perfil_autor, "categoria": "Programación", "tags": ["python", "aprendizaje"], "estado": estados_post[1]},
    {"id": 2, "titulo": "Ordenar las ideas", "contenido": "Colecciones para organizar publicaciones.",
     "autor": perfil_autor, "categoria": "Organización", "tags": ["datos", "blog"], "estado": estados_post[0]},
    {"id": 3, "titulo": "Publicar una entrada", "contenido": "Una nota sobre el proceso de escritura.",
     "autor": perfil_autor, "categoria": "Escritura", "tags": ["blog", "aprendizaje"], "estado": estados_post[1]},
]

print("Autor del segundo post:", posts[1]["autor"]["nombre"])
print("Estados posibles:", estados_post)
print("Etiquetas sin duplicados:", etiquetas_blog)
print("Lista completa de posts:")
for post in posts:
    print(post)
