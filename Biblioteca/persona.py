# persona.py
class Persona:
    def __init__(self, nombre, apellido, dni, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email

    def mostrar_info(self):
        print(f"{self.nombre} {self.apellido} - DNI: {self.dni}")
