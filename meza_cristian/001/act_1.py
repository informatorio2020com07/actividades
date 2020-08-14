'''
Programa que pregunte al usuario, el precio del producto y la cantidad de unidades vendidas.
Informar el total de ventas.
'''
print("Calculador de Ventas: ")
precio=float(input("Ingresar Precio del Producto $: "))
cantidad=int(input("Ingresar cantidad de unidades Vendidas : "))
print("El Importe Total de las Ventas Realizadas es: ${}".format(precio*cantidad))
