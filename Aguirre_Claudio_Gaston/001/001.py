#Programa que pregunte al usuario, el precio del producto y la cantidad de unidades vendidas.
#Informar el total de ventas.
precio=None
while precio==None:
	try:
		precio=float(input("introduce precio en formato $x.xx o similar: $"))
	except:
		print("introduce una cifra valida")

cantidad=None
while cantidad==None:
	try:
		cantidad=int(input("introduce la cantidad de productos requerida: "))
	except:
		print("introduce una cifra valida")

total=cantidad*precio

print("el total es: $"+ str(total))

		

