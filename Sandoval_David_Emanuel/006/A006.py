# 006-
#     Crear una función que reciba una lista de números y elimine
#     los valores que se encuentran duplicados de la lista.
#     Retornar la lista, y una tupla con los valores que han sido
#     eliminados.


def no_duplicados(numeros: list):
    duplicados = []
    for n in numeros:
        if numeros.count(n) > 1:
            numeros.remove(n)
            duplicados.append(n)
    return numeros, tuple(duplicados)


if __name__ == "__main__":
    original = [0, 0, 1, 2, 2, 3, 4, 4, 7, 2]
    resultado = no_duplicados(numeros=original)
    print(resultado)
    print(original is resultado[0])
