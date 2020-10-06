# 1- Realizar un función que reciba como parámetro una cantidad de
# segundos, y devuelva una tupla con la cantidad de segundos
# expresada en hh,mm,ss.

#2-Realizar una función que reciba como parámetros cantidades de horas, minutos y/o segundos. 
#Y que retorne la suma de estos expresanda en segundos. (Los parámetros, son opcionales y por defecto sus valores 0.)


def segundos(seg):
	
    
	segu=seg%60
	coc=seg//60
	minu=coc%60
	hora=coc//60
	
	return(hora,minu,segu)

def suma_segundos(horas=0,minutos=0,segundos=0):
	
	segundos=horas*3600 + minutos*60 + segundos
	return(segundos)

print(segundos(3652))

print(suma_segundos(1,1,1))