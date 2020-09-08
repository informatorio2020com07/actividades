#Función que reciba como parametros dos números (a y b), y
#devuelva una tupla con todos los números primos que se encuentra entre
#a y b (incluyendo a y b si son primos).
#Por defecto a=0, y b=100

def primos():
	numero = 2

	yield numero
	
	while True:
		temp = numero
		while True:
			temp += 1
			contador_a = 1
			contador_divisores_b = 0
			while contador_a <= temp:
				if temp %  contador_a == 0:
					contador_divisores_b += 1
				if contador_divisores_b > 2:
					break

				contador_a += 1
			if contador_divisores_b == 2:
				yield temp


c = primos()
primos_muestra = [next(c) for _ in range(20)]
print(primos_muestra)
