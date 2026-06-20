from functools import wraps


def registrar_accion(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"[LOG] Ejecutando '{func.__name__}'")

        resultado = func(*args, **kwargs)

        print(f"[LOG] '{func.__name__}' ejecutado correctamente")

        return resultado

    return wrapper