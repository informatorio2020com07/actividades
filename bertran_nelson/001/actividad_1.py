""" Programa que pregunte al usuario, el precio del producto y la cantidad de unidades vendidas.
    Informar el total de ventas.
"""
def calcTotVenta():

	print("INFORME TOTAL DE VENTA:".center(10, "*"))
	
	precio = float(input("Ingrese precio del producto: "))

	cantidad = float(input("Ingrese cantidad de unidades vendidas: "))

	print("TOTAL DE VENTA:".center(10, "*"), cantidad*precio)

seguir = True

while seguir:

	while True:

		try:
			calcTotVenta()

			break;

		except ValueError:

			print("Ingrese numero! Intente otra ves")

		except:
			
			print("Ocurrio algun error! intente nuevamente")

	seguir = input("Presione n para salir, o cualquier tecla para continuar"
					+ " con otro calculo: ")

	if (seguir.lower()) == "n" :

		seguir = False