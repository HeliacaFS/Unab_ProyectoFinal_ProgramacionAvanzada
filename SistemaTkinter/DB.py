import sqlite3
from  libro import Libro


Base_Nombre = "biblioteca.db"

class BasedeDatos():
    def __init__(self):
        self.libros = []
    

    def crear_tabla(self,nombre_tabla, columnas):

        con = sqlite3.connect(Base_Nombre)
        cursor = con.cursor()

        query = f"""
        CREATE TABLE IF NOT EXISTS {nombre_tabla}
        (
            {columnas}
        )
        """

        cursor.execute(query)

        con.commit()
        con.close()
    def VerTablas(self):
        con = sqlite3.connect(Base_Nombre)
        cursor = con.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = cursor.fetchall()
        print("Tablas en la base de datos:")
        for tabla in tablas:
            print(tabla[0])

        con.close()
    def ver_Valores(self, nombre_tabla):
        con = sqlite3.connect(Base_Nombre)
        cursor = con.cursor()

        cursor.execute(f"SELECT * FROM {nombre_tabla}")
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)

        con.close()

class Gestor_usuarios:
  
    
    def agregar_usuario(self, usuario):
        con = sqlite3.connect(Base_Nombre)
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO tabla_usuarios (usuario, nombre, apellido, dni, email, contraseña, rango) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (usuario.usuario, usuario.nombre, usuario.apellido, usuario.dni, usuario.email, usuario.contraseña, usuario.rango)
        )
        con.commit()
        con.close()
    def eliminar_usuario(self, usuario):
        con = sqlite3.connect("bibloteca.db")
        cursor = con.cursor()
        cursor.execute(
            "DELETE FROM tabla_usuarios WHERE dni = ?",
            (usuario.dni,)
        )
        con.commit()
        con.close()
    def modificar_usuario(self):
        pass
    def buscar_usuario(self, dni):
        con = sqlite3.connect("bibloteca.db")
        cursor = con.cursor()
        cursor.execute(
            "SELECT * FROM tabla_usuarios WHERE dni = ?",
            (dni,)
        )
        usuario = cursor.fetchone()
        con.close()
        if usuario:
            return usuario
        else:
            return None
    def mostrar_usuario(self):
        pass
    def verificar_usuario(self,usuario,contraseña):
        con = sqlite3.connect(Base_Nombre)
        cursor = con.cursor()
        cursor.execute(
            "SELECT * FROM tabla_usuarios WHERE usuario = ? AND contraseña = ?",
            (usuario, contraseña)
        )
        usuario = cursor.fetchone()
        con.close()
        if usuario:
            return True
        else:
            return False


class Gestor_Libros:
    def agregar_libro(self, libro: Libro):
        con = sqlite3.connect(Base_Nombre)
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO tabla_libros (titulo, autor, Genero, isbn, anio, paginas, stock, disponible) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (libro.titulo, libro.autor, libro.genero, libro.isbn, libro.anio, libro.paginas, libro.stock, libro.disponible)
        )
        con.commit()  
        con.close()
        
        print(f"Libro '{libro.titulo}' guardado con éxito en la DB.")
    
    def eliminar_libro(self,libro):
        con = sqlite3.connect("bibloteca.db")
        cursor = con.cursor()
        cursor.execute(
            "DELETE FROM tabla_libro WHERE isbn = ?",
            (libro.isbn,)
        )
        con.commit()
        con.close()




class Gestor_Prestamo:
    pass

DB = BasedeDatos()
DB.crear_tabla(
    "tabla_libros",
    "Id_Libro INTEGER PRIMARY KEY AUTOINCREMENT, "
    "titulo VARCHAR(100) NOT NULL, "
    "autor VARCHAR(100) NOT NULL, "
    "Genero VARCHAR(100) NOT NULL, "
    "isbn VARCHAR(100) NOT NULL, "
    "anio INTEGER NOT NULL, "
    "paginas INTEGER NOT NULL, "
    "stock INTEGER NOT NULL DEFAULT 0, "
    "disponible BOOLEAN NOT NULL"
)

DB.crear_tabla("tabla_usuarios", 
    "id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, " \
    "usuario VARCHAR(100) NOT NULL UNIQUE, " \
    "nombre VARCHAR(100) NOT NULL, " \
    "apellido VARCHAR(100) NOT NULL, " \
    "dni VARCHAR(20) NOT NULL UNIQUE, " \
    "email VARCHAR(100) NOT NULL UNIQUE, " \
    "contraseña VARCHAR(255) NOT NULL, " \
    "rango VARCHAR(50) NOT NULL CHECK(rango IN ('Cliente', 'Bibliotecario'))")

DB.crear_tabla("tabla_prestamos",
    "id_prestamo INTEGER PRIMARY KEY AUTOINCREMENT, " \
    "id_usuario INTEGER NOT NULL, " \
    "id_libro INTEGER NOT NULL, " \
    "fecha_prestamo DATE NOT NULL, " \
    "fecha_devolucion DATE NOT NULL, " \
    "FOREIGN KEY (id_usuario) REFERENCES tabla_usuarios(id_usuario), " \
    "FOREIGN KEY (id_libro) REFERENCES tabla_libros(id_libro)")

libro1 = Libro(
    titulo="Cien años de soledad", 
    autor="Gabriel García Márquez", 
    genero="Realismo Mágico", 
    isbn="978-3-16-148410-0", 
    anio=1967, 
    paginas=417, 
    stock=5, 
)

libros = Gestor_Libros()
libros.agregar_libro(libro1)