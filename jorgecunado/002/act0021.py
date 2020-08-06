import os
from act002 import *

os.system("cls")

segundos = int(input("Ingresar cantidad de segundos :"))
hh,mm,ss = convertir_a_hhmmss(segundos)
print("{} segundos son : {} horas, {} minutos, {} segundos.".format(segundos, hh, mm, ss))

a = input("Seguir...")

os.system("cls")

minutos = int(input("Ingresar cantidad de minutos :"))
hh,mm,ss = convertir_a_hhmmss(minutos*60)
print("{} minutos son : {} horas, {} minutos, {} segundos.".format(minutos, hh, mm, ss))

a = input("Seguir...")

os.system("cls")

cadena=input("Ingrese cadena de caracteres en formato hh:mm:ss ")

hh=int(cadena[0:2])
mm=int(cadena[3:5])
ss=int(cadena[6:8])

print(" ")
print("Horas: ",hh)
print("Minutos: ",mm)
print("Segundos: ",ss)
print("Total de segundos equivalentes: {}.".format(convertir_a_segundos(hh,mm,ss)))
