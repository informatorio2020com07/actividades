#Guia: 1. Elegir una palabra de manera aleatoria
#      2. Mostar el dibujo
#      3. Mostrar guion por cada letra 
#      4. Pedir una letra

nombre=input("¿Como te llamas?: ")
print("Hola, "+nombre,"preparando el juego.... VAMOS ")
print("")
from time import sleep
sleep(1.5)
print("Comienza a adivinar")
sleep(1.5)

import random
# tres comillas dobles al comenzar y al terminar nuestro texto, 
# para que ocupe varias líneas
AHORCADO = ['''
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
    =========''']

palabras = ["balija", "lagartija", "viajes", "comercio", "desafios", "felinos", "camilla", "maternidad", "amigos", "arroz", "pollo", "piara", "muercielago", "hermanos", "familia", "lazo"]

palabra = random.choice(palabras)

def buscarPalabraAleat(listaPalabras):
    # una palabra aleatoria
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]


def elijeLetra(algunaLetra):
    # ver la letra que se ingreso y hace que el jugador ingrese solo una letra, avisa si ya se repitio la letra y que solo sean letras
    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce una sola letra.') 
        elif letra in algunaLetra:
            print ('Ya has elegido esa letra. Prueba con otra!')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letra

#para incorporar letras y que muestre si no es correcta la agrega al costado para mostarle al juador
def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(AHORCADO[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)): # para los espacios en para la letra bien escrita
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: #ver la palabra secret con espacios entre letras
        print (letra, fin)
    print ("")


def empezar():
    # devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

print ('A H O R C A D O')
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscarPalabraAleat(palabras)
finJuego = False
while True:
    displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
    # El usuairo elije una letra.
    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        # Se fija si el jugador ganó
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ('¡Muy bien! La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
        if len(letraIncorrecta) == len(AHORCADO) - 1:
            displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
            print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
            finJuego = True

    # Pregunta al jugador si quiere jugar de nuevo
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabraSecreta = buscarPalabraAleat(palabras)
        else:
            break