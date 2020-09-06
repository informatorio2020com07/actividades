#!/usr/bin/python3

#001-
#   Programa que pregunte al usuario, el precio del producto
#	y la cantidad de unidades vendidas.
#   Informar el total de ventas.

while True:
    try:
        precioP = float(input ("Precio del producto: "))
        cantVen = int(input ("Cantidad Vendida: "))
    except ValueError:
        print("Ingrese un número válido: ")
    else:
        print ("Total de ventas: ", precioP * cantVen)
        break