from os import system
from random import choice
from time import sleep

def titulo():
    tit="AHORCADO GAME!"
    print(tit.center(50, "="))
    
def carga_palabras():
    palabras=("AMOR","ROMA","PERRO","GATO","JUEGO","TELE","SILLON","HABITACION","CAMPERA","MOCHILA","CELULAR","PUERTA","COPA","BAÑERA","JARDIN")
    return choice(palabras)

def limpiar_pantalla():
    system("cls")

def dibuja_palabra(adivina):
    muestra=list(adivina.values())
    print("".join(muestra))
    
def adivina_dicc(palabra):
    adivina_pal={}
    for x in range(0,len(palabra)):
        adivina_pal.setdefault(x, " ____ ")      
    return adivina_pal

def controla_letra(letra, pal, adivina):
    bandera=False
    for x in range(0, len(pal)):
        if pal[x]==letra:
            adivina[x]=letra
            bandera=True
    return bandera

def controla_palabra_completa(adivina):
    bandera=False
    if " ____ " in adivina.values():
        print("FALTA MENOS!!!!")
        sleep(1)
    else:        
        bandera=True    
    return bandera

def imprime_pantalla(vidas,adivina,list_letra):
    limpiar_pantalla()
    titulo()
    print()
    print("Vidas Disponibles: ",vidas)
    print("Letras Utilizadas hasta el momento: ", list_letra)
    imprime_ahorcado(vidas)
    dibuja_palabra(adivina)

    
def juego_play():
    list_letra=[]
    pal=carga_palabras()
    adivina=adivina_dicc(pal)
    vidas=6
    while vidas>=0:
            imprime_pantalla(vidas, adivina, list_letra)
            letra=input("\nIngrese Letra: ")
            if letra.isdigit():
                print("Solo se Permiten Letras!!! Vuelva a Intentar")
                sleep(1)
            elif len(letra)>1:
                print("Solo se Permite 1 Letra por Vuelta!!! Vuelva a Intentar")
                sleep(1)
            elif letra=="":   
                print("Favor Ingresar Letra!!!")
                sleep(1)
            elif letra.upper() in list_letra: 
                print("Letra ya Utilizada!!! Vuelva a Intentar")
                sleep(1)
            else:
                control_vidas=controla_letra(letra.upper(), pal,adivina)
                list_letra.append(letra.upper())
                if control_vidas==False:
                    print("Letra no Encontrada!")
                    sleep(1)
                    vidas=vidas-1
                else:
                    completo=controla_palabra_completa(adivina)
                    if completo==True:
                        imprime_pantalla(vidas, adivina, list_letra)
                        print("GENIO!!!!! PALABRA CORRECTA!!!!")
                        sleep(4)
                        vidas=-1
                


def imprime_ahorcado(vidas):
    if vidas==6:
        print('''
          +---+
          |   |
          |
          |
          |
          |
    =========''')
    elif vidas==5:
        print('''
          +---+
          |   |
          |   O
          |
          |
          |
    =========''')
    elif vidas==4:
        print('''
          +---+
          |   |
          |   O
          |   |
          |
          |
    =========''')
    elif vidas==3:
        print('''
          +---+
          |   |
          |   O
          |  /|
          |
          |
    =========''')
    elif vidas==2:
        print('''
          +---+
          |   |
          |   O
          |  /|\\
          |
          |
    =========''')
    elif vidas==1:
        print('''
          +---+
          |   |
          |   O
          |  /|\\
          |  /
          |
    =========''')
    else:
        print('''
          +---+
          |   |
          |   O
          |  /|\\
          |  / \\
          |
    =========''')




    