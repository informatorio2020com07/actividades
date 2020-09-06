#!/usr/bin/python3
'''
004-

    Un programa que permita escribir varios modelos de cartas/notas
y que después pueda seleccionar un modelo de nota, y que me generé
varias notas reemplazando los destinatarios con una lista de nombres
que se le pase y el nombre del remitente indicado.
    
    Ej:
    ----
        Estimado (nombre):
            Le damos la bienvenida al servicio.

        Con afecto,
            (nombre_remitente)
    ----

    Pasandole lista destinatarios: Juan, Sandra y Jorge.
        Y remitente Axel.

    ----
        Estimado Juan:
            Le damos la bienvenida al servicio.

        Con afecto,
            Axel
    ----
        Estimado Sandra:
            Le damos la bienvenida al servicio.

        Con afecto,
            Axel
    ----

        Estimado Jorge:
            Le damos la bienvenida al servicio.

        Con afecto,
            Axel                        
    ----
'''
listaDestinatarios = []
modNotas={'1':'Nota A','2':'Nota B','3':'Nota C','4':'Nota propia'}

for key in modNotas:
    print(key,':',modNotas[key])

while True:
    try:
        opcion = int(input('Elija una opción de nota: '))

        num_destinatarios = int(input('¿Cuántos destinatarios desea ingresar?: '))
    
    except ValueError:
        print('Ingrese un número válido: ')
    else:
        break
    
for i in range(num_destinatarios): 
    nombres = input('Ingrese el nombre del destinatario: ')
    listaDestinatarios.append(nombres)
               
nombre_remitente = input('Ingrese nombre del remitente: ')

if opcion == 1:  
    for i in range(num_destinatarios):
        print('Estimado: ',listaDestinatarios[i])
        print('Le damos la bienvenida al servicio.')
        print('Con afecto: ',nombre_remitente,'\n')
elif opcion == 2:
    for i in range(num_destinatarios):
        print('Querido',listaDestinatarios[i])
        print('Lo extraño desesperadamente')
        print('Con cariño',nombre_remitente,'\n')
elif opcion == 3:
    for i in range (num_destinatarios):
        print('Buenos días',listaDestinatarios[i])
        print('Su motocicleta está lista para retirar del taller')
        print('Con respeto',nombre_remitente,'\n')
elif opcion == 4:
    nota_usuario=input('Ingrese su modelo de nota: ')
    for i in range (num_destinatarios):
        print(listaDestinatarios[i],nota_usuario)
        print(nombre_remitente)
else:
    print('la opción elegida no es una opción válida')