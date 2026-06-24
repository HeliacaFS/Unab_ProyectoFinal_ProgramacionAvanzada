# gestor_libros.py
from decoradores import registrar_accion

class GestorLibros:
    def __init__(self):
        self.libros = []

    @registrar_accion
    def alta(self, libro):
        self.libros.append(libro)

    @registrar_accion
    def baja(self, isbn):
        self.libros = [l for l in self.libros if l.isbn != isbn]

    @registrar_accion
    def modificar(self, isbn, nuevo_titulo):
        for l in self.libros:
            if l.isbn == isbn:
                l.titulo = nuevo_titulo

    def listar(self):
        for l in self.libros:
            l.mostrar_info()
