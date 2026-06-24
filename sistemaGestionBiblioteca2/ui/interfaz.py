import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import os
from ui.login_usuario import LoginUsuario
from ui.login_admin import LoginAdmin
from ui.registro_usuario import RegistroUsuario
from utils.ui_helpers import centrar_ventana





class Main:
    def __init__(self, root):
        self.root = root
        centrar_ventana(self.root, 500, 300)

        self.root.resizable(False, False) 


        # Crear menú principal
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Menú Archivo
        #archivo_menu = tk.Menu(menubar, tearoff=0)
        #archivo_menu.add_command(label="Salir", command=self.root.quit)
        #menubar.add_cascade(label="Archivo", menu=archivo_menu)

        # Menú Información
        #info_menu = tk.Menu(menubar, tearoff=0)
        #info_menu.add_command(label="Ingresar", command=self.mostrar_info)
        #menubar.add_cascade(label="Administrador", menu=info_menu)

        # --- Contenido principal ---
        ruta_icono_principal = os.path.join(
            os.path.dirname(__file__), "..", "assets", "iconos", "librodigital.png"
        )
        self.icono = tk.PhotoImage(file=ruta_icono_principal)

        label = ttk.Label(
            self.root,
            text="Biblioteca Digital",
            font=("Arial", 16),
            image=self.icono,
            compound="left"
        )
        label.pack(pady=20)

        # --- Íconos de login ---
        self._crear_iconos_login()

        # --- Footer ---
        self._crear_footer()

    def mostrar_info(self):
        messagebox.showinfo("Administrador", "Acceso al panel de administración.\nFuncionalidad en desarrollo.")

    def _crear_iconos_login(self):
        frame_login = tk.Frame(self.root)
        frame_login.pack(pady=30)

        # Ícono Usuario
        ruta_usuario = os.path.join(
            os.path.dirname(__file__), "..", "assets", "iconos", "usuario.png"
        )
        self.icono_usuario = tk.PhotoImage(file=ruta_usuario)

        btn_usuario = tk.Button(
            frame_login,
            image=self.icono_usuario,
            cursor="hand2",
            borderwidth=2,
            relief="flat",
            command=self.abrir_login_usuario
        )
        btn_usuario.grid(row=0, column=0, padx=40)
        lbl_usuario = tk.Label(frame_login, text="Usuario", font=("Arial", 12))
        lbl_usuario.grid(row=1, column=0)

        # Hover efecto Usuario
        btn_usuario.bind("<Enter>", lambda e: btn_usuario.config(relief="solid"))
        btn_usuario.bind("<Leave>", lambda e: btn_usuario.config(relief="flat"))

        # Ícono Administrador
        ruta_admin = os.path.join(
            os.path.dirname(__file__), "..", "assets", "iconos", "admin.png"
        )
        self.icono_admin = tk.PhotoImage(file=ruta_admin)

        btn_admin = tk.Button(
            frame_login,
            image=self.icono_admin,
            cursor="hand2",
            borderwidth=2,
            relief="flat",
            command=self.abrir_login_admin

        )
        btn_admin.grid(row=0, column=1, padx=40)
        lbl_admin = tk.Label(frame_login, text="Administrador", font=("Arial", 12))
        lbl_admin.grid(row=1, column=1)

        # Hover efecto Administrador
        btn_admin.bind("<Enter>", lambda e: btn_admin.config(relief="solid"))
        btn_admin.bind("<Leave>", lambda e: btn_admin.config(relief="flat"))

    def _crear_footer(self):
        footer = tk.Frame(self.root, bg="#2C3E50", height=40)
        footer.pack(side="bottom", fill="x")

        footer_label = tk.Label(
            footer,
            text="SGB Digital - Creado por Nirmata Software",
            fg="white",
            bg="#2C3E50",
            font=("Arial", 10, "bold")
        )
        footer_label.pack(side="left", padx=10)

        ruta_icono_footer = os.path.join(
            os.path.dirname(__file__), "..", "assets", "iconos", "creador.png"
        )
        self.footer_icono = tk.PhotoImage(file=ruta_icono_footer)

        icono_btn = tk.Button(
            footer,
            image=self.footer_icono,
            bg="#2C3E50",
            borderwidth=0,
            cursor="hand2",
            command=lambda: webbrowser.open("https://nirmatasoftware.com")
        )
        icono_btn.pack(side="right", padx=10)

    def abrir_login_usuario(self):
        from ui.login_usuario import LoginUsuario
        LoginUsuario(self.root)

    def abrir_login_admin(self):
         LoginAdmin(self.root)


