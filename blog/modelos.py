from dataclasses import dataclass, field


ESTADOS = ("borrador", "publicado", "archivado")


@dataclass
class Autor:
    nombre: str
    bio: str = ""
    redes_sociales: list[str] = field(default_factory=list)

    def a_diccionario(self):
        return {"nombre": self.nombre, "bio": self.bio, "redes_sociales": self.redes_sociales}

    @classmethod
    def desde_diccionario(cls, datos):
        if not isinstance(datos, dict) or not isinstance(datos.get("nombre"), str):
            raise ValueError("El autor debe tener un nombre.")
        return cls(datos["nombre"], datos.get("bio", ""), datos.get("redes_sociales", []))


@dataclass
class Post:
    id: int
    titulo: str
    contenido: str
    autor: Autor
    tags: list[str]
    estado: str = "borrador"
    categoria: str = "General"

    def a_diccionario(self):
        return {"id": self.id, "titulo": self.titulo, "contenido": self.contenido,
                "autor": self.autor.a_diccionario(), "tags": self.tags,
                "estado": self.estado, "categoria": self.categoria}

    @classmethod
    def desde_diccionario(cls, datos):
        if not isinstance(datos, dict):
            raise ValueError("El post debe ser un diccionario.")
        try:
            return cls(id=datos["id"], titulo=datos["titulo"], contenido=datos["contenido"],
                       autor=Autor.desde_diccionario(datos["autor"]), tags=datos["tags"],
                       estado=datos["estado"], categoria=datos.get("categoria", "General"))
        except KeyError as error:
            raise ValueError(f"Falta el campo {error.args[0]} en un post.") from error


class Blog:
    def __init__(self, posts=None):
        self.posts = list(posts or [])

    def listar_posts(self):
        return list(self.posts)

    def buscar_por_titulo(self, termino):
        return [post for post in self.posts if termino.lower() in post.titulo.lower()]

    def filtrar_por_tag(self, tag):
        return [post for post in self.posts if any(tag.lower() == item.lower() for item in post.tags)]

    def crear_post(self, titulo, contenido, autor, tags, estado="borrador", categoria="General"):
        siguiente_id = max((post.id for post in self.posts), default=0) + 1
        post = Post(siguiente_id, titulo, contenido, autor, tags, estado, categoria)
        from .validaciones import validar_post
        errores = validar_post(post)
        if errores:
            raise ValueError("; ".join(errores))
        self.posts.append(post)
        return post

    def validar_posts(self):
        from .validaciones import validar_post
        return [(post, validar_post(post)) for post in self.posts]
