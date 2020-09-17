"""En otro archivo, importar las funciones creadas.
Realizar un programa que"""
from funciones import convertidor_hh_mm_ss
from funciones import suma_hh_mm_ss
"""Primero pregunte por una cantidad de segundos, 
y diga cuantas horas, minutos y segundos son."""
print("CONVERTIDOR DE HS:MM:SS")
segun=int(input("ingrese la cantidad de segundo a convertir: "))
convertidor=convertidor_hh_mm_ss(segun)
print("expresado en hs:mm:ss",convertidor)

mm=int(input("ingrese la cantidad de minutos a convertir: "))
minu=suma_hh_mm_ss(0,mm)
print("expresado en hs:mm:ss",convertidor_hh_mm_ss(minu))
"""
 Después, solicitar al usuario ingresar una cantidad de tiempo expresada en una cadena de cáracter como "hs:mm:ss".
 Mostrar cuantas horas ingresó el usuario, cuantos minutos, y cuantos segundos en distintas lineas.
Luego mostrar a cuanto tiempo expresado en segundos equivale.
                
                Horas: 10
                Minutos: 30
                Segundos: 25
                Equivale a: 37825 Segundos."""
hh_mm_ss=input("ingrese cantidad de tiempo expresado en 'hs:mm:ss'(ej=02:34:56): ")
hh=int(hh_mm_ss[:2])
mm=int(hh_mm_ss[3:5])
ss=int(hh_mm_ss[6:8])
print("Horas:", hh)
print("Minutos:",mm)
print("Segundos:",ss)
s=suma_hh_mm_ss(hh,mm,ss)
print("Equivale a:",s,"segundos")

