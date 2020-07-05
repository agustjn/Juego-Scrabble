import PySimpleGUI as sg
from const import *

def Tablero():
    ''' Esta Funcion consiste en generar el tablero de botones 15x15 en
        donde seran colocadas las letras de cada jugador durante el juego '''
    tablero = [[sg.Button(
                size=board_button_size,
                button_color=('black',  'grey'),
                key=(x,y),
                pad=board_padd_size)
                for x in range(15)]for y in range(15)]
    return tablero

def Botones():
    ''' Esta Funcion consiste en definir los botones varios que permiten
        posponer,terminar,mostrar en pantalla el top 10 puntajes y las reglas
        del juego '''
    botones = [[sg.Button('POSPONER', size=button_size)],
               [sg.Button('TERMINAR', size=button_size)],
               [sg.Button('TOP 10', size=button_size)],
               [sg.Button('REGLAS', size=button_size)]]
    return botones

def Puntos_jugador():
    ''' Esta Funcion consiste en definir la ventana en donde iran los puntos
        del jugador'''
    puntos_jugador = [[sg.Text('Puntaje Jugador',
                               size=(13, 1),
                               justification='center')],
                      [sg.Text('',key='Puntos_jugador',
                                  size=button_size)]]
    return puntos_jugador

def Puntos_cpu():
    ''' Esta Funcion consiste en definir la ventana en donde iran los puntos
        del cpu '''
    puntos_cpu = [[sg.Text('Puntaje CPU',
                           size=(13, 1),
                           justification='center')],
                  [sg.Text('',key='Puntos_cpu',
                              size=button_size)]]
    return puntos_cpu

def Turno_actual():
    turno_actual= [[sg.Text('Turno = ',size=turno_text_size),sg.Text('',key='Turno')]]
    return turno_actual

def Puntos_Y_Botones(puntos_jugador,puntos_cpu,botones,turno_actual):
    ''' Esta Funcion consiste en colocar en colocar en columnas los distintos
        elementos que presenta el tablero '''
    puntos_botones = [[sg.Column(puntos_jugador)],
                      [sg.Column(puntos_cpu)],
                      [sg.Column(botones)],
                      [sg.Column(turno_actual)]]
    return puntos_botones

def Letras_jugador():
    ''' Esta funcion consiste en crear la mano del jugador la cual va a recibir
        las letras durante el juego consta de 7 botones '''
    letrasJ = ['',  '',  '',  '',  '',  '',  '']
    letras_jugador = [[sg.Button(letrasJ[x],  key=('Jugador',x),  size=(3, 1),
                       pad=board_padd_size)for x in range(7)]]
    return letras_jugador

def Letras_cpu():
    ''' Esta funcion consiste en crear la mano del cpu la cual va a recibir
        las letras durante el juego consta de 7 botones '''
    letrasC = ['',  '',  '',  '',  '',  '',  '']
    letras_cpu = [[sg.Button(letrasC[x],  key=('Cpu',x),  size=(3, 1),
                   pad=board_padd_size)for x in range(7)]]
    return letras_cpu

def Botones_Turno():
    ''' Esta funcion consiste en crear los botones que van acompañados con la
        mano del jugador los cuales permiten cambiar y dar fin del turno del
        jugador '''
    botones_turno = [[sg.Button('Cambiar Fichas',
                                     size=button_size),
                           sg.Button('Fin De Turno',
                                     size=button_size)]]
    return botones_turno

def Atril_jugador(letras_jugador,botones_turno):
    ''' Esta funcion consiste en crear el atril del jugador colocando en
        columnas la mano del jugador y los botones del turno '''
    atril_jugador = [[sg.Text('Atril Jugador',
                              size=text_atril_size)],
                     [sg.Column(letras_jugador)],
                     [sg.Column(botones_turno)]]
    return atril_jugador

def Atril_cpu(letras_cpu):
    ''' Esta funcion consiste en crear el atril del cpu colocando en
        columna la mano del cpu '''
    atril_cpu = [[sg.Text('Atril CPU',
                          size=text_atril_size)],
                 [sg.Column(letras_cpu)]]
    return atril_cpu

def Layout(tablero,puntos_botones,atril_jugador,atril_cpu):
    ''' Esta funcion consiste en juntar todos los elementos anteriores para
        formar el tablero y las demas funcionalidades del juego'''
    layout = [[sg.Column(tablero),
               sg.Column(puntos_botones)],
              [sg.Column(atril_jugador),
               sg.Column(atril_cpu)]]
    return layout

def Window(layout,nivel):
    ''' Esta funcion consiste en darle todos los elementos del tablero mediante
        el layout a la ventana la cual permite crear la interfaz del tablero'''
    window = sg.Window('Tablero de juego nivel '+nivel,
                       margins=marg_size,
                       element_padding=padd_size,
                       font=font_size,
                       location=window_location).Layout(layout).Finalize()
    return window

def Crear_Tablero(colores,window):
    ''' Esta funcion consiste en recibir un diccionario de colores para
        actualizar las casillas segun que nivel de tablero sea'''
    matriz_tablero = {(x,y): {'letra': '',  'color_casilla': ''}
                      for x in range(15)for y in range(15)}
    for color,  casillas in colores.items():
        for casilla in casillas:
            window.Element(casilla).Update(button_color=('black',color))
            matriz_tablero[casilla]['color_casilla'] = color
    return matriz_tablero
#str(x)+','+str(y)
