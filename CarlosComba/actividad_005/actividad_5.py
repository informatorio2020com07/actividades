def primos(a=0,b=100):
    lista=[2,3,5,7]
    if a<=2:
        a=3
        primo=[2]
    else:
        primo=[]
    for x in range(a,b+1):
        """controla que el numero sea primo recorre solo primos 
        y lista base"""
        for i in lista+primo:
            if (x%i) == 0 and x!=i:
                break
        else:                    
            primo.append(x)
    return tuple(primo)                    

        
def mostrar_primos(tupla):
    y=0
    limite=5
    largo_de_ultimo=len(str(tupla[len(tupla)-1]))
    """escribe en fila de 5 y tabula los numeros"""
    for x in tupla:
        if len(str(x))<largo_de_ultimo:
            for i in range(0,largo_de_ultimo-len(str(x))):
                print(" ",end="")
            print(x,end=" ") 
        else:
            print(x,end=" ")
        y+=1    
        if y == limite:
            limite+=5
            print("")
       

def main():

    inicio=int(input("ingrese el inicio de lista numerica: "))
    fin=int(input("ingrese el fin de lista numerica: "))
    mostrar_primos(primos(inicio,fin))

main()