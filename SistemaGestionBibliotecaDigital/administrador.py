from persona import Persona


class Administrador(Persona):

    def __init__(self, nombre, apellido, dni, email, legajo, cargo):

        super().__init__(nombre, apellido, dni, email)

        self.legajo = legajo
        self.cargo = cargo

    def mostrar_info(self):

        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Email: {self.email}")
        print(f"Legajo: {self.legajo}")
        print(f"Cargo: {self.cargo}")