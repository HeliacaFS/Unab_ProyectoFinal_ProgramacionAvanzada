from decoradores import registrar_accion


class GestorLibros:

    def __init__(self):

        self.libros = []

    @registrar_accion
    def agregar_libro(self, libro):

        self.libros.append(libro)

    @registrar_accion
    def eliminar_libro(self, libro):

        self.libros.remove(libro)

    def modificar_libro(self):

        pass

    def buscar_libro(self, isbn):

        for libro in self.libros:

            if libro.isbn == isbn:

                return libro

        return None

    def mostrar_libro(self):

        for libro in self.libros:

            libro.mostrar_info()