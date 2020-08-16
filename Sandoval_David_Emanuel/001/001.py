# 001-
# Programa que pregunte al usuario, el precio del producto y la cantidad de unidades vendidas.
# Informar el total de ventas.


precio = float(input("Precio: $ "))
unidades = int(input("Unidades: "))

print(f"Ventas: {unidades} unidades vendidas a $ {precio}")
print(f"Total: $", unidades * precio)
