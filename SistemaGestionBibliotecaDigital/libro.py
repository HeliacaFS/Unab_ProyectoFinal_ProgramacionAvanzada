from metaclase import MetaEntidad


class Libro(metaclass=MetaEntidad):

    def __init__(self, titulo, autor, isbn, anio, paginas):

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio = anio
        self.paginas = paginas
        self.disponible = True

    def mostrar_info(self):

        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Año: {self.anio}")
        print(f"Páginas: {self.paginas}")
        print(f"Disponible: {self.disponible}")