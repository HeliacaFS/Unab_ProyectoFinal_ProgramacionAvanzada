from decoradores import registrar_accion
from prestamo import Prestamo


class GestorPrestamos:

    def __init__(self):

        self.prestamos = []

    @registrar_accion
    def registrar_prestamo(self, libro, usuario):

        if libro.disponible:

            prestamo = Prestamo(libro, usuario)

            self.prestamos.append(prestamo)

            libro.disponible = False

        else:

            print("El libro ya tiene un préstamo activo.")

    @registrar_accion
    def registrar_devolucion(self, prestamo):

        prestamo.registrar_devolucion()

    def buscar_prestamo(self, isbn):

        for prestamo in self.prestamos:

            if prestamo.libro.isbn == isbn and prestamo.activo:

                return prestamo

        return None

    def mostrar_activos(self):

        for prestamo in self.prestamos:

            if prestamo.activo:

                prestamo.mostrar_info()