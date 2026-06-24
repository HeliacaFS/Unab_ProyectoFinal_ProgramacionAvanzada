import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from db.conexion import obtener_conexion



class RegistroUsuario(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registro de Nuevo Usuario")
        self.geometry("400x400")
        self.resizable(False, False)

        ttk.Label(self, text="Nuevo Usuario", font=("Arial", 14, "bold")).pack(pady=10)

        # Campos
        ttk.Label(self, text="Nombre:").pack(pady=3)
        self.entry_nombre = ttk.Entry(self)
        self.entry_nombre.pack()

        ttk.Label(self, text="Apellido:").pack(pady=3)
        self.entry_apellido = ttk.Entry(self)
        self.entry_apellido.pack()

        ttk.Label(self, text="DNI:").pack(pady=3)
        self.entry_dni = ttk.Entry(self)
        self.entry_dni.pack()

        ttk.Label(self, text="Email:").pack(pady=3)
        self.entry_email = ttk.Entry(self)
        self.entry_email.pack()

        # 🔹 Campo de contraseña
        ttk.Label(self, text="Contraseña:").pack(pady=3)
        self.entry_contraseña = ttk.Entry(self, show="*")
        self.entry_contraseña.pack()

        # Botones
        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=15)

        btn_crear = tk.Button(frame_botones, text="Crear", bg="lightgreen", command=self.crear_usuario)
        btn_crear.grid(row=0, column=0, padx=10)

        btn_limpiar = tk.Button(frame_botones, text="Limpiar campos", bg="beige", command=self.limpiar_campos)
        btn_limpiar.grid(row=0, column=1, padx=10)

    def crear_usuario(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        dni = self.entry_dni.get()
        email = self.entry_email.get()
        contraseña = self.entry_contraseña.get()

        if not (nombre and apellido and dni and email and contraseña):
            messagebox.showwarning("Atención", "Todos los campos son obligatorios")
            return

        

        conn = obtener_conexion()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO usuarios (nombre, apellido, dni, email, contraseña)
                VALUES (?, ?, ?, ?, ?)
            """, (nombre, apellido, dni, email, contraseña))
            conn.commit()
            messagebox.showinfo("Éxito", "Usuario creado correctamente")
            self.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "El email ya está registrado")
        finally:
            conn.close()

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_dni.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_contraseña.delete(0, tk.END)
