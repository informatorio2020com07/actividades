def segundero(segundos):
	horas = segundos//3600
	minutos = segundos%3600//60
	segundos = segundos%3600%60
	return (horas, minutos, segundos)

def horatero(horas = 0, minutos = 0, segundos = 0):
	segundos = horas*3600 + minutos*60 + segundos
	return (segundos)
	
#print(horatero(2, 25, 45))

#print(segundero(horatero(2, 25, 45)))