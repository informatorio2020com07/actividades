from time import sleep
from juego import limpiar_pantalla, titulo, juego_play


limpiar_pantalla()
jugar=True
while jugar:
    try:
        titulo()
        print("\nFavor Seleccionar Opcion:")
        res=int(input("1- Jugar:\n2- Salir\nOpcion: "))
        if res==1:
            juego_play()
            limpiar_pantalla()
        elif res==2:
            jugar=False
        else:
            print("Volver a Intentar!")
            sleep(1)
            limpiar_pantalla()
    except:
        print("Error en Seleccion. Volver a Intentar!")
        sleep(1)
        limpiar_pantalla()
        
limpiar_pantalla()
print("Muchas Gracias. Vuelva Pronto!")


    