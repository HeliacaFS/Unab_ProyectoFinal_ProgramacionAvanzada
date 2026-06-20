from persona import Persona


class Usuario(Persona):

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Email: {self.email}")