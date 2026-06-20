class MetaEntidad(type):

    clases_registradas = []

    def __new__(cls, nombre, bases, atributos):

        nueva_clase = super().__new__(cls, nombre, bases, atributos)

        cls.clases_registradas.append(nombre)

        print(f"Clase '{nombre}' registrada correctamente.")

        return nueva_clase