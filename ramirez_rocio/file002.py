def convertir_segundos_a_tiempo(segundos):
	hh=int(segundos/3600)
	minu=int((segundos-hh)/60)
	ss=segundos-minu
	print ("Hora: ",hh)
	print("Minutos: ",minu)
	print("Segundos: ",ss)


#segundos_usuario=int(input("Ingrese el tiempo en segundos: "))


#convertir_segundos_a_tiempo(segundos_usuario)


def tiempo_en_segundos(hora, minutos, segundos):
	segundos_=hora*3600+minutos*60+segundos
	print("Tiempo en segundos: ", segundos_)

#hh=int(input("Ingrese las horas: "))
#minu=int(input("Ingrese los minutos: "))
#ss=int(input("Ingrese los segundos: "))
#tiempo_en_segundos(hh, minu, ss)

def convertir_minutos_a_tiempo(minutos):
	hh=int(minutos/60)
	minu=int(minutos-hh*60)
	ss=(minutos-minu-hh*60)*60
	print ("Hora: ",hh)
	print("Minutos: ",minu)
	print("Segundos: ",ss)

#minu=int(input("Ingrese los minutos: "))
#convertir_minutos_a_tiempo(minu)