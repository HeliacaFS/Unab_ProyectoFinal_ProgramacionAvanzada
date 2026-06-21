from tkinter import *
from Interfaz import *
import DB as DB


class App:
    def __init__(self):
        self.root = Tk()

        self.db = DB.Gestor_usuarios()

        self.usuario_actual = None

    def iniciar_aplicacion(self):
        self.mostrar_login()
        self.root.mainloop()

    def mostrar_login(self):
        self.limpiar_ventana()
        Login(self.root, self)

    def mostrar_registro(self):
        self.limpiar_ventana()
        Registro(self.root, self)

    def mostrar_main(self):
        self.limpiar_ventana()
        Main(self.root, self)

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()
   


aplicacion = App()
aplicacion.iniciar_aplicacion()
