"""002-
Realizar un función que reciba como parámetro una cantidad de
segundos, y devuelva una tupla con la cantidad de segundos
expresada en hh,mm,ss"""

def convertidor_hh_mm_ss(cantidad_seg):
	seg=cantidad_seg%60
	minu=(cantidad_seg/60)%60
	hor=(cantidad_seg/60)/60
	resultado=int(hor),int(minu),int(seg)
	return resultado
"""Realizar una función que reciba como parámetros 
cantidades de horas, minutos y/o segundos.
 Y que retorne la suma de estos expresanda en 
 segundos. (Los parámetros, son opcionales y 
 por defecto sus valores 0.)"""
def suma_hh_mm_ss(hh=00,mm=00,ss=00):
 	hh_a_ss=3600*hh
 	mm_a_ss=60*mm

 	return hh_a_ss+mm_a_ss+ss
