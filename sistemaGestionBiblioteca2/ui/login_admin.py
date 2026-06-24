import tkinter as tk
from tkinter import ttk, messagebox
from utils.ui_helpers import centrar_ventana


class LoginAdmin(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Login de Administrador")
        centrar_ventana(self, 400, 250)

        self.resizable(False, False)

        lbl_titulo = ttk.Label(self, text="Acceso de Administrador", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=15)

        # Campo Usuario
        frame_usuario = tk.Frame(self)
        frame_usuario.pack(pady=5)
        ttk.Label(frame_usuario, text="Usuario:").grid(row=0, column=0, padx=5)
        self.entry_usuario = ttk.Entry(frame_usuario, width=25)
        self.entry_usuario.grid(row=0, column=1)

        # Campo Contraseña
        frame_contra = tk.Frame(self)
        frame_contra.pack(pady=5)
        ttk.Label(frame_contra, text="Contraseña:").grid(row=0, column=0, padx=5)
        self.entry_contra = ttk.Entry(frame_contra, width=25, show="*")
        self.entry_contra.grid(row=0, column=1)

        # Botón Ingresar
        btn_ingresar = tk.Button(
            self,
            text="Ingresar",
            bg="blue",
            fg="white",
            width=12,
            command=self.ingresar
        )
        btn_ingresar.pack(pady=20)

    def ingresar(self):
        usuario = self.entry_usuario.get()
        contra = self.entry_contra.get()
        # Aquí podrías validar contra la base de datos
        messagebox.showinfo("Administrador", f"Intentando ingresar como administrador: {usuario}")
