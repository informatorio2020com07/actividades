"""
	Crear una función que reciba una lista de números y elimine
	los valores que se encuentran duplicados de la lista.
	Retornar la lista, y una tupla con los valores que han sido
	eliminados.
"""

def eliminaDuplicados(listaNumeros):

	duplicados = []

	for i in listaNumeros:
		if i in listaNumeros[listaNumeros.index(i)+1:]:

			duplicados.append(i)

	listaNueva = set(listaNumeros)

	return f"La lista sin duplicados es: {list(listaNueva)} y la tupla de duplicados: {tuple(duplicados)}"
	
"""
listaPrueba = [1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 10, 11, 4, 3, 2, 1]
print(eliminaDuplicados(listaPrueba))
La lista sin duplicados es: [1, 2, 3, 4, 5, 10, 11] y la tupla de duplicados: (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 4, 3, 2, 1)
"""