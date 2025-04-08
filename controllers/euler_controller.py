import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt
import os

def f(x, y):
    return x + y

def calcular_y_real(x):
    y = math.exp(-0.2 + 0.2 * math.pow(x, 2))
    return y

def solucion_exacta(x, x0, y0):
    # Calculamos C
    C = (y0 + x0 + 1) * math.exp(-x0)
    return C * math.exp(x) - x - 1

def euler_mejorado(x0, y0, h, n):
    x_vals = [x0]
    y_vals = [y0]
    y_exact_vals = [calcular_y_real(x0)]
    errores = [abs(y_vals[0] - y_exact_vals[0])]

    x = x0
    y = y0

    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y = y + (h / 2) * (k1 + k2)
        x = x + h

        y_real = calcular_y_real(x)
        error_abs = abs(y - y_real)

        x_vals.append(x)
        y_vals.append(y)
        y_exact_vals.append(y_real)
        errores.append(error_abs)

    return x_vals, y_vals, y_exact_vals, errores

def datos_grafica(x_vals, y_aprox, y_exact):
    return {
        "x": x_vals,
        "y_aprox": y_aprox,
        "y_exact": y_exact
    }



def metodo_euler_mejorado(ecuacion_str, x0, y0, h, n=10):
    x, y = sp.symbols('x y')
    f = sp.sympify(ecuacion_str)
    f_lambd = sp.lambdify((x, y), f)

    resultados = []
    xn, yn = x0, y0

    for i in range(n + 1):
        y_real = None
        error = None

        try:
            k1 = f_lambd(xn, yn)
            k2 = f_lambd(xn + h, yn + h * k1)
            yn_siguiente = yn + (h / 2) * (k1 + k2)
        except Exception as e:
            yn_siguiente = "Error"

        # Calcular yReal
        if isinstance(yn_siguiente, float):
            y_real = calcular_y_real(xn)
            error = abs(yn - y_real)
        else:
            y_real = "Error"
            error = "Error"
        
        #if isinstance(yn_siguiente, float):
        #    y_real = "N/A"
        #    error = "N/A"

        resultados.append({
            "n": i,
            "xn": round(xn, 4),
            "yn": round(yn, 4) if isinstance(yn, float) else yn,
            "yreal": y_real,
            "error": error
        })

        yn = yn_siguiente
        xn += h

    return resultados
