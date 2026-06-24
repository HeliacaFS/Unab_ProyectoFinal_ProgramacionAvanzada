import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

from db.conexion import obtener_conexion

class UsuarioRegistrado(tk.Toplevel):
    def __init__(self, parent, usuario_id):
        super().__init__(parent)
        self.title("Panel de Usuario")
        self.resizable(False, False)
        self.geometry("600x400")

        self.usuario_id = usuario_id
        
        conn = obtener_conexion()
        self.cursor = self.conn.cursor()

        # --- Campo de búsqueda ---
        frame_busqueda = tk.Frame(self)
        frame_busqueda.pack(pady=10)

        self.entry_busqueda = ttk.Entry(frame_busqueda, width=30)
        self.entry_busqueda.grid(row=0, column=0, padx=5)

        self.combo_filtro = ttk.Combobox(
            frame_busqueda,
            values=["nombre", "autor", "isbn", "categoria"],
            state="readonly",
            width=15
        )
        self.combo_filtro.current(0)
        self.combo_filtro.grid(row=0, column=1, padx=5)

        btn_buscar = tk.Button(frame_busqueda, text="Buscar", command=self.buscar_libro)
        btn_buscar.grid(row=0, column=2, padx=5)

        # --- Resultado de búsqueda ---
        self.lbl_resultado = ttk.Label(self, text="Resultado de búsqueda aparecerá aquí")
        self.lbl_resultado.pack(pady=10)

        self.btn_solicitar = tk.Button(
            self,
            text="Solicitar",
            state="disabled",
            bg="lightblue",
            width=12,
            command=self.solicitar_libro
        )
        self.btn_solicitar.pack(pady=5)

        # --- Lista de préstamos activos ---
        lbl_prestamos = ttk.Label(self, text="Préstamos activos:")
        lbl_prestamos.pack(pady=10)

        self.lista_prestamos = tk.Listbox(self, width=60, height=8)
        self.lista_prestamos.pack(pady=5)

        btn_devolver = tk.Button(
            self,
            text="Devolver libro",
            bg="orange",
            width=15,
            command=self.devolver_libro
        )
        btn_devolver.pack(pady=5)

        # --- Botón salir ---
        btn_salir = tk.Button(self, text="Salir", bg="red", fg="white", width=10, command=self.destroy)
        btn_salir.pack(pady=15)

        # Cargar préstamos activos
        self.cargar_prestamos()

    # --- Métodos ---
    def buscar_libro(self):
        criterio = self.combo_filtro.get()
        texto = self.entry_busqueda.get()

        self.cursor.execute(f"SELECT id, nombre, autor, disponible FROM libros WHERE {criterio} LIKE ?", (f"%{texto}%",))
        libro = self.cursor.fetchone()

        if libro:
            estado = "Disponible" if libro[3] == 1 else "No disponible"
            self.lbl_resultado.config(text=f"Libro: {libro[1]} - Autor: {libro[2]} - {estado}")
            self.libro_id = libro[0]
            self.btn_solicitar.config(state="normal" if libro[3] == 1 else "disabled")
        else:
            self.lbl_resultado.config(text="No se encontró el libro")
            self.btn_solicitar.config(state="disabled")

    def solicitar_libro(self):
        fecha = datetime.now().strftime("%d/%m/%Y")
        self.cursor.execute("INSERT INTO prestamos (usuario_id, libro_id, fecha) VALUES (?, ?, ?)",
                            (self.usuario_id, self.libro_id, fecha))
        self.cursor.execute("UPDATE libros SET disponible=0 WHERE id=?", (self.libro_id,))
        self.conn.commit()
        self.cargar_prestamos()
        self.btn_solicitar.config(state="disabled")
        messagebox.showinfo("Solicitud", "Libro solicitado con éxito")

    def devolver_libro(self):
        seleccion = self.lista_prestamos.curselection()
        if seleccion:
            texto = self.lista_prestamos.get(seleccion)
            libro_id = int(texto.split("|")[0].split(":")[1])  # extraer id del texto
            self.cursor.execute("DELETE FROM prestamos WHERE usuario_id=? AND libro_id=?", (self.usuario_id, libro_id))
            self.cursor.execute("UPDATE libros SET disponible=1 WHERE id=?", (libro_id,))
            self.conn.commit()
            self.cargar_prestamos()
            messagebox.showinfo("Devolución", "Libro devuelto correctamente")
        else:
            messagebox.showwarning("Atención", "Seleccione un préstamo para devolver")

    def cargar_prestamos(self):
        self.lista_prestamos.delete(0, tk.END)
        self.cursor.execute("""
            SELECT prestamos.libro_id, libros.nombre, prestamos.fecha
            FROM prestamos
            JOIN libros ON prestamos.libro_id = libros.id
            WHERE prestamos.usuario_id=?
        """, (self.usuario_id,))
        for libro_id, nombre, fecha in self.cursor.fetchall():
            self.lista_prestamos.insert(tk.END, f"ID:{libro_id} | {nombre} | Fecha: {fecha}")
