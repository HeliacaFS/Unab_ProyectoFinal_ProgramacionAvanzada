# administrador.py
from persona import Persona

class Administrador(Persona):
    def __init__(self, nombre, apellido, dni, email, cargo):
        super().__init__(nombre, apellido, dni, email)
        self.cargo = cargo

    def mostrar_info(self):
        print(f"Administrador: {self.nombre} {self.apellido} - Cargo: {self.cargo}")
