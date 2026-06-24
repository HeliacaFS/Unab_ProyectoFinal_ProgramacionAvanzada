# usuario.py
from persona import Persona

class Usuario(Persona):
    def __init__(self, nombre, apellido, dni, email):
        super().__init__(nombre, apellido, dni, email)
        self.activo = True

    def mostrar_info(self):
        print(f"Usuario: {self.nombre} {self.apellido} ({'Activo' if self.activo else 'Inactivo'})")
