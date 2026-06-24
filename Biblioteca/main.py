from usuario import Usuario
from administrador import Administrador
from libro import Libro
from prestamo import Prestamo
from gestor_libros import GestorLibros
from gestor_usuarios import GestorUsuarios
from gestor_prestamos import GestorPrestamos
from datetime import date

# --- Login ---
def login(gestor_usuarios, tipo):
    email = input("Email: ")
    dni = input("DNI: ")
    usuario = next((u for u in gestor_usuarios.usuarios if u.email == email and u.dni == dni), None)
    if usuario and ((tipo == "usuario" and isinstance(usuario, Usuario)) or 
                    (tipo == "admin" and isinstance(usuario, Administrador))):
        return usuario
    return None

# --- Menú Administrador ---
def menu_administrador(gestor_usuarios, gestor_libros):
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Alta usuario")
        print("2. Baja usuario")
        print("3. Listar usuarios")
        print("4. Alta libro")
        print("5. Baja libro")
        print("6. Listar libros")
        print("7. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            email = input("Email: ")
            usuario = Usuario(nombre, apellido, dni, email)
            gestor_usuarios.alta(usuario)
            print("Usuario agregado.")

        elif opcion == "2":
            dni = input("Ingrese DNI del usuario a eliminar: ")
            gestor_usuarios.baja(dni)
            print("Usuario eliminado.")

        elif opcion == "3":
            gestor_usuarios.listar()

        elif opcion == "4":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            anio = int(input("Año de publicación: "))
            paginas = int(input("Cantidad de páginas: "))
            libro = Libro(titulo, autor, isbn, anio, paginas)
            gestor_libros.alta(libro)
            print("Libro agregado.")

        elif opcion == "5":
            isbn = input("Ingrese ISBN del libro a eliminar: ")
            gestor_libros.baja(isbn)
            print("Libro eliminado.")

        elif opcion == "6":
            gestor_libros.listar()

        elif opcion == "7":
            break

        else:
            print("Opción inválida.")

# --- Menú Usuario ---
def menu_usuario(usuario, gestor_libros, gestor_prestamos):
    while True:
        print(f"\n--- Menú Usuario ({usuario.nombre}) ---")
        print("1. Listar libros")
        print("2. Solicitar préstamo")
        print("3. Devolver libro")
        print("4. Listar préstamos")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestor_libros.listar()

        elif opcion == "2":
            isbn = input("Ingrese ISBN del libro: ")
            libro = next((l for l in gestor_libros.libros if l.isbn == isbn), None)
            if not libro:
                print("Libro no encontrado.")
                continue

            if libro.disponible:
                prestamo = Prestamo(libro, usuario, date.today())
                gestor_prestamos.alta(prestamo)
                libro.disponible = False
                print("Préstamo registrado.")
            else:
                print("El libro ya está prestado.")

        elif opcion == "3":
            isbn = input("Ingrese ISBN del libro a devolver: ")
            prestamo = next((p for p in gestor_prestamos.prestamos if p.libro.isbn == isbn and not p.fecha_devolucion), None)
            if prestamo:
                prestamo.registrar_devolucion(date.today())
                print("Devolución registrada.")
            else:
                print("No se encontró préstamo activo para ese libro.")

        elif opcion == "4":
            gestor_prestamos.listar()

        elif opcion == "5":
            break

        else:
            print("Opción inválida.")

# --- Programa Principal ---
def main():
    gestor_libros = GestorLibros()
    gestor_usuarios = GestorUsuarios()
    gestor_prestamos = GestorPrestamos()

    # Crear un administrador por defecto
    admin = Administrador("Diego", "Fernández", "33333333", "admin@mail.com", "Coordinador")
    gestor_usuarios.alta(admin)

    while True:
        print("\n=== Sistema de Biblioteca Digital ===")
        print("1. Login Usuario")
        print("2. Login Administrador")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = login(gestor_usuarios, "usuario")
            if usuario:
                menu_usuario(usuario, gestor_libros, gestor_prestamos)
            else:
                print("Usuario no válido.")

        elif opcion == "2":
            usuario = login(gestor_usuarios, "admin")
            if usuario:
                menu_administrador(gestor_usuarios, gestor_libros)
            else:
                print("Administrador no válido.")

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
