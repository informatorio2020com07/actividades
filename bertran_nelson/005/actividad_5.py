"""
	Función que reciba como parametros dos números (a y b), y
	devuelva una tupla con todos los números primos que se encuentra entre
	a y b (incluyendo a y b si son primos).
    Por defecto a=0, y b=100
"""

def primosRango(a=0, b=100):

	primos = [2]

	for num in range(2, b + 1):

		for primo in primos:

			if num % primo == 0:
				break
		else:
			primos.append(num)

	return tuple([p for p in primos if (p >= a and p <= b)])

#print(primosRango(a=0, b=200))