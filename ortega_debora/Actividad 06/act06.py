#Crear una función que reciba una lista de números y elimine
#los valores que se encuentran duplicados de la lista.
#Retornar la lista, y una tupla con los valores que han sido
#eliminados.


#eliminar repetidos:

def eliminar_repetidos(lista):
    nueva=[]
    repetidos= []
    for elemento in lista:
        if not elemento in nueva:
            nueva.append(elemento)
        else:
            repetidos.append(elemento)
    la_tupla=tuple(repetidos)
    return nueva, la_tupla


Lista = [8, 5, 5, 3, 5, 2, 1, 6, 8, 8]
print(Lista)
print(eliminar_repetidos(Lista))

