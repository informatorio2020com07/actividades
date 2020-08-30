
def borra_duplicado(lista):
    """recibe una lista y borra los numeros repetidos"""
    borrados=[]
    for x in lista:
        if lista.count(x)>1:           
            if not x in borrados:
                borrados.append(x)
    
    return list(set(lista)),tuple(borrados)

if __name__=="__main__":
    lista1=[1,2,3,43,5,56,7,87,5,43,8,8,23,21,1,2,3,4,45,56,7,8,8,9,7,67,5,43,23,2,2,2]
    print(lista1)
    lis,tu=borra_duplicado(lista1)
    print(lis)
    print(tu)
    flag=True
    lista2=[]
    print("Ingrese su propia lista:")
    while flag:        
        num=input("carga tu numero si desea salir ingrese una letra: ")
        if num.isnumeric():
            lista2.append(int(num))
        else:
            flag=False            
    print(lista2)
    lis,tu=borra_duplicado(lista2)
    print(lis)
    print(tu)            