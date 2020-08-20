 # Función que reciba como parametros dos números (a y b), y
# devuelva una tupla con todos los números primos que se encuentra entre
# a y b (incluyendo a y b si son primos).
# Por defecto a=0, y b=100
# Por defecto a=0, y b=100


def devolvertupla(a=0,b=100):
   if a >= b: 
      for a in range(2, b + 1):
         primos = True
      for j in range(2,11):
         if a == j:
            break
         elif a%j == 0:
            primos = False
         else:
            continue
         if primos == True:
               print (' ',i, end='')
               cont += 1
   print ('\nHay %u números primos.' % cont )

#para probar que funciona
lista = int(input("¿Hasta qué número quieres la lista?:\n "))
cont = 0
for i in range(2, lista + 1):
    primos = True
    for j in range(2,11):
        if i == j:
           break
        elif i%j == 0:
           primos = False
        else:
           continue
    if primos == True:
        print(' ',i, end='')
        cont += 1
print('\nHay %u números primos.' % cont )
