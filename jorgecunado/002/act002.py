
def convertir_a_hhmmss(segundos):
	#recibe segundos y los convierte al formato HH,MM,SS
	horas = segundos//3600
	segundos_exed = segundos%3600
	minutos = segundos_exed//60
	segundos = segundos_exed%60
	return horas, minutos, segundos

def convertir_a_segundos(horas = 0, minutos = 0, segundos = 0):
	#Convierte los parametros de hora, minutos, segundos a segundos
	csegundos = (horas*3600) + (minutos * 60) + segundos
	return csegundos