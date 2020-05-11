# Tic Tac Toe

import random

def drawtablero(tablero):
    # Esta función imprime el tablero que se pasó.

    # "tablero" es una lista de 10 cadenas que representan el tablero (ignore elíndice 0).
    print(tablero[7] + '|' + tablero[8] + '|' + tablero[9])
    print('-+-+-')
    print(tablero[4] + '|' + tablero[5] + '|' + tablero[6])
    print('-+-+-')
    print(tablero[1] + '|' + tablero[2] + '|' + tablero[3])

def inputletra_Juegador():
    # Permite al jugador escribir qué letra quiere ser..
    # Devuelve una lista con la letra del jugador como primer elemento y el.
    
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('¿Quieres ser X o O?')
        letter = input().upper()

    #  El primer elemento en la lista es la letra del jugador; el segundo es la carta de la computadora..
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Elige al azar qué jugador va primero..
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(tablero, letter, mover):
    tablero[mover] = letter

def isWinner(bo, le):
    # Dada una tabla y la carta de un jugador, ese jugador ha ganado..
    # Usamos "bo" en lugar de "tablero" y "le" en lugar de "letra" para no tener que escribir tanto..
    
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #  en la parte superior
    (bo[4] == le and bo[5] == le and bo[6] == le) or # en el medio
    (bo[1] == le and bo[2] == le and bo[3] == le) or #  en la parte inferior
    (bo[7] == le and bo[4] == le and bo[1] == le) or #  Abajo del lado izquierdo
    (bo[8] == le and bo[5] == le and bo[2] == le) or # por el medio
    (bo[9] == le and bo[6] == le and bo[3] == le) or # por el lado  derecho
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def gettableroCopy(tablero):
    # Haga una copia de la lista del tablero y devuélvelo
    tableroCopy = []
    for i in tablero:
        tableroCopy.append(i)
    return tableroCopy

def isSpaceFree(tablero, mover):
    #  Return True si el movimiento pasado es libre en el tablero aprobado.
    return tablero[mover] == ' '

def getPlayermover(tablero):
    # Deja que el jugador entre en su movimiento
    mover = ' '
    while mover not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(tablero, int(mover)):
        print('¿Cuál es tu próximo movimiento? (1-9)')
        mover = input()
    return int(mover)

def chooseRandommoverFromList(tablero, moversList):
    # Devuelve un valor válido moverrrse de la lista aprobada en el tablero aprobado.
    # Devuelve Ninguno si no hay movimiento válido.
    possiblemovers = []
    for i in moversList:
        if isSpaceFree(tablero, i):
            possiblemovers.append(i)

    if len(possiblemovers) != 0:
        return random.choice(possiblemovers)
    else:
        return None

def getComputermover(tablero, letra_Computadora):
    # Dada un tablero y la letra de la computadora, determina dónde mover y devuelve ese movimiento..
    if letra_Computadora == 'X':
        letra_Juegador = 'O'
    else:
        letra_Juegador = 'X'

    # Aquí está el algoritmo para nuestra IA de Tic-Tac-Toe::
    # Primero, verifica si podemos ganar en el próximo movimiento
    for i in range(1, 10):
        tableroCopy = gettableroCopy(tablero)
        if isSpaceFree(tableroCopy, i):
            makeMove(tableroCopy, letra_Computadora, i)
            if isWinner(tableroCopy, letra_Computadora):
                return i

    # Comprueba si el jugador puede ganar en su próximo movimiento y bloquéalo..
    
    for i in range(1, 10):
        tableroCopy = gettableroCopy(tablero)
        if isSpaceFree(tableroCopy, i):
            makeMove(tableroCopy, letra_Juegador, i)
            if isWinner(tableroCopy, letra_Juegador):
                return i

    # Intenta tomar una de las esquinas, si están libres.
    mover = chooseRandommoverFromList(tablero, [1, 3, 7, 9])
    if mover != None:
        return mover

    # Intenta tomar el centro, si está libre.
    if isSpaceFree(tablero, 5):
        return 5

    # Muévete en uno de los lados.
    return chooseRandommoverFromList(tablero, [2, 4, 6, 8])

def istableroFull(tablero):
    # Devuelve True si se ha ocupado cada espacio en el tablero. De lo contrario, devuelve False..
    for i in range(1, 10):
        if isSpaceFree(tablero, i):
            return False
    return True

def Jugar_tateti():
    print('Bienvenido a Tic Tac Toe!')
    
    while True:
        # Restablecer el tablero
    
        El_Tablero = [' '] * 10
        letra_Juegador, letra_Computadora = inputletra_Juegador()
        turno = whoGoesFirst()
        print('El ' + turno + ' ira primero')
        gameIsPlaying = True
    
        while gameIsPlaying:
            if turno == 'player':
                # Player's turno.
                drawtablero(El_Tablero)
                mover = getPlayermover(El_Tablero)
                makeMove(El_Tablero, letra_Juegador, mover)
    
                if isWinner(El_Tablero, letra_Juegador):
                    drawtablero(El_Tablero)
                    print('¡Hurra! ¡Has ganado el juego!')
                    gameIsPlaying = False
                else:
                    if istableroFull(El_Tablero):
                        drawtablero(El_Tablero)
                        print('¡El juego es un empate!')
                        break
                    else:
                        turno = 'computer'
    
            else:
                # turnoo de la computadora.
                mover = getComputermover(El_Tablero, letra_Computadora)
                makeMove(El_Tablero, letra_Computadora, mover)
    
                if isWinner(El_Tablero, letra_Computadora):
                    drawtablero(El_Tablero)
                    print('¡La computadora te ha derrotado! Tú pierdes')
                    gameIsPlaying = False
                else:
                    if istableroFull(El_Tablero):
                        drawtablero(El_Tablero)
                        print('El juego es un empate!')
                        break
                    else:
                        turno = 'player'
    
        print('¿Quieres jugar de nuevo? (sí o no )' )
        if not input().lower().startswith('si'):
            break
        