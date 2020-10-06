"""Programa que pregunte al usuario, el precio del producto y la cantidad de unidades vendidas.
    Informar el total de ventas."""

precio_producto=float(input("Ingrese el precio del producto: $"))
cantidad_unidades=int(input("Ingrese la cantidad de unidades: "))
print("El total de ventas es: $",precio_producto*cantidad_unidades)    