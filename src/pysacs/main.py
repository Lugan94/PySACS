from time import perf_counter
from functools import wraps

def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = perf_counter()
        resultado = func(*args, **kwargs)
        fin = perf_counter()
        print(f"Función '{func.__name__}' tardó: {fin - inicio:.6f} s")
        return resultado
    return wrapper

import numpy as np

@medir_tiempo
def crear_lista_python(n):
    return [i for i in range(n)]

@medir_tiempo
def crear_array_numpy(n):
    return np.arange(n)

# Prueba con 10 millones de elementos
n = 1000
crear_lista_python(n)
crear_array_numpy(n)