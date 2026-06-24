import tkinter as tk
from ui.interfaz import Main
from db.conexion import cargar_libros_csv_si_vacio

def main():
    # Cargar libros desde CSV si la tabla está vacía
    cargar_libros_csv_si_vacio()

    # Iniciar la interfaz principal
    root = tk.Tk()
    root.title("Sistema de Gestión de Biblioteca Digital")
    app = Main(root)
    root.mainloop()

if __name__ == "__main__":
    main()
