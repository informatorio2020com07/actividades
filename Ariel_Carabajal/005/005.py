#!/usr/bin/python3
'''005-
    Función que reciba como parametros dos números (a y b), y
    devuelva una tupla con todos los números primos que se encuentra entre
    a y b (incluyendo a y b si son primos).
    Por defecto a=0, y b=100
'''

def primos(a = 0, b = 100):

    def esPrimo(n):
    
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    res = []
    for n in range(max(a, 2), b + 1):
        if esPrimo(n):
            res.append(n)
    return tuple(res)

print('Tupla de números primos: ', primos(20, 50))
print('Tupla de números primos por defecto: ', primos())
