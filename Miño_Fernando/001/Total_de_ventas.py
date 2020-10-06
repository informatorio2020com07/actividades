

"""

001-
    Programa que pregunte al usuario, el precio del producto y la cantidad de unidades vendidas.
    Informar el total de ventas.

"""

print ("Bienvenido\n\n\n")
print ("Este programa calcular el total de ventas\n\n\n")

ventas = 0 
while True:

	while True:

		try:
		
			producto = float(input ("Ingrese precio del producto: "))
			break
		
		except ValueError:
		
			print ("\n\n\nError, Debe ingresar un Numero Real\n\n\n")

	while True:

		try:

			unidades = int (input ("Ingrese cantidadse vendidas: "))
			break

		except ValueError:

			print ("\n\n\nDebe ingresar un Entero\n\n\n")

	ventas +=1


	while True:

		caracter = input("\n\n\n¿Desea agregar otra venta?\n\n\n")

		if caracter == 's' or caracter == 'n':

			break

		else:

			print ("\n\n\ningrese solo [s] o [n]\n\n\n")

	if (caracter == 'n'):

		print ("Gracias por usar nuestro servicio ")

		break

"""
Dado que este programa es para mostrar los pasos de los procesos para verificar que estan bien, no se uso ningun cls.
"""		

print ("La Cantidad de Ventas fue: {}".format(ventas))






