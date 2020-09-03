"""006-
    Crear una función que reciba una lista de números y elimine
    los valores que se encuentran duplicados de la lista.
    Retornar la lista, y una tupla con los valores que han sido
    eliminados."""
  
def borrar_repetidos(lista_numeros):
	lista_nueva=[]
	borrados=[]	
	for x in lista_numeros:		
		if x in lista_nueva:
			borrados.append(x)
		else :
			lista_nueva.append(x)
	borrados.sort()
	lista_nueva.sort()
	tupla=tuple(borrados)	
	return lista_nueva, tupla


lista1=[1,3,4,2,5,2,67,87,90,3,1,67,90,10,9,12,4,5,15]
repetidos=borrar_repetidos(lista1)
print(repetidos)