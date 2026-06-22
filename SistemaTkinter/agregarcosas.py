"""""from libro import Libro
libros = {
    1: Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", genero="Realismo Mágico", isbn="978-3-16-148410-0", anio=1967, paginas=417, stock=5),
    2: Libro(titulo="Don Quijote de la Mancha", autor="Miguel de Cervantes", genero="Novela", isbn="978-84-376-0494-7", anio=1605, paginas=863, stock=3),
    3: Libro(titulo="La sombra del viento", autor="Carlos Ruiz Zafón", genero="Misterio", isbn="978-84-08-05748-0", anio=2001, paginas=565, stock=7),
    4: Libro(titulo="Rayuela", autor="Julio Cortázar", genero="Novela", isbn="978-84-376-0495-4", anio=1963, paginas=600, stock=4),
    5: Libro(titulo="Pedro Páramo", autor="Juan Rulfo", genero="Realismo Mágico", isbn="978-968-16-0394-0", anio=1955, paginas=124, stock=6),
    6: Libro(titulo="El Aleph", autor="Jorge Luis Borges", genero="Cuento", isbn="978-84-376-0496-1", anio=1949, paginas=174, stock=8),
    7: Libro(titulo="1984", autor="George Orwell", genero="Distopía", isbn="978-0-452-28423-4", anio=1949, paginas=328, stock=10),
    8: Libro(titulo="Fahrenheit 451", autor="Ray Bradbury", genero="Distopía", isbn="978-0-7432-4722-1", anio=1953, paginas=256, stock=9),
    9: Libro(titulo="Orgullo y prejuicio", autor="Jane Austen", genero="Romántica", isbn="978-0-19-953556-9", anio=1813, paginas=432, stock=5),
    10: Libro(titulo="Crimen y castigo", autor="Fiódor Dostoyevski", genero="Novela", isbn="978-0-14-044913-6", anio=1866, paginas=671, stock=4),
    11: Libro(titulo="Los miserables", autor="Victor Hugo", genero="Novela", isbn="978-0-14-044430-8", anio=1862, paginas=1232, stock=6),
    12: Libro(titulo="Madame Bovary", autor="Gustave Flaubert", genero="Novela", isbn="978-0-14-044912-9", anio=1857, paginas=448, stock=5),
    13: Libro(titulo="Ulises", autor="James Joyce", genero="Modernismo", isbn="978-0-679-72232-9", anio=1922, paginas=730, stock=3),
    14: Libro(titulo="En busca del tiempo perdido", autor="Marcel Proust", genero="Novela", isbn="978-0-14-243796-4", anio=1913, paginas=4215, stock=2),
    15: Libro(titulo="El gran Gatsby", autor="F. Scott Fitzgerald", genero="Novela", isbn="978-0-7432-7356-5", anio=1925, paginas=180, stock=7),
    16: Libro(titulo="Moby Dick", autor="Herman Melville", genero="Aventura", isbn="978-0-14-243724-7", anio=1851, paginas=720, stock=4),
    17: Libro(titulo="La Odisea", autor="Homero", genero="Épica", isbn="978-0-14-026886-7", anio=-800, paginas=541, stock=6),
    18: Libro(titulo="La Ilíada", autor="Homero", genero="Épica", isbn="978-0-14-027536-0", anio=-750, paginas=704, stock=6),
    19: Libro(titulo="Hamlet", autor="William Shakespeare", genero="Tragedia", isbn="978-0-7434-7712-3", anio=1603, paginas=342, stock=8),
    20: Libro(titulo="Macbeth", autor="William Shakespeare", genero="Tragedia", isbn="978-0-7434-7713-0", anio=1606, paginas=249, stock=7),
    21: Libro(titulo="Romeo y Julieta", autor="William Shakespeare", genero="Tragedia", isbn="978-0-7434-7714-7", anio=1597, paginas=320, stock=9),
    22: Libro(titulo="El señor de los anillos", autor="J.R.R. Tolkien", genero="Fantasía", isbn="978-0-618-00222-8", anio=1954, paginas=1178, stock=10),
    23: Libro(titulo="El hobbit", autor="J.R.R. Tolkien", genero="Fantasía", isbn="978-0-618-00221-1", anio=1937, paginas=310, stock=8),
    24: Libro(titulo="Harry Potter y la piedra filosofal", autor="J.K. Rowling", genero="Fantasía", isbn="978-0-7475-3269-9", anio=1997, paginas=223, stock=12),
    25: Libro(titulo="Harry Potter y la cámara secreta", autor="J.K. Rowling", genero="Fantasía", isbn="978-0-7475-3849-3", anio=1998, paginas=251, stock=11),
    26: Libro(titulo="Harry Potter y el prisionero de Azkaban", autor="J.K. Rowling", genero="Fantasía", isbn="978-0-7475-4215-5", anio=1999, paginas=317, stock=11),
    27: Libro(titulo="Harry Potter y el cáliz de fuego", autor="J.K. Rowling", genero="Fantasía", isbn="978-0-7475-4624-5", anio=2000, paginas=636, stock=10),
    28: Libro(titulo="Harry Potter y la orden del Fénix", autor="J.K. Rowling", genero="Fantasía", isbn="978-0-7475-5100-3", anio=2003, paginas=766, stock=9),
    29: Libro(titulo="Harry Potter y el misterio del príncipe", autor="J.K. Rowling", genero="Fantasía", isbn="978-0-7475-8108-6", anio=2005, paginas=607, stock=9),
    30: Libro(titulo="Harry Potter y las reliquias de la muerte", autor="J.K. Rowling", genero="Fantasía", isbn="978-0-7475-9105-4", anio=2007, paginas=607, stock=10),
    31: Libro(titulo="El código Da Vinci", autor="Dan Brown", genero="Thriller", isbn="978-0-385-50420-8", anio=2003, paginas=689, stock=8),
    32: Libro(titulo="Ángeles y demonios", autor="Dan Brown", genero="Thriller", isbn="978-0-671-02735-4", anio=2000, paginas=616, stock=7),
    33: Libro(titulo="Inferno", autor="Dan Brown", genero="Thriller", isbn="978-0-385-53718-3", anio=2013, paginas=480, stock=6),
    34: Libro(titulo="El origen", autor="Dan Brown", genero="Thriller", isbn="978-0-385-54116-6", anio=2017, paginas=480, stock=6),
    35: Libro(titulo="La chica del tren", autor="Paula Hawkins", genero="Thriller", isbn="978-0-385-35062-1", anio=2015, paginas=395, stock=7),
    36: Libro(titulo="Gone Girl", autor="Gillian Flynn", genero="Thriller", isbn="978-0-307-58836-4", anio=2012, paginas=432, stock=7),
    37: Libro(titulo="El psicoanalista", autor="John Katzenbach", genero="Thriller", isbn="978-84-666-0569-9", anio=2002, paginas=512, stock=8)}

import sqlite3
from libro import Libro


con = sqlite3.connect("biblioteca.db")
cursor = con.cursor()

# Usamos .values() para iterar sobre los objetos Libro, no sobre los IDs
for libro in libros.values():
    cursor.execute(
        """"""  INSERT INTO tabla_libros
        (titulo, autor, Genero, isbn, anio, paginas, stock, disponible)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""""",
        (
            libro.titulo,
            libro.autor,
            libro.genero,
            libro.isbn,
            libro.anio,
            libro.paginas,
            libro.stock,
            # Como 'disponible' no está en tu objeto Libro, asumimos True si hay stock
            True if libro.stock > 0 else False 
        )
    )

con.commit()
con.close()

print(f"{len(libros)} libros cargados correctamente.")

"""""

from DB import Gestor_Prestamo

def ejecutar_prestamo_ejemplo():
    # 1. Instanciamos la clase que maneja los préstamos
    gestor = Gestor_Prestamo()
    
    # 2. Definimos las variables solicitadas
    usuario_id = 1
    libro_id = 1
    
    print("Iniciando proceso de préstamo...")
    
    # 3. Llamamos al método agregar_prestamo
    resultado = gestor.agregar_prestamo(usuarioID=usuario_id, LibroID=libro_id)
    
    # 4. Verificamos el resultado de la operación
    if resultado:
        print("¡Operación completada con éxito!")
    else:
        print("No se pudo registrar el préstamo. Verifica los errores en consola.")

if __name__ == "__main__":
    ejecutar_prestamo_ejemplo()