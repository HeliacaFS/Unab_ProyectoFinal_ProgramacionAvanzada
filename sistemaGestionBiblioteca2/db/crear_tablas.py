import sqlite3
import os

# Crear carpeta db si no existe
if not os.path.exists("db"):
    os.makedirs("db")

conn = sqlite3.connect("db/biblioteca.db")
cursor = conn.cursor()

# Tabla de libros
cursor.execute("""
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    autor TEXT,
    isbn TEXT,
    categoria TEXT,
    disponible INTEGER
)
""")

# Tabla de préstamos
cursor.execute("""
CREATE TABLE IF NOT EXISTS prestamos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    libro_id INTEGER,
    fecha TEXT
)
""")

# Tabla de usuarios con contraseña
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellido TEXT,
    dni TEXT,
    email TEXT UNIQUE,
    contraseña TEXT
)
""")

conn.commit()
conn.close()

print("Tablas creadas correctamente.")
