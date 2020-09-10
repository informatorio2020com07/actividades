'''
Crear una función que reciba una lista de números y elimine
los valores que se encuentran duplicados de la lista.
Retornar la lista, y una tupla con los valores que han sido eliminados.
'''
from os import system


def duplicados(numeros):
    sin_dupli = []
    eliminados = []

    for i in numeros:
        if not i in sin_dupli:
            sin_dupli.append(i)
        elif not i in eliminados:
            eliminados.append(i)

    tupla = tuple(eliminados)

    return sin_dupli, tupla


sigue_cargando = True
list_num = []
system("cls")
while sigue_cargando:
    try:
        numero = int(input("ingrese Valor : (deje vacio para cortar la carga)\n"))
        list_num.append(numero)
        system("cls")
    except:
        sigue_cargando = False
print("Lista sin Duplicados: \n{}\nNumeros Eliminados:\n{}".format(*duplicados(list_num)))
