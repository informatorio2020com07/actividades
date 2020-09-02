
def primos(a=0,b=100):
	primos = []
	for x in range(a,b+1):
		if x%2 == 0 and x!=2:
			continue
			#print(x, "no es primo porque es al menos múltiplo de 2")
		elif x%3 == 0 and x!=3:
			continue
			#print(x, "no es primo porque es al menos múltiplo de 3")
		elif x%5 == 0 and x!=5:
			continue
			#print(x, "no es primo porque es al menos múltiplo de 5")
		elif x%7 == 0 and x!=7:
			continue
			#print(x, "no es primo porque es al menos múltiplo de 7")
		elif x%11 == 0 and x!=11:
			continue
			#print(x, "no es primo porque es al menos múltiplo de 11")
		elif x==1:
			print("1 no es primo ni compuesto")
		else:
			#print(x, "es primo")
			primos.append(x)
	print("Números primos entre ", a, " y ", b,": ", primos)
	return tuple(primos)
	#print(tuple(primos)

primos(0,15)
	