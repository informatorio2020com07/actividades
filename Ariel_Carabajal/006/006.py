#!/usr/bin/python3
'''006-
    Crear una función que reciba una lista de números y elimine
    los valores que se encuentran duplicados de la lista.
    Retornar la lista, y una tupla con los valores que han sido
    eliminados.
'''

def borrarDuplicados(_lista):
	listaNueva = []
	eliminado = []
	
	for i in _lista:
		if not i in listaNueva:
			listaNueva.append(i)
		else:
			eliminado.append(i)
	
	tupla = tuple(eliminado)

	return listaNueva, tupla


lista = [1,1,2,6,8,6,5,8,11,4,5,55,64,11]

print('Lista y Tupla con números eliminados:\n', borrarDuplicados(lista))