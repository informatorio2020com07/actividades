def eliminar_duplicados(lista):
    acu, eli = [], []
    for x in lista:
        if x in acu: eli.append(x)
        else:        acu.append(x)
    return acu, tuple(eli)

print(eliminar_duplicados([1,1,2,3,2,3,1]))
print(eliminar_duplicados([1,2,3,1,2,3,1,2,3]))

# modifica la lista argumento
def eliminar_duplicados_m(lista):
    elim = []

    i = 0
    while i < len(lista):
        try:
            j = lista.index(lista[i], i+1)
            elim.append(lista[j])
            del lista[j]
        except ValueError:
            i += 1

    return lista, tuple(elim)

print(eliminar_duplicados_m([1,1,2,3,2,3,1]))
print(eliminar_duplicados_m([1,2,3,1,2,3,1,2,3]))