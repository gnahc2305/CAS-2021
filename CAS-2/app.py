# May 31, 2021
import random


def dado1():
    numero = random.uniform(1, 6)
    global a
    a = round(numero)
    print(f"Primer Dado: {a}")


dado1()


def dado2():
    numero = random.uniform(1, 6)
    global b
    b = round(numero)
    print(f"Segundo Dado: {b}")


dado2()


def suma_de_dados():
    operacion = a + b
    print(f"Suma de los Dados: {operacion}")


suma_de_dados()