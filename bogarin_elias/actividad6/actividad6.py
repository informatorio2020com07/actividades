#006-
#Crear una función que reciba una lista de números y elimine
#los valores que se encuentran duplicados de la lista.
#Retornar la lista, y una tupla con los valores que han sido
#eliminados.

def duplicadosono():
    lista = [1,2,3,4,5,2,4,6,6,7,7,8,8,9,9]
    norepetidos=[]
    repetidos=[]
    for x in lista:
        if x not in norepetidos:
            norepetidos.append(x)
            #agrega los numeros no repetidos a la lista para mostrarlos luego en pantalla
        else:
            if x not in repetidos:
                repetidos.append(x)
                #agrega los numeros repetidos a la lista para luego volverlos tupla y mostrarlos (como si los eliminara)

    (tuple(repetidos))
    print ("no repetidos",norepetidos)
    print ("numeros repetidos: ",tuple(repetidos))
    
duplicadosono()
