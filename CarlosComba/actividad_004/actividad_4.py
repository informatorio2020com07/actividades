
def ingresar_nota():
    print("ingrese su nota  en el nombre de las persona ingrese 'destinatario' y 'remitente'\
 para salir escriba termine solo")
    """Recibe la nota en oraciones"""
    lista_nota=[]
    while True:
        print("Linea:",end=" ")
        nota=input("")
        if nota.lower()=="termine":
            break
        lista_nota.append(nota)   
    return lista_nota


def ingresar_personas():
    """recibe los destinatarios"""
    lista=[]
    while True:
        destinatario=input("Ingrese la persona destinatario, ingrese un numero \
para salir: ")
        print("")
        if destinatario.isnumeric():
            break
        lista.append(destinatario) 
    remitente=input("Ingrese la persona remitente: ")
    print(lista)    
    return lista,remitente

def cambiar_mensaje(nota_recibida,destinatario,remitente):
    for y,x in enumerate(nota_recibida):
        nota_recibida[y]=x.replace("destinatario",destinatario).replace("remitente",remitente)        
    return nota_recibida


def mostrar_nota(lista):
    print("")
    print("----")
    for x,linea in enumerate(lista):
        if x==0:
            print("    ",linea)
        elif x==len(lista)-1:
            print("    ",linea)
        else:
            print("  ",linea) 


def main():
    print("Manda tu mensaje")
    print("")
    nota=ingresar_nota()
    destinatarios,remitente=ingresar_personas()
    for destinatario in destinatarios:  
        mostrar_nota(cambiar_mensaje(nota,destinatario,remitente))


main()