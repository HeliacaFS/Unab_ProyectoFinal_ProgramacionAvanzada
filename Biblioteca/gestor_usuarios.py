# gestor_usuarios.py
from decoradores import registrar_accion

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    @registrar_accion
    def alta(self, usuario):
        self.usuarios.append(usuario)

    def listar(self):
        for u in self.usuarios:
            u.mostrar_info()
