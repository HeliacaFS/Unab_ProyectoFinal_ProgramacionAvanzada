from abc import ABC, abstractmethod
from metaclase import MetaEntidad


class Persona(ABC, metaclass=MetaEntidad):

    def __init__(self, nombre, apellido, dni, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email

    @abstractmethod
    def mostrar_info(self):
        pass