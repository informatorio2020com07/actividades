#Crear una función que reciba una lista de números y elimine
#los valores que se encuentran duplicados de la lista.
#Retornar la lista, y una tupla con los valores que han sido
#eliminados.
#def duplicados(lista):
def eliminar_repetidos(lista):
	nueva=[]
	repetido=[]
	for elemento in lista:
		if not elemento in nueva:
			nueva.append(elemento)
		else:
			repetido.append(elemento)
	tupla=tuple(repetido)

	return nueva, tupla


Lista = [1,1,1,3,4,4,5,5,5,5,5,5,5,7]
print(Lista)
print(eliminar_repetidos(Lista))

	