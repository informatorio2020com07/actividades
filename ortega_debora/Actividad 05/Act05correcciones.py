#Funcion para buscar primos
a = 0
b = 100
def buscador_Primos(a, b):
    primos =[]
    
    for x in range(a, b+1):
        contador = 0
        for i in range(1, x+1):
            if x % i == 0:
                contador += 1
        if contador == 2:
            primos.append(x)

    return primos

print(buscador_Primos(a, b))
