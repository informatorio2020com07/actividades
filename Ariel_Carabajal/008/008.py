import random
import os

#programado por Ariel Carabajal, Gral Pinedo. Chaco. Argentina

ahorcado = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ¡PERDISTE!''']

palabras = ['CAPITAN', 'CABALLO', 'GATUBELO', 'BATMAN', 
            'TERMOMETRO', 'SOMBRERO', 'KILOMETRO', 'AUTOMOVIL'
            'EDIFICIO', 'PELOTA', 'QUESO', 'QUILOMBO']

def buscar_palabras_aleatorias(lista_palabras):
    # Esta funcion retorna un indice aleatorio correspondiente a una palabra de la lista
    palabra_aleatoria = random.randint(0, len(lista_palabras) - 1)
    return lista_palabras[palabra_aleatoria]

def mostrar_tablero(ahorcado, letra_incorrecta, letra_correcta, palabra_secreta):
    print(ahorcado[len(letra_incorrecta)])

    espacio = '_' * len(palabra_secreta)
    for i in range(len(palabra_secreta)): # Remplaza los espacios en blanco por la letra bien escrita
        if palabra_secreta[i] in letra_correcta:
            espacio = espacio[:i] + palabra_secreta[i] + espacio[i+1:]

    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print(letra, end=' ')

def elije_letra(dato):
    # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
    while True:
        print("\n")
        letra = str(input('Adivina una letra: '))
        letra = letra.upper()
        if len(letra) != 1:
            print ('Elije una sola letra por favor') 
        elif letra in dato:
            print ('¡Ya has elegido esa letra!')
        elif not letra.isalpha():
            print ('Elije una letra wee!')
        else:
            return letra

def empezar():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

def limpiar(): 
    os.system("clear") #cambiar por "cls" para windows, limpia la pantalla

letra_incorrecta = ""
letra_correcta = ""
palabra_secreta = buscar_palabras_aleatorias(palabras)
finJuego = False

while True:
    limpiar()
    print ('A H O R C A D O')
    mostrar_tablero(ahorcado, letra_incorrecta, letra_correcta, palabra_secreta)
    # El usuairo elije una letra.
    letra = elije_letra(letra_incorrecta + letra_correcta)
    if letra in palabra_secreta:
        letra_correcta = letra_correcta + letra
        # Se fija si el jugador ganó
        letras_encontradas = True
        for i in range(len(palabra_secreta)):

            if palabra_secreta[i] not in letra_correcta:
                letras_encontradas = False
                break

        if letras_encontradas:
            print ('¡Muy bien! La palabra secreta es "' + palabra_secreta + '"\n  ¡GANASTE!')
            finJuego = True
    else:
        limpiar()
        letra_incorrecta = letra_incorrecta + letra
        # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
        if len(letra_incorrecta) == len(ahorcado) - 1:
            mostrar_tablero(ahorcado, letra_incorrecta, letra_correcta, palabra_secreta)

            print ('\n¡Te has quedado sin intentos!\nLa palabra era "' + palabra_secreta +'"')

            finJuego = True
    # Pregunta al jugador si quiere jugar de nuevo
    if finJuego:
        if empezar():
            letra_incorrecta = ""
            letra_correcta = ""
            finJuego = False
            palabra_secreta = buscar_palabras_aleatorias(palabras)
        else:
            break