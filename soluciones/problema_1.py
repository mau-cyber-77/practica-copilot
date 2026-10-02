
"""Programa para calcular x = sqrt(b - a^2) / c."""

import math


def leer_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")


def calcular_x(a, b, c):
    if c == 0:
        raise ValueError("El valor de c no puede ser cero.")

    return math.sqrt(b - a ** 2) / c


def main():
    a = leer_numero("Ingrese el valor de a: ")
    b = leer_numero("Ingrese el valor de b: ")
    c = leer_numero("Ingrese el valor de c: ")

    try:
        x = calcular_x(a, b, c)
        print(f"El valor de x es: {x}")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
