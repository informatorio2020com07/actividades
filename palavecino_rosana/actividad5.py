#Función que reciba como parametros dos números (a y b), y
#devuelva una tupla con todos los números primos que se encuentra entre
#a y b (incluyendo a y b si son primos).
    #Por defecto a=0, y b=100

def primos(a=0,b=100):
	mult=[]
	lista=[]
	tamizar=[True]*(b+1) 
	
	for p in range (2, b+1):#tamiza los múltiplos de 2 hasta b
		if(tamizar[p]):
			mult.append(p)
			
			if p>=a: #agrega a una lista los números primos mayores o iguales a a
				lista.append(p)
				
			for i in range (p, b+1, p):#descarta los números que no son primos
				tamizar[i]=False
	tupla=tuple(lista)


	return tupla

print(primos(23,111))


