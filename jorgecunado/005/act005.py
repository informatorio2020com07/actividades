def esprimo(numero):
	
	if numero < 2:
		return False
	
	for n in range(2, numero):
		if numero % n == 0:
			return False
	
	return True		


def primos(a = 0, b = 100):
		
	lista=[]
	
	for a in range(a, b + 1):
		
		if esprimo(a):
			lista.append(a)
	
	return tuple(lista)		
