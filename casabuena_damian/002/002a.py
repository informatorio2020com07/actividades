import os

from b002 import *

os.system("cls")

segundos=int(input("Introduzca una cantidad de segundos:"))
hh,mm,ss=pasar_a_hhmmss(segundos)
print("{} segundos son:{} horas, {} minutos, {} segundos".format(segundos,hh,mm,ss))

a=input("Continuar")

os.system("cls")

minutos=int(input("Ingresar cantidad de minutos:"))
hh,mm,ss=pasar_a_hhmmss(minutos*60)
print("{} minutos son: {} horas, {} minutos, {} segundos".format(minutos,hh,mm,ss))

a=input("Continuar")

os.system("cls")

cadena=input("Ingrese caracteres en formato hh/mm/ss:")

hh=int(cadena[0:2])
mm=int(cadena[3:5])
ss=int(cadena[6:8])

print(" ")
print("horas: ",hh)
print("minutos: ",mm)
print("segundos: ",ss)
print("segundos equivalentes: {}".format(pasar_a_segundos(hh,mm,ss)))

