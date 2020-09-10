'''
Función que reciba como parametros dos números (a y b), y
devuelva una tupla con todos los números primos que se encuentra entre
a y b (incluyendo a y b si son primos).
    Por defecto a=0, y b=100
'''
from os import system
import math


def primo(numero):
    if (numero <= 1):
        return False

    for i in range(2, math.ceil(math.sqrt(numero)) + 1):
        if (numero % i == 0 and i != numero):
            return False
    return True


def tupla_primos(val1, val2):
    list_primos = []
    for num in range(val1, val2 + 1):
        res = primo(num)
        if res:
            list_primos.append(num);
    return tuple(list_primos)


while True:
    try:
        system("cls")
        print("Para salir ingrese una letra")
        numero1 = int(input("Ingrese valor inferior del rango: "))
        numero2 = int(input("Ingrese valor Superior del rango: "))
        tup_primos = tupla_primos(numero1, numero2)
        print("\nLos numeros Primos Entre los Valores Ingresados son: ")
        print(tup_primos)
        input()
    except:
        break
