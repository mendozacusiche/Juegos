import random
AHORCADO = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
 
palabras = """ hormiga babuino tejón murciélago oso castor camello gato almeja cobra puma
        coyote cuervo ciervo perro burro pato águila hurón zorro rana cabra ganso halcón
       león lagarto llama lunar mono alce ratón mula tritón nutria búho panda
       loro paloma pitón conejo ram rata cuervo rinoceronte foca salmón tiburón oveja
       zorrillo perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga
       comadreja ballena lobo wombat cebra """.split ()
       
def buscarPalabra(listaPalabras):
    # Esta función devuelve una cadena aleatoria de la lista de cadenas pasada .
     palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
     return listaPalabras[palabraAleatoria]

def displayBoard(letraIncorrecta, letraCorrecta, palabraSecreta):
    print(AHORCADO[len(letraIncorrecta)])
    print()
    
    print('Letras incorrectas :', end=' ')
     
    for letra in letraIncorrecta:
        print(letra, end=' ')
    print()

    espacio = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)): 
        # Reemplace espacios en blanco con correctamente;

        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
 
    for letra in espacio: # Muestra la palabra secreta con espacios en el medio .
         print(letra, end=' ')
    print("")

def elige_Letra(algunaLetra):
     # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
        
    while True:
         print("")
         print('Adivina una letra:')
         letra = input()
         letra = letra.lower()
         if len(letra) != 1:
             print('Ingrese una sola letra.')
         elif letra in algunaLetra:
             print('Ya has adivinado esa letra. Elige de nuevo.')
         elif letra not in 'abcdefghijklmnopqrstuvwxyz':
             print('Por favor ingrese una letra.')
         else:
             return letra

def comenzar():
     # Esta función devuelve True si el jugador quiere volver a jugar;
     

     print('¿Quieres volver a jugar? (Sí o no)')
     return input().lower().startswith('si')

def Jugar_ahorcado():
    print(' A H O R C A D O')
    letraIncorrecta = ''
    letraCorrecta = ''
    palabraSecreta = buscarPalabra(palabras)
    finJuego = False
    
    while True:
        displayBoard(letraIncorrecta, letraCorrecta, palabraSecreta)
    
         # Deje que el jugador ingrese una letra.
        letra = elige_Letra(letraIncorrecta + letraCorrecta)
    
        if letra in palabraSecreta:
            letraCorrecta = letraCorrecta + letra
    
            # Comprueba si el jugador ha ganado.
            letrasEncontradas = True
            for i in range(len(palabraSecreta)):
                if palabraSecreta[i] not in letraCorrecta:
                    letrasEncontradas = False
                    break
            if letrasEncontradas:
                print(' ¡Sí! ¡La palabra secreta es "' + palabraSecreta +
                       '"! ¡Has ganado!')
                finJuego = True
        else:
            letraIncorrecta = letraIncorrecta + letra
    
            # Compruebe si el jugador ha adivinado demasiadas veces y ha perdido.
            if len(letraIncorrecta) == len(AHORCADO) - 1:
                displayBoard(letraIncorrecta, letraCorrecta, palabraSecreta)
                print('\n ¡Se ha quedado sin letras! Despues de ' +
                    str(len(letraIncorrecta)) + ' letras erroneas y  ' +
                    str(len(letraCorrecta)) + '\n letras correctas, la palabra era "' + palabraSecreta + '"')
                finJuego = True
    
        # Pregunte al jugador si quiere volver a jugar (pero solo si el juego a terminado.
            
        if finJuego:
            if comenzar():
                letraIncorrecta = ''
                letraCorrecta = ''
                finJuego = False
                palabraSecreta = buscarPalabra(palabras)
            else:
                break