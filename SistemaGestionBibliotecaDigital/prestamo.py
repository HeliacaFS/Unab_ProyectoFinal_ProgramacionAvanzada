from datetime import date
from metaclase import MetaEntidad


class Prestamo(metaclass=MetaEntidad):

    def __init__(self, libro, usuario):

        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None
        self.activo = True

    def registrar_devolucion(self):

        self.fecha_devolucion = date.today()
        self.activo = False
        self.libro.disponible = True

    def mostrar_info(self):

        print("Libro:", self.libro.titulo)
        print("Usuario:", self.usuario.nombre)
        print("Fecha préstamo:", self.fecha_prestamo)
        print("Activo:", self.activo)