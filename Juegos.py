import PySimpleGUI as sg
import json 
import time
from ahorcado import Jugar_ahorcado
from tictactoe import Jugar_tateti
from reversegam import Jugar_reverse
# armando una columna

columna_1 = [
                [sg.Text('Nombre'), sg.Input(key='nombre')],
                [sg.Text('Alias'), sg.Input(key='alias')]
            ]

columna_2 = [
              [sg.Text('Juegos'), sg.Listbox(values=('Ahorcado', 'Tateti', 'Reverse'), size=(30,1))],
              [sg.Text('Juego'), sg.Input(key='juego')]
            ]

#Armo el diseño de la interdace

diseño = [
    
         [sg.Text('Ingresa tus datos')],
         [sg.Column(columna_1, background_color= 'blue'), sg.Column(columna_2, background_color='pink')],
         [sg.Button('Cargar'), sg.Exit()]
]

#suario = sg.popup_get_text('Usuario')
#password = sg.popup_get_text('Password: (contraseña)', password_char='*')
 
def escribirArchivoJugadores(jugadores):
    with open('Jugadores.json', 'w') as archivo:
        json.dump(jugadores, archivo)
        

def cargarJugador(values):

    escribirArchivoJugadores(values)    
    juego =  str(values['juego'])
    
    if juego in 'Ahorcado':
        Jugar_ahorcado()
    elif  juego in 'Tateti':
        Jugar_tateti()
    elif juego in 'Reverse':
        Jugar_reverse()
    

def leerArchivoJugadores():
    
    with open('Jugadores.json', 'r') as archivo:
        datos = json.load(archivo)
    return datos


#print(values['nombre'])
#print(values['contraseña'])
#print(values['juego'])          

window = sg.Window('Datos del Jugador').Layout(diseño)
    
while True:

    (event, values) = window.Read()

    if event is None or event =='Exit':
        break
    elif event == 'Cargar':
        if values['nombre'] == '' or values['alias'] == '' or values['juego'] == '' :
            sg.Popup('Falta completar algun campo')
        else:
            cargarJugador(values)
    
    ListJugadores = leerArchivoJugadores()    

    print("Lista de Jugadores que Jugaron los juegos")

    print(ListJugadores)





