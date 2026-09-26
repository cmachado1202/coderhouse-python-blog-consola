from .modelos import Autor, ESTADOS
from .operaciones import mostrar_posts, pedir_texto


def mostrar_menu():
    print("\n--- BLOG POR CONSOLA ---")
    print("1. Ver todos los posts\n2. Buscar por título\n3. Filtrar por tag")
    print("4. Crear post\n5. Validar posts\n6. Guardar en JSON\n7. Salir")
    try:
        return int(input("Elegí una opción: "))
    except ValueError:
        print("Ingresá un número del 1 al 7.")
        return 0


def ejecutar_menu(blog, guardar):
    while True:
        opcion = mostrar_menu()
        try:
            if opcion == 1:
                mostrar_posts(blog.listar_posts())
            elif opcion == 2:
                mostrar_posts(blog.buscar_por_titulo(pedir_texto("Título a buscar: ")))
            elif opcion == 3:
                mostrar_posts(blog.filtrar_por_tag(pedir_texto("Tag a filtrar: ")))
            elif opcion == 4:
                titulo = pedir_texto("Título: ")
                contenido = pedir_texto("Contenido: ")
                nombre = pedir_texto("Autor: ")
                tags = [tag.strip() for tag in input("Tags separados por coma: ").split(",") if tag.strip()]
                estado = input(f"Estado {ESTADOS} [borrador]: ").strip().lower() or "borrador"
                post = blog.crear_post(titulo, contenido, Autor(nombre), tags, estado)
                print(f"Post {post.id} creado. Usá la opción 6 para guardarlo.")
            elif opcion == 5:
                for post, errores in blog.validar_posts():
                    print(f"Post {post.id}: {'; '.join(errores) if errores else 'válido'}")
                if not blog.posts:
                    print("No hay posts para validar.")
            elif opcion == 6:
                guardar(blog)
                print("Posts guardados en posts.json.")
            elif opcion == 7:
                print("Hasta la próxima.")
                return
            elif opcion:
                print("Opción inexistente.")
        except (ValueError, OSError) as error:
            print(f"No se completó la operación: {error}")
