from tkinter import *
import tkinter as tk
from tkinter import ttk 
from tkinter.messagebox import *
import DB as DB
from DB import *
from usuario import Usuario
import sqlite3

class Main:
    def __init__(self, root, app):
        self.root = root
        self.app = app 

        self.root.title("Sistema de Biblioteca")
        self.root.geometry("1150x600")
        self.root.resizable(False, False)
        
        self.bg_color = "#ffffff"
        self.root.configure(bg=self.bg_color)

        self.var_busqueda = StringVar()
        self.var_titulo = StringVar()
        self.var_autor = StringVar()
        self.var_isbn = StringVar()
        self.var_anio = StringVar()
        self.var_paginas = StringVar()
        self.var_genero = StringVar() 

        self.crear_menu()
        self.crear_widgets()
        self.mostrar_libros()   
        self.mostrar_prestamos()
    def mostrar_info(self):
        showinfo("Biblioteca", "Sistema de gestión de biblioteca")

    def mostrar_autor(self):
        showinfo("Autor", "Brian Fernandez, Marcos Chaves, Santiago")

    def crear_menu(self):
        barramenu = Menu(self.root)
        menu_archivo = Menu(barramenu, tearoff=0)
        menu_archivo.add_command(label="Salir", command=self.root.destroy) 
        barramenu.add_cascade(label="Archivo", menu=menu_archivo)

        menu_info = Menu(barramenu, tearoff=0)
        menu_info.add_command(label="Acerca del programa", command=self.mostrar_info)
        menu_info.add_command(label="Acerca del autor", command=self.mostrar_autor)
        barramenu.add_cascade(label="Información", menu=menu_info)

        self.root.config(menu=barramenu)

    def crear_widgets(self):
        main_frame = Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill="both", expand=True, padx=50, pady=(15, 15))

        main_frame.grid_rowconfigure(2, weight=1)      
        main_frame.grid_columnconfigure(0, weight=1)   
        main_frame.grid_columnconfigure(1, weight=0)   

        top_frame = Frame(main_frame, bg=self.bg_color)
        top_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 20))  # columnspan 2
        top_frame.grid_columnconfigure(0, weight=1)

        Label(top_frame, text="Biblioteca",
            font=("Arial", 22, "bold"), bg=self.bg_color).grid(row=0, column=0, sticky="w")

        usuario_texto = f"Usuario: {self.app.usuario_nombre}"
        Label(top_frame, text=usuario_texto, font=("Arial", 11, "bold"),
            bg=self.bg_color, fg="#333333").grid(row=0, column=1, sticky="e", padx=(20,0))

        search_frame = Frame(main_frame, bg=self.bg_color)
        search_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 20))  # columnspan 2
        search_frame.grid_columnconfigure(0, weight=1)
        search_frame.grid_columnconfigure(1, weight=1)

        lbl_titulo = Label(search_frame, text="Buscar libro por título", font=("Arial", 14, "bold"), bg=self.bg_color)
        lbl_titulo.grid(row=0, column=0, sticky="w", padx=(0, 10))
        entry_titulo_frame = Frame(search_frame, bg=self.bg_color, highlightbackground="#000000", highlightthickness=1)
        entry_titulo_frame.grid(row=0, column=1, sticky="ew", padx=(0, 20))
        Entry(entry_titulo_frame, textvariable=self.var_busqueda, bd=0, font=("Arial", 11)).pack(side="left", padx=5, pady=5, fill="x", expand=True)

        lbl_genero = Label(search_frame, text="Buscar libro por Género", font=("Arial", 14, "bold"), bg=self.bg_color)
        lbl_genero.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(10,0))
        entry_genero_frame = Frame(search_frame, bg=self.bg_color, highlightbackground="#000000", highlightthickness=1)
        entry_genero_frame.grid(row=1, column=1, sticky="ew", padx=(0, 20), pady=(10,0))
        Entry(entry_genero_frame, textvariable=self.var_genero, bd=0, font=("Arial", 11)).pack(side="left", padx=5, pady=5, fill="x", expand=True)

        table_frame = Frame(main_frame, bg=self.bg_color, bd=2, relief="groove")
        table_frame.grid(row=2, column=0, sticky="nsew", pady=(0, 10))  

        Label(
            table_frame,
            text="Libros disponibles",
            bg=self.bg_color,
            font=("Arial", 14, "bold")
        ).pack(anchor="w", padx=10, pady=(10, 5))

        tree_container = Frame(table_frame, bg=self.bg_color)
        tree_container.pack(padx=10, pady=(0, 10), fill="both", expand=True)

        self.tabla_libros = ttk.Treeview(
            tree_container,
            columns=("titulo", "autor", "isbn", "anio", "paginas", "genero"),
            show="headings",
            height=12
        )

        self.tabla_libros.heading("titulo", text="Título")
        self.tabla_libros.heading("autor", text="Autor")
        self.tabla_libros.heading("isbn", text="ISBN")
        self.tabla_libros.heading("anio", text="Año")
        self.tabla_libros.heading("paginas", text="Páginas")
        self.tabla_libros.heading("genero", text="Género")

        self.tabla_libros.column("titulo", width=150)
        self.tabla_libros.column("autor", width=120)
        self.tabla_libros.column("isbn", width=100)
        self.tabla_libros.column("anio", width=60, anchor="center")
        self.tabla_libros.column("paginas", width=70, anchor="center")
        self.tabla_libros.column("genero", width=100)

        scrollbar_y = Scrollbar(tree_container, orient="vertical", command=self.tabla_libros.yview)
        self.tabla_libros.configure(yscrollcommand=scrollbar_y.set)

        self.tabla_libros.pack(side="left", fill="both", expand=True)
        scrollbar_y.pack(side="right", fill="y")

        prestamos_frame = Frame(main_frame, bg=self.bg_color, bd=2, relief="groove")
        prestamos_frame.grid(row=2, column=1, sticky="nsew", padx=(10, 0), pady=(0, 10))
        prestamos_frame.grid_propagate(False) 
        prestamos_frame.config(width=300)      

        Label(
            prestamos_frame,
            text="Préstamos activos",
            bg=self.bg_color,
            font=("Arial", 14, "bold")
        ).pack(anchor="w", padx=10, pady=(10, 5))

        prestamo_tree_container = Frame(prestamos_frame, bg=self.bg_color)
        prestamo_tree_container.pack(padx=10, pady=(0, 10), fill="both", expand=True)

        self.tabla_prestamos = ttk.Treeview(
            prestamo_tree_container,
            columns=("libro", "fecha"),
            show="headings",
            height=6  
        )

        self.tabla_prestamos.heading("libro", text="Libro")
        self.tabla_prestamos.heading("fecha", text="Fecha préstamo")

        self.tabla_prestamos.column("libro", width=120)
        self.tabla_prestamos.column("fecha", width=80)

        scrollbar_prestamos = Scrollbar(prestamo_tree_container, orient="vertical", command=self.tabla_prestamos.yview)
        self.tabla_prestamos.configure(yscrollcommand=scrollbar_prestamos.set)

        self.tabla_prestamos.pack(side="left", fill="both", expand=True)
        scrollbar_prestamos.pack(side="right", fill="y")

        bottom_frame = Frame(main_frame, bg=self.bg_color)
        bottom_frame.grid(row=3, column=0, columnspan=2, sticky="e", pady=(0, 5))  
        Button(bottom_frame, text="Pedir prestado", font=("Arial", 12),
            bg="#e0e0e0", relief="raised", width=15, command=self.solicitar_prestamo).pack(side="right")
        
    def mostrar_libros(self):
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()

        for item in self.tabla_libros.get_children():
            self.tabla_libros.delete(item)

        cursor.execute("SELECT id_libro, titulo, autor, isbn, anio, paginas, genero FROM tabla_libros")
        filas = cursor.fetchall()

        for fila in filas:
            id_libro = fila[0]        
            resto_valores = fila[1:]   
            
            self.tabla_libros.insert("", "end", iid=id_libro, values=resto_valores)

        conn.close()

    def mostrar_prestamos(self):
        conn = sqlite3.connect("biblioteca.db")
        cursor = conn.cursor()

        for item in self.tabla_prestamos.get_children():
            self.tabla_prestamos.delete(item)

        try:
            id_usuario_actual = self.app.usuario_actual.id_usuario
        except AttributeError:
            id_usuario_actual = self.app.usuario_actual 

        query = """
            SELECT tabla_libros.titulo, tabla_prestamos.fecha_prestamo 
            FROM tabla_prestamos
            INNER JOIN tabla_libros ON tabla_prestamos.id_libro = tabla_libros.Id_Libro
            WHERE tabla_prestamos.id_usuario = ?
        """
        
        cursor.execute(query, (id_usuario_actual,))
        filas = cursor.fetchall()

        for fila in filas:
            self.tabla_prestamos.insert("", "end", values=fila)

        conn.close()
    
    def solicitar_prestamo(self):
        seleccion = self.tabla_libros.selection()
        
        if not seleccion:
            showwarning("Atención", "Por favor, seleccione un libro de la lista.")
            return
            
        id_libro = seleccion[0]
        id_usuario = self.app.usuario_actual

        gestor = Gestor_Prestamo()
        
        exito = gestor.agregar_prestamo(usuarioID=id_usuario, LibroID=id_libro)
        
        if exito:
            showinfo("Éxito", "El préstamo ha sido registrado correctamente.")
            self.mostrar_libros()
            self.mostrar_prestamos()
        else:
            showerror("Error", "No se pudo procesar el préstamo. Verifique el stock disponible.")
    



class Login:
    def __init__(self, root, app):
        self.root = root
        self.app = app  
        self._configurar_ventana()
        self._inicializar_variables()        
        self._crear_interfaz()

    def _configurar_ventana(self):
        self.root.title("Login")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.bg_color = "#f0f0f0"
        self.root.configure(bg=self.bg_color)
        
        self.font_title = ("Arial", 18, "bold")
        self.font_label = ("Arial", 10, "bold")
        self.font_entry = ("Arial", 10)
        self.font_subtitle = ("Arial", 9, "underline")

    def _inicializar_variables(self):
        self.var_usuario = StringVar(value="")
        self.var_contraseña = StringVar(value="")

    def _crear_interfaz(self):
        Label(self.root, text="Bienvenido a Biblioteca", font=self.font_title, bg=self.bg_color, fg="#333333").grid(row=0, column=0, columnspan=2, pady=(30, 5))
        Label(self.root, text="¿Nuevo usuario? Regístrate para acceder", font=self.font_subtitle, bg=self.bg_color, fg="#333333").grid(row=1, column=0, columnspan=2, pady=(0, 20))

        self._crear_campo(label_text="USUARIO", variable=self.var_usuario, fila=2)
        self._crear_campo(label_text="Contraseña", variable=self.var_contraseña, fila=3, es_password=True)
        self._crear_botones()

    def _crear_campo(self, label_text, variable, fila, es_password=False):
        Label(self.root, text=label_text, font=self.font_label, bg=self.bg_color, fg="#555555").grid(row=fila, column=0, sticky="e", padx=(30, 10), pady=5)        
        show_char = "*" if es_password else ""
        Entry(self.root, textvariable=variable, font=self.font_entry, show=show_char, width=35, relief="solid", bd=1).grid(row=fila, column=1, sticky="w", padx=(0, 30), pady=5)

    def _crear_botones(self):
        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=30)
        Button(btn_frame, text="Iniciar Sesion", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", padx=20, pady=5, relief="flat", cursor="hand2", command=self.iniciar_sesion).pack(side="left", padx=10)
        Button(btn_frame, text="Crear Cuenta", font=("Arial", 10, "bold"), bg="#008CBA", fg="white", padx=20, pady=5, relief="flat", cursor="hand2", command=self.cambiar_a_registro).pack(side="left", padx=10)
    
    def cambiar_a_registro(self):
        self.app.mostrar_registro()
    def iniciar_sesion(self):
        usuario_input = self.var_usuario.get()
        contraseña_input = self.var_contraseña.get()

        if not usuario_input or not contraseña_input:
            showinfo("Error", "Complete todos los campos")
            return

        datos_usuario = self.app.db.verificar_usuario(usuario_input, contraseña_input)

        if datos_usuario is not None:
            id_usuario, usuario,*_ = datos_usuario
            
            self.app.usuario_actual = id_usuario
            self.app.usuario_nombre = usuario
            
            showinfo("Inicio de sesión exitoso", f"Bienvenido {usuario}")
            self.app.mostrar_main()
        else:
            showinfo("Error", "Usuario o contraseña incorrectos")
    

class Registro:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self._configurar_ventana()
        self._inicializar_variables()        
        self._crear_interfaz()

    def _configurar_ventana(self):
        self.root.title("Registro")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.bg_color = "#f0f0f0"
        self.root.configure(bg=self.bg_color)
        
        self.font_title = ("Arial", 18, "bold")
        self.font_label = ("Arial", 10, "bold")
        self.font_entry = ("Arial", 10)
        self.font_subtitle = ("Arial", 9, "underline")

    def _inicializar_variables(self):
        self.var_usuario = StringVar()
        self.var_nombre = StringVar()
        self.var_apellido = StringVar()
        self.var_email = StringVar()
        self.var_contraseña = StringVar()
        self.var_dni = StringVar()

    def _crear_interfaz(self):
        Label(self.root, text="Bienvenido a la Biblioteca", font=self.font_title, bg=self.bg_color, fg="#333333").grid(row=0, column=0, columnspan=2, pady=(30, 5))
        Label(self.root, text="¿Nuevo usuario? Regístrate para acceder", font=self.font_subtitle, bg=self.bg_color, fg="#333333").grid(row=1, column=0, columnspan=2, pady=(0, 20))

        self._crear_campo(label_text="USUARIO", variable=self.var_usuario, fila=2)
        self._crear_campo(label_text="NOMBRE", variable=self.var_nombre, fila=3)
        self._crear_campo(label_text="APELLIDO", variable=self.var_apellido, fila=4)
        self._crear_campo(label_text="EMAIL", variable=self.var_email, fila=5)
        self._crear_campo(label_text="Contraseña", variable=self.var_contraseña, fila=6, es_password=True)
        self._crear_campo(label_text="DNI", variable=self.var_dni, fila=7)
        self._crear_botones()

    def _crear_campo(self, label_text, variable, fila, es_password=False):
        Label(self.root, text=label_text, font=self.font_label, bg=self.bg_color, fg="#555555").grid(row=fila, column=0, sticky="e", padx=(30, 10), pady=5)        
        show_char = "*" if es_password else ""
        Entry(self.root, textvariable=variable, font=self.font_entry, show=show_char, width=35, relief="solid", bd=1).grid(row=fila, column=1, sticky="w", padx=(0, 30), pady=5)

    def _crear_botones(self):
        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.grid(row=8, column=0, columnspan=2, pady=30)
        Button(btn_frame, text="Atras", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", padx=20, pady=5, relief="flat", cursor="hand2", command=self.cambiar_a_login).pack(side="left", padx=10)
        Button(btn_frame, text="Registrarse", font=("Arial", 10, "bold"), bg="#008CBA", fg="white", padx=20, pady=5, relief="flat", cursor="hand2", command=self.registrar_usuario).pack(side="left", padx=10)

    def registrar_usuario(self):
        usuario = self.var_usuario.get()
        nombre = self.var_nombre.get()
        apellido = self.var_apellido.get()
        email = self.var_email.get()
        contraseña = self.var_contraseña.get()
        dni = self.var_dni.get()

        if not usuario or not nombre or not email or not contraseña or not dni:
            showinfo("Error", "Por favor, complete todos los campos.")
            return

        nuevo_usuario = Usuario(usuario, nombre, apellido, dni, email, contraseña, "Cliente")
        

        registrado = self.app.db.agregar_usuario(nuevo_usuario)

        if registrado:
            showinfo("Registro exitoso", "Usuario registrado correctamente.")
            self.cambiar_a_login()
        else:
            showerror("Error de registro", "El usuario, DNI o correo electrónico ya se encuentran registrados.")
            
            ventana_ayuda = Toplevel(self.root) 
            ventana_ayuda.title("Ayuda con la cuenta")
            ventana_ayuda.geometry("300x120")
            ventana_ayuda.resizable(False, False)
            
            ventana_ayuda.transient(self.root)
            ventana_ayuda.grab_set()

            Label(ventana_ayuda, text="¿Tienes problemas para registrarte?", font=("Arial", 10, "bold")).pack(pady=10)

            def recuperar_con():
                ventana_ayuda.destroy() 
                showinfo("Recuperación", "Se ha enviado un correo de recuperación al mail ingresado.")

            btn_olvido = Button(
                ventana_ayuda, 
                text="¿Haz olvidado tu contraseña?", 
                command=recuperar_con,
                fg="blue", 
                cursor="hand2"
            )
            btn_olvido.pack(pady=5)





    def cambiar_a_login(self):
        self.app.mostrar_login()