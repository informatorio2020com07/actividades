from actividad_2 import cantSegundos, devuelveSegundos
import time
from datetime import datetime

def principal():
	
	# PREGUNTA CANT DE SEGUNDOS, DEVUELVE HORARIO
	segus = int(input("Ingrese la cantidad de segundos que desea pasar a horarios: "))
	print(cantSegundos(segus))


	# PREGUNTA CANT DE MINUTOS, DEVUELVE HORA Y SEGUNDOS
	minus = int(input("Ingrese la cant de minutos que desea pasar a horarios: "))
	segundos = minus * 60
	horaDesdeSeg = cantSegundos(segundos)

	print("minutos {} equivale al horario: {} . Son {} segundos"
		.format(minus, str(horaDesdeSeg), segundos)) 
	
	# PEDIR INGRESO Y DEVOLVER EN FORMATO FILA Y EL EQUIVALENTE EN SEGUNDOS
	horaIngresada = input('Ingrese horario con formato "hs:mm:ss" : ')
	#print("hora ingresada", horaIngresada)
	hora = datetime.strptime(horaIngresada, '%H:%M:%S').time()
	#print("en formato hora: ", hora)
	#print(type(hora))

	hh = hora.hour
	mm = hora.minute
	ss = hora.second

	print("Horas: ", hh)
	print("Minutos: ", mm)
	print("Segundos: ", ss)
	print("El horario equivale a {} segundos totales"
		.format(devuelveSegundos(hora=hh, minuto=mm, segundo=ss)))

if __name__ == "__main__":

    principal()