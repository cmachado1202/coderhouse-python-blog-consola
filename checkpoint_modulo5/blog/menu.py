from .operaciones import buscar_por_titulo, filtrar_por_tag, listar_posts, validar_posts


def mostrar_menu():
    print("\n--- MENÚ DEL BLOG ---")
    print("1. Ver posts\n2. Buscar por título\n3. Filtrar por tag\n4. Validar posts\n5. Salir")
    try:
        return int(input("Opción: "))
    except ValueError:
        print("Ingresá un número.")
        return 0


def iniciar_menu(posts):
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            listar_posts(posts)
        elif opcion in (2, 3):
            termino = input("Título: " if opcion == 2 else "Tag: ").strip()
            if not termino:
                print("El texto no puede estar vacío.")
                continue
            resultado = buscar_por_titulo(posts, termino) if opcion == 2 else filtrar_por_tag(posts, termino)
            listar_posts(resultado)
        elif opcion == 4:
            validar_posts(posts)
        elif opcion == 5:
            print("Hasta la próxima.")
            break
        else:
            print("Opción inexistente.")
