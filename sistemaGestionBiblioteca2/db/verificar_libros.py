import sqlite3

conn = sqlite3.connect("db/biblioteca.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM libros")
cantidad = cursor.fetchone()[0]

print(f"📚 Cantidad de libros en la tabla: {cantidad}")

conn.close()
