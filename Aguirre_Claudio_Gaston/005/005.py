#Función que reciba como parametros dos números (a y b), y devuelva una tupla con todos los números primos que se encuentra entre a y b (incluyendo a y b si son primos). Por defecto a=0, y b=100

def num_primos(a=0, b=100):
	primos= []
	if a < 2:
		a=2
	for i in range (a,b+1):
		cont=0		
		for x in range (1,i+1):
			if (i % x) == 0:
				cont +=1
		if cont == 2:
			primos.append(i)
	primos=tuple(primos) 
	return primos


print(num_primos(4,97))