from sistema import SistemaGestionBibliotecaDigital
from libro import Libro
from usuario import Usuario

# Crear única instancia del sistema
sistema = SistemaGestionBibliotecaDigital()

while True:

    print("\n===== SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL =====")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Agregar usuario")
    print("4. Mostrar usuarios")
    print("5. Registrar préstamo")
    print("6. Mostrar préstamos activos")
    print("7. Registrar devolución")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        anio = int(input("Año de publicación: "))
        paginas = int(input("Cantidad de páginas: "))

        libro = Libro(titulo, autor, isbn, anio, paginas)

        sistema.gestor_libros.agregar_libro(libro)

    elif opcion == "2":

        sistema.gestor_libros.mostrar_libro()

    elif opcion == "3":

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        email = input("Correo electrónico: ")

        usuario = Usuario(nombre, apellido, dni, email)

        sistema.gestor_usuarios.agregar_usuario(usuario)

    elif opcion == "4":

        sistema.gestor_usuarios.mostrar_usuario()

    elif opcion == "5":

        isbn = input("ISBN del libro: ")
        dni = input("DNI del usuario: ")

        libro = sistema.gestor_libros.buscar_libro(isbn)
        usuario = sistema.gestor_usuarios.buscar_usuario(dni)

        if libro and usuario:

            sistema.gestor_prestamos.registrar_prestamo(libro, usuario)

        else:

            print("Libro o usuario no encontrado.")

    elif opcion == "6":

        sistema.gestor_prestamos.mostrar_activos()

    elif opcion == "7":

        isbn = input("ISBN del libro a devolver: ")

        prestamo = sistema.gestor_prestamos.buscar_prestamo(isbn)

        if prestamo:

            sistema.gestor_prestamos.registrar_devolucion(prestamo)

        else:

            print("Préstamo no encontrado.")

    elif opcion == "0":

        print("Programa finalizado.")
        break

    else:

        print("Opción inválida.")