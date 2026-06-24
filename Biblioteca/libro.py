# libro.py
class Libro:
    def __init__(self, titulo, autor, isbn, anio, paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio = anio
        self.paginas = paginas
        self.disponible = True

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"{self.titulo} ({self.autor}) - {estado}")
