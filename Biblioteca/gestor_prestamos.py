# gestor_prestamos.py
from decoradores import registrar_accion

class GestorPrestamos:
    def __init__(self):
        self.prestamos = []

    @registrar_accion
    def alta(self, prestamo):
        # Registrar un nuevo préstamo
        self.prestamos.append(prestamo)

    @registrar_accion
    def baja(self, prestamo):
        # Eliminar un préstamo
        if prestamo in self.prestamos:
            self.prestamos.remove(prestamo)

    def listar(self):
        # Mostrar todos los préstamos
        for p in self.prestamos:
            p.mostrar_info()
