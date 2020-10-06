
## 004-

##Un programa que permita escribir varios modelos de cartas/notas
#y que después pueda seleccionar un modelo de nota, y que me generé
#varias notas reemplazando los destinatarios con una lista de nombres
#que se le pase y el nombre del remitente indicado.
import random

menu=int(input("Que desea hacer?\n---1-Escribir Carta\n---2-Ver estilos"))
if menu==1:
    agregar=True
    while agregar:
        listad=input("A quien va dirigida la carta?\n")
        listar=input("Quien la escribe?\n") 
        preguntas=int(input("Que estilo desea?\n"))
        if preguntas==2 or preguntas==3:
            dias=int(input("Que dia fue escrita la carta?\n"))
            mess=int(input("En que mes?\n"))
            años=int(input("En que año\n"))
            dia=[dias]
            mes=[mess]
            año=[años]
            ciudad=input("En que ciudad se escribio?")
        destinatario=[listad]
        remitente=[listar]
        estilo=[preguntas]


        continuar=int(input("Desea agregar mas destinatarios?\n 1-Si  0-No"))
        if continuar==0:
            agregar=False
            pass
        txt=input("Escriba aqui su carta :\n")
        texto=[txt]
        for x in range(0, len(destinatario)):
            for j in range(0, len(remitente)):
                    if preguntas == 1:                  
                        print("!--------------------!")
                        print("Querido ", destinatario," : ")
                        print(texto)
                        print("!--------------------!")
                        print("Atentamente", remitente)
                        print("                       ")
                        print("                        ")
                        print("                        ")
                    elif preguntas== 2:
                        print("!!!!!!!!!!!!!!!!!")
                        print("                           {}/{}/{}   Ciudad:".format(dia,mes,año),ciudad)  
                        print("*******************************************************")
                        print("Estimado",destinatario,": ")
                        print("                         ",texto)
                        print("*********************************************************")
                        print("Me despido,",remitente)
                        print("!!!!!!!!!!!!!!!!!!")
                    elif preguntas==3:
                        #seria una carta mas como para o desde un trabajo queriendo informar sobre x suceso
                        razon=input("Para que va dirigida la carta?")
                        print("Me dirijo a usted para informarle sobre:",razon)
                        print("En el dia de la fecha  {}/{}/{}".format(dia,mes,año))
                        print("\n De parte de: ",destinatario)
                        print("\n Para comentarle que",texto)
if menu==2:
    print("Estilos**************************")
    print("Estilo 1--")
    print("!--------------------!")
    print("Querido Destinatario: ")
    print(" TEXTO-----------------")
    print("-----------Texto-----------")
    print("-----TEXTO-----------")
    print("!--------------------!")
    print("Atentamente: Remitente")
    print("                       ")
    print("                        ")                       
    print("                        ")
    print("\n                                \n                               \n                       \n")
    print("Estilo 2----")
    print("!!!!!!!!!!!!!!!!!")
    print("                                     Fecha(Dia,mes,Año)          Ciudad: en la cual se escribio la carta")  
    print("*******************************************************")
    print("Estimado : Destinatario ")
    print("----------Texto-----------")
    print("--------------Texto-----------")
    print("------------texto-----------")
    print("-----------Texto---------")
    print("*********************************************************")
    print("Me despido,atte Remitente")
    print("!!!!!!!!!!!!!!!!!!")
    print("\n                         \n                        \n                    \n                ")
    print("Estilo 3-----")
    print("                                 ")
    print("Me dirijo a usted: Destinatario para informarle sobre: Motivo/Razon")
    print("En el dia de la fecha     Dia,Mes,Año")
    print("\n De parte de: Remitente")
    print("\n Para comentarle que: ----------------------Texto--------------")
    print("----------------------Texto---------------")
    menu=int(input("Que desea hacer ahora?\n 1-Escribir carta\n2- Ver de nuevo Estilos\n"))
if menu==1:
    agregar=True
    while agregar:
        listad=input("A quien va dirigida la carta?\n")
        listar=input("Quien la escribe?\n") 
        preguntas=int(input("Que estilo desea?\n"))
        if preguntas==2 or preguntas==3:
            dias=int(input("Que dia fue escrita la carta?\n"))
            mess=int(input("En que mes?\n"))
            años=int(input("En que año\n"))
            dia=[dias]
            mes=[mess]
            año=[años]
            ciudad=input("En que ciudad se escribio?")
        destinatario=[listad]
        remitente=[listar]
        estilo=[preguntas]


        continuar=int(input("Desea agregar mas destinatarios?\n 1-Si  0-No"))
        if continuar==0:
            agregar=False
            pass
        txt=input("Escriba aqui su carta :\n")
        texto=[txt]
        for x in range(0, len(destinatario)):
            for j in range(0, len(remitente)):
                    if preguntas == 1:                  
                        print("!--------------------!")
                        print("Querido ", destinatario," : ")
                        print(texto)
                        print("!--------------------!")
                        print("Atentamente", remitente)
                        print("                       ")
                        print("                        ")
                        print("                        ")
                    elif preguntas== 2:
                        print("!!!!!!!!!!!!!!!!!")
                        print("                           {}/{}/{}   Ciudad:".format(dia,mes,año),ciudad)  
                        print("*******************************************************")
                        print("Estimado",destinatario,": ")
                        print("                         ",texto)
                        print("*********************************************************")
                        print("Me despido,",remitente)
                        print("!!!!!!!!!!!!!!!!!!")
                    elif preguntas==3:
                        #seria una carta mas como para o desde un trabajo queriendo informar sobre x suceso
                        razon=input("Para que va dirigida la carta?")
                        print("Me dirijo a usted para informarle sobre:",razon)
                        print("En el dia de la fecha  {}/{}/{}".format(dia,mes,año))
                        print("\n De parte de: ",destinatario)
                        print("\n Para comentarle que",texto)
if menu==2:
    print("Estilos**************************")
    print("Estilo 1--")
    print("!--------------------!")
    print("Querido Destinatario: ")
    print(" TEXTO-----------------")
    print("-----------Texto-----------")
    print("-----TEXTO-----------")
    print("!--------------------!")
    print("Atentamente: Remitente")
    print("                       ")
    print("                        ")                       
    print("                        ")
    print("\n                                \n                               \n                       \n")
    print("Estilo 2----")
    print("!!!!!!!!!!!!!!!!!")
    print("                                     Fecha(Dia,mes,Año)          Ciudad: en la cual se escribio la carta")  
    print("*******************************************************")
    print("Estimado : Destinatario ")
    print("----------Texto-----------")
    print("--------------Texto-----------")
    print("------------texto-----------")
    print("-----------Texto---------")
    print("*********************************************************")
    print("Me despido,atte Remitente")
    print("!!!!!!!!!!!!!!!!!!")
    print("\n                         \n                        \n                    \n                ")
    print("Estilo 3-----")
    print("                                 ")
    print("Me dirijo a usted: Destinatario para informarle sobre: Motivo/Razon")
    print("En el dia de la fecha     Dia,Mes,Año")
    print("\n De parte de: Remitente")
    print("\n Para comentarle que: ----------------------Texto--------------")
    print("----------------------Texto---------------")
