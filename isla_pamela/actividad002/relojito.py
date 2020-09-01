from actividad002 import reloj
from actividad002 import relojero

print("*****Bienvenidos*****")

tiempo=input("Ingrese  los segundos: ")
print("")
horas,minutos,segundos=reloj(int(tiempo))
print("")
print("La cantidad de segundos son,hora {}, minutos {}, segundos{}".format(horas,minutos,segundos))
print("")
horas=int(input("ingrese horas: "))
minutos=int(input("Ingrese minutos: "))
segundos=int(input("Ingrese segundos: "))
print("")
print("")

segundos=relojero(horas, minutos,segundos)
print("")
print("La cantidad de segundos son {}".format(segundos))