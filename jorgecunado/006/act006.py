def elimina_duplicados(plista):

	lista_nueva = []
	repetidos = []
	
	for numero in plista:
		
		if numero in lista_nueva:
			repetidos.append(numero)
		else :
			lista_nueva.append(numero)

	return lista_nueva, tuple(repetidos)		
