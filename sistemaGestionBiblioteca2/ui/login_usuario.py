import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from ui.usuario_registrado import UsuarioRegistrado
from ui.registro_usuario import RegistroUsuario
from db.conexion import obtener_conexion

class LoginUsuario(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Login Usuario")
        self.geometry("400x300")
        self.resizable(False, False)

        # --- Campos de login ---
        ttk.Label(self, text="Email").pack(pady=5)
        self.var_usuario = tk.StringVar()
        self.entry_usuario = ttk.Entry(self, textvariable=self.var_usuario, width=30)
        self.entry_usuario.pack()

        ttk.Label(self, text="Contraseña").pack(pady=5)
        self.var_contraseña = tk.StringVar()
        self.entry_contraseña = ttk.Entry(self, textvariable=self.var_contraseña, show="*", width=30)
        self.entry_contraseña.pack()

        # --- Botones ---
        btn_ingresar = tk.Button(self, text="Ingresar", bg="lightblue", width=15, command=self.ingresar)
        btn_ingresar.pack(pady=10)

        btn_nuevo = tk.Button(self, text="Nuevo Usuario", bg="lightgreen", width=15, command=self.abrir_registro_usuario)
        btn_nuevo.pack(pady=5)

        btn_salir = tk.Button(self, text="Salir", bg="red", fg="white", width=10, command=self.destroy)
        btn_salir.pack(pady=15)

    # --- Métodos ---
    def ingresar(self):
        email = self.var_usuario.get()
        contraseña = self.var_contraseña.get()

        if not email or not contraseña:
            messagebox.showwarning("Atención", "Complete todos los campos")
            return

       

        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email=? AND contraseña=?", (email, contraseña))
        fila = cursor.fetchone()
        conn.close()

        if fila:
            usuario_id = fila[0]
            messagebox.showinfo("Bienvenido", f"Acceso correcto: {email}")
            UsuarioRegistrado(self, usuario_id)  # abrir interfaz de usuario registrado
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def abrir_registro_usuario(self):
        RegistroUsuario(self)
