# prestamo.py
class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion=None):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def registrar_devolucion(self, fecha):
        self.fecha_devolucion = fecha
        self.libro.disponible = True

    def mostrar_info(self):
        if self.fecha_devolucion:
            print(f"{self.usuario.nombre} devolvió '{self.libro.titulo}' el {self.fecha_devolucion}")
        else:
            print(f"{self.usuario.nombre} tiene '{self.libro.titulo}' desde {self.fecha_prestamo}")
