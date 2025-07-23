# Programa para determinar si un numero es primo

import math


def es_primo(n):
    """Devuelve True si n es primo, False en caso contrario."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limite = int(math.isqrt(n))
    for i in range(3, limite + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    valor = input("Introduce un numero: ")
    try:
        numero = int(valor)
    except ValueError:
        print("Debes introducir un numero entero")
        return

    if es_primo(numero):
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")


if __name__ == "__main__":
    main()
