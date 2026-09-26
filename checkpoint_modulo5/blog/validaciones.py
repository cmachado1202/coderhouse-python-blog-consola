from .datos import estados_post


def validar_post(post):
    if not isinstance(post, dict):
        return False, "el post no es un diccionario"
    for clave in ("id", "titulo", "contenido", "autor", "tags", "estado"):
        if clave not in post:
            return False, f"falta {clave}"
    if not isinstance(post["titulo"], str) or not post["titulo"].strip():
        return False, "título vacío"
    if not isinstance(post["contenido"], str) or not post["contenido"].strip():
        return False, "contenido vacío"
    if not isinstance(post["autor"], dict) or not post["autor"].get("nombre"):
        return False, "autor inválido"
    if not isinstance(post["tags"], list):
        return False, "tags inválidos"
    if post["estado"] not in estados_post:
        return False, "estado inválido"
    return True, "válido"
