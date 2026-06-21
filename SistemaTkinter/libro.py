


class Libro():

    def __init__(self, titulo, autor,genero, isbn, anio, paginas,stock):

        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.isbn = isbn
        self.anio = anio
        self.paginas = paginas
        self.stock = stock
        if self.stock == 0:
            self.disponible = False
        elif self.stock < 0: 
            self.stock = 0
        else:
            self.disponible = True
        
    def mostrar_info(self):

        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Año: {self.anio}")
        print(f"Páginas: {self.paginas}")
        print(f"Disponible: {self.disponible}")


