def primos(a=0,b=100):
    limite=5
    y=0
    for x in range(a,b+1):
        """controla que el numero sea primo"""
        if x!=1 and x!=0:
            flag=True
            if x>2:
                for i in range(2,x):
                    if (x%i) == 0:
                        flag=False
                        break

            if x==2 or flag:        
                """escribe en fila de 5 y tabula los numeros"""
                if len(str(x))<len(str(b)):
                    for i in range(0,(len(str(b))-len(str(x)))):
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
    primos(inicio,fin)

main()    