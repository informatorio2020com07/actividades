def eliminar_duplicados(lista):
    acu, eli = [], []
    for x in lista:
        if x in acu: eli.append(x)
        else:        acu.append(x)
    return (acu, tuple(eli))

print(eliminar_duplicados([1,1,2,3,2,3,1]))
