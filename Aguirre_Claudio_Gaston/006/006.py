#Crear una función que reciba una lista de números y elimine los valores que se encuentran duplicados de la lista. Retornar la lista, y una tupla con los valores que han sido eliminados.
def borra_duplicados (lista):
	lista_num = []
	eliminados = []
	for num in lista:
		if lista.count(num) < 2:
			lista_num.append(num)
		else:
			eliminados.append(num)
	eliminados=tuple(eliminados) 	
	return lista_num, eliminados

numeros=[2, 5, 6, 5, 6, 8, 9, 6, 4, 78, 6, 51, 7, 7]
print(borra_duplicados(numeros))
