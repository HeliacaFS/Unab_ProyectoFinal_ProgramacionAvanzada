import sqlite3
import csv
import os

def obtener_conexion():
    db_path = os.path.join(os.path.dirname(__file__), "biblioteca.db")
    return sqlite3.connect(db_path)

def cargar_libros_csv_si_vacio():
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM libros")
    cantidad = cursor.fetchone()[0]

    if cantidad == 0:
        dataset_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "dataset", "libros.csv")
        if os.path.exists(dataset_path):
            with open(dataset_path, newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        disponible = int(row["disponible"])
                    except (ValueError, KeyError):
                        disponible = 1
                    cursor.execute("""
                        INSERT INTO libros (nombre, autor, isbn, categoria, disponible)
                        VALUES (?, ?, ?, ?, ?)
                    """, (row["nombre"], row["autor"], row["isbn"], row["categoria"], disponible))
            conn.commit()
            print("Libros iniciales cargados desde CSV.")
        else:
            print("No se encontró el archivo libros.csv en assets/dataset/")
    else:
        print(f"La tabla ya tiene {cantidad} libros, no se cargó nada.")
    conn.close()
