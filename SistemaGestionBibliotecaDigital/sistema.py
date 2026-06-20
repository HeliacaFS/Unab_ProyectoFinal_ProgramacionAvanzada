from gestor_libros import GestorLibros
from gestor_usuarios import GestorUsuarios
from gestor_prestamos import GestorPrestamos


class SistemaGestionBibliotecaDigital:

    __instancia = None

    def __new__(cls):

        if cls.__instancia is None:

            cls.__instancia = super().__new__(cls)

            cls.__instancia.gestor_libros = GestorLibros()
            cls.__instancia.gestor_usuarios = GestorUsuarios()
            cls.__instancia.gestor_prestamos = GestorPrestamos()

        return cls.__instancia