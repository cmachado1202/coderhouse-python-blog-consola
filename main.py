from blog.datos import cargar_posts, guardar_posts
from blog.menu import ejecutar_menu
from blog.modelos import Blog


def main():
    blog = Blog(cargar_posts())
    ejecutar_menu(blog, guardar_posts)


if __name__ == "__main__":
    main()
