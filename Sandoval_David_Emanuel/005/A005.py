# 005-
#     Función que reciba como parametros dos números (a y b), y
# devuelva una tupla con todos los números primos que se encuentra entre
# a y b (incluyendo a y b si son primos).
#     Por defecto a=0, y b=100


def primos_en_rango(a=0, b=100):
    primos = [2]  # lista de números primos
    # recorro todos los números hasta b
    for num in range(2, b + 1):
        for primo in primos:
            # divido cada número por cada número primo
            if num % primo == 0:
                # si la división da cero, no es primo
                # de modo que corto el loop, 
                # no necesito seguir dividiendo
                break
        else:
            # Si lo anterios no sucede, el número es primo
            # lo agrego a la lista de primos.
            # (Este primo también va a ser utilizado para 
            # chequear los siguientes números)
            primos.append(num)

    # Solo incluyo los primos dentro del rango indicado
    primos_in_range = tuple([p for p in primos if (p >= a and p <= b)])
    return primos_in_range # y lo devuelvo


print(primos_en_rango(5, 9743))
