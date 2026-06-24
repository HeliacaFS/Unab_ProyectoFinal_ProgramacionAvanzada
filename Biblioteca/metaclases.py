# metaclases.py
class InfoMeta(type):
    def __init__(cls, name, bases, dct):
        if "mostrar_info" not in dct:
            raise TypeError(f"La clase {name} debe implementar mostrar_info()")
        super().__init__(name, bases, dct)
