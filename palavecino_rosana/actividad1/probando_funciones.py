#Realizar un programa que:
 #Primero pregunte por una cantidad de segundos, y diga cuantas horas,
 #minutos y segundos son.
        
 #Luego, preguntar por una cantidad de minutos y decir a cuantas
 #horas, minutos y segundos representa.

 #Después, solicitar al usuario ingresar una cantidad de tiempo 
 #expresada en una cadena de cáracter como "hs:mm:ss".
 #Mostrar cuantas horas ingresó el usuario, cuantos minutos, 
 #y cuantos segundos en distintas lineas.
 #Luego mostrar a cuanto tiempo expresado en segundos equivale.

from actividad2 import segundos,suma_segundos
segu=int(input("Ingrese la cantidad de segundos: "))
print(segundos(segu))
minu=int(input("Ingrese la cantidad de minutos: "))

print(suma_segundos(minutos=minu))
#print(segundos())
#print(suma_segundos())