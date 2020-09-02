"""005-
    Función que reciba como parametros dos números (a y b), y
devuelva una tupla con todos los números primos que se encuentra entre
a y b (incluyendo a y b si son primos).
    Por defecto a=0, y b=100"""

def verificador_de_n_primos(num):
	if num < 2:
		return False
	for x in range(2, num):
		if num % x == 0:
			return False
	return True	

def rango_primos(a=0, b=100):
	lista=[]
	for a in range(a, b + 1):
		if verificador_de_n_primos(a):
			lista.append(a)
	tupla=tuple(lista)
	return tupla

primos=rango_primos(10, 50)
print(primos)
