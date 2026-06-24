# decoradores.py
def registrar_accion(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Ejecutando: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
