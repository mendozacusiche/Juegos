# Reversegam: a clone of Othello/Reversi
import random
import sys
Ancho = 8  #  El tablero tiene 8 espacios de ancho
Altura = 8 #  El tablero tiene 8 espacios de altura
def drawBoard(Tablero):
    # Imprime el tablero pasado a esta fune . Devolvera ninguno.
    print('  12345678')
    print(' +--------+')
    for y in range(Altura):
        print('%s|' % (y+1), end='')
        for x in range(Ancho):
            print(Tablero[x][y], end='')
        print('|%s' % (y+1))
    print(' +--------+')
    print('  12345678')

def getNewBoard():
    # crea uan nueve estructura de dato de tablero en blanco.
    Tablero = []
    for i in range(Ancho):
        Tablero.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return Tablero

def isValidMove(Tablero, tile, xstart, ystart):
    # Devuelve False si el movimiento del jugador en el espacio xstart, ystart no es válido..
    #  Si es un movimiento válido, devuelve una lista de espacios que se convertirían en los del jugador si hicieran un movimiento aquí..
    
    if Tablero[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # Primer paso en la direccion x
        y += ydirection # Primer paso en la direccion y
        while isOnBoard(x, y) and Tablero[x][y] == otherTile:
            # Siga moviendose en esta direccion x & y.
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and Tablero[x][y] == tile:
                # Hay piezas para voltear. Ir en la dirección inversa hasta llegar al espacio original, observando todas las fichas en el camino..
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    if len(tilesToFlip) == 0: # Si no se voltearon los mosaicos, este no es un.
        return False
    return tilesToFlip

def isOnBoard(x, y):
    # Devuelve True si las coordenadas se encuentran en el tablero..
    return x >= 0 and x <= Ancho - 1 and y >= 0 and y <= Altura - 1

def getBoardWithValidMoves(Tablero, tile):
    # Devuelve un nuevo tablero con puntos que marquen la validez movimientos que el jugador puede hacer..
    boardCopy = getBoardCopy(Tablero)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(Tablero, tile):
    # Devuelve una lista de [x, y] listas de movimientos válidos para el jugador dado en el tablero dado..
    validMoves = []
    for x in range(Ancho):
        for y in range(Altura):
            if isValidMove(Tablero, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def getScoreOfBoard(Tablero):
    # Determine la puntuación contando las fichas. Devuelve un diccionario  con las teclas 'X' y 'O'..
    xscore = 0
    oscore = 0
    for x in range(Ancho):
        for y in range(Altura):
            if Tablero[x][y] == 'X':
                xscore += 1
            if Tablero[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}

def enterPlayerTile():
    # Deje que el jugador ingrese la casilla que quiere ser..
    # Devuelve una lista con el mosaico del jugador como primer elemento y la computadora .
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('¿Quieres ser X u O?')
        tile = input().upper()

    #  El primer elemento en la lista es el mosaico del jugador, y el segundo es el mosaico de la computadora..
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Elige al azar quien va primero.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'Jugador'

def makeMove(Tablero, tile, xstart, ystart):
    # Coloque el mosaico en el tablero en xstart, ystart y voltee cualquiera de las.
    # Devuelve False si este es un movimiento no válido; Es cierto si es válido..
    tilesToFlip = isValidMove(Tablero, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    Tablero[xstart][ystart] = tile
    for x, y in tilesToFlip:
        Tablero[x][y] = tile
    return True

def getBoardCopy(Tablero):
    # Haga un duplicado de la lista de tableros y devuélvala.
    boardCopy = getNewBoard()

    for x in range(Ancho):
        for y in range(Altura):
            boardCopy[x][y] = Tablero[x][y]

    return boardCopy

def isOnCorner(x, y):
    # Devuelve True si la posición está en una de las cuatro esquinas..
    return (x == 0 or x == Ancho - 1) and (y == 0 or y == Altura - 1)

def getPlayerMove(Tablero, playerTile):
    # Deje que el jugador Ingrese su moverse.
    # Devuelve el movimiento como [x, y] (o devuelve las cadenas 'pistas' o 'salir').
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Ingrese su movimiento, "salga" para finalizar el juego, o " alternar sugerencias. .')
        move = input().lower()
        if move == 'quit' or move == 'hints':
            return move

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(Tablero, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('Eso no es un movimiento válido. Ingrese la columna (1-8) y luego la fila (1-8) .')
            print('Por ejemplo, 81 se moverá en la esquina superior derecha..')

    return [x, y]

def getComputerMove(Tablero, computerTile):
    # Dado un tablero y el mosaico de la computadora, determine dónde
    # mover y devolver ese movimiento como una lista [x, y].
    possibleMoves = getValidMoves(Tablero, computerTile)
    random.shuffle(possibleMoves) # randomize the order of the moves

    # Siempre vaya por una esquina si está disponible.
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # Encuentra el movimiento de mayor puntuación posible.
    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(Tablero)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def printScore(Tablero, playerTile, computerTile):
    scores = getScoreOfBoard(Tablero)
    print('Usted: %s puntos. Computadora: %s puntos.' % (scores[playerTile], scores[computerTile]))

def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print('El ' + turn + ' ira primero.')

    # Despeja el tablero y coloca las piezas iniciales..
    Tablero = getNewBoard()
    Tablero[3][3] = 'X'
    Tablero[3][4] = 'O'
    Tablero[4][3] = 'O'
    Tablero[4][4] = 'X'

    while True:
        playerValidMoves = getValidMoves(Tablero, playerTile)
        computerValidMoves = getValidMoves(Tablero, computerTile)

        if playerValidMoves == [] and computerValidMoves == []:
            return Tablero # Nadie puede moverse, así que finaliza el juego..

        elif turn == 'Jugador': # turno del jugador
            if playerValidMoves != []:
                if showHints:
                    validMovesBoard = getBoardWithValidMoves(Tablero, playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(Tablero)
                printScore(Tablero, playerTile, computerTile)

                move = getPlayerMove(Tablero, playerTile)
                if move == 'quit':
                    print('Gracias por jugar !')
                    sys.exit() # Termina el programa.
                elif move == 'hints':
                    showHints = not showHints
                    continue
                else:
                    makeMove(Tablero, playerTile, move[0], move[1])
            turn = 'computer'

        elif turn == 'computer': # turno de la computadora
            if computerValidMoves != []:
                drawBoard(Tablero)
                printScore(Tablero, playerTile, computerTile)

                input('Presione Enter para ver el movimiento de la computadora ')
                move = getComputerMove(Tablero, computerTile)
                makeMove(Tablero, computerTile, move[0], move[1])
            turn = 'Jugador'



def Jugar_reverse():
    print('Bienvenido a Reversegam!')
    
    playerTile, computerTile = enterPlayerTile()
    
    while True:
        finalBoard = playGame(playerTile, computerTile)
    
        # Muestra la puntuacion final.
        drawBoard(finalBoard)
        scores = getScoreOfBoard(finalBoard)
        print('X obtuvo %s puntos . O obtuvo %s puntos.' % (scores['X'], scores['O']))
        if scores[playerTile] > scores[computerTile]:
            print('Has vencido a la computadora por %s puntos! Felicitaciones !' % (scores[playerTile] - scores[computerTile]))
        elif scores[playerTile] < scores[computerTile]:
            print('Has perdio. La computadora te gano por %s puntos.' % (scores[computerTile] - scores[playerTile]))
        else:
            print('El juego fue un empate!')
    
        print('¿Quieres jugar de nuevo? (si or no)')
        if not input().lower().startswith('si'):
            break
        