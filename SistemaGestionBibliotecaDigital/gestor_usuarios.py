from decoradores import registrar_accion


class GestorUsuarios:

    def __init__(self):

        self.usuarios = []

    @registrar_accion
    def agregar_usuario(self, usuario):

        self.usuarios.append(usuario)

    @registrar_accion
    def eliminar_usuario(self, usuario):

        self.usuarios.remove(usuario)

    def modificar_usuario(self):

        pass

    def buscar_usuario(self, dni):

        for usuario in self.usuarios:

            if usuario.dni == dni:

                return usuario

        return None

    def mostrar_usuario(self):

        for usuario in self.usuarios:

            usuario.mostrar_info()