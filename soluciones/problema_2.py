
"""Programa para aproximar n! usando la fórmula de Stirling."""

import math


def leer_n():
    while True:
        try:
            n = float(input("Ingrese el valor de n: "))
            if n < 0:
                print("El valor de n debe ser mayor o igual a 0.")
                continue
            return n
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")


def calcular_factorial_aproximado(n):
    if n == 0:
        return 1.0
    if n < 0:
        raise ValueError("n debe ser mayor o igual a 0")

    return (math.sqrt(2 * math.pi * n) * (math.e ** (-n)) * (n ** (n + 0.5)))


def main():
    n = leer_n()
    resultado = calcular_factorial_aproximado(n)
    print(f"El valor aproximado de n! para n = {n} es: {resultado}")


if __name__ == "__main__":
    main()
