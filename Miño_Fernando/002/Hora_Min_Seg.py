"""
002-
    Realizar un función que reciba como parámetro una cantidad de
    segundos, y devuelva una tupla con la cantidad de segundos
    expresada en hh,mm,ss.

    Realizar una función que reciba como parámetros cantidades de horas, minutos y/o segundos. 
    Y que retorne la suma de estos expresanda en segundos. 
    (Los parámetros, son opcionales y por defecto sus valores 0.)

"""






def Transf_Seg(seg):
	hh = seg//3600
	mm = seg%3600//60
	ss = seg%3600%60
	return print ("\nHora: ",hh,"Minutos: ",mm,"Segundos: ",ss,"\n")


def Transf_Min(Min):


	hh = Min//60
	ss = Min*60
	mm = ss%3600//60
	return print ("\nHora: ",hh,"Minutos: ",mm,"Segundos: ",ss,"\n")



def cantidad_Horas(hh=0,mm=0,ss=0):
	sumador = hh*3600+mm*60+ss
	print ("\nhora: ",hh,"\nminuto: ",mm,"\nSegundo: ",ss,"\nEquivale a: ",sumador," Segundos","\n")
	print ("Formato ==> {}:{}:{}".format(hh,mm,ss))



