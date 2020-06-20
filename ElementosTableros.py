import PySimpleGUI as sg
from const import *

def Tablero():
    tablero = [[sg.Button('{},{}'.format(x, y),
                size=board_button_size,
                button_color=('black',  'grey'),
                key=str(x)+','+str(y),
                pad=board_padd_size)
                for x in range(15)]for y in range(15)]
    return tablero

def Botones():
    botones = [[sg.Button('POSPONER', size=button_size)],
               [sg.Button('TERMINAR', size=button_size)],
               [sg.Button('TOP 10', size=button_size)],
               [sg.Button('REGLAS', size=button_size)]]
    return botones

def Puntos_jugador():
    lista = []
    puntos_jugador = [[sg.Text('Puntaje Jugador',
                               size=(13, 1),
                               justification='center')],
                      [sg.Listbox(lista,
                                  key='Puntos_jugador',
                                  size=button_size)]]
    return puntos_jugador

def Puntos_cpu():
    lista = []
    puntos_cpu = [[sg.Text('Puntaje CPU',
                           size=(13, 1),
                           justification='center')],
                  [sg.Listbox(lista,
                              key='Puntos_cpu',
                              size=button_size)]]
    return puntos_cpu

def Turno_actual():
    turno_actual= [[sg.Text('Turno = ',size=turno_text_size),sg.Text('',key='Turno')]]
    return turno_actual

def Puntos_Y_Botones(puntos_jugador,puntos_cpu,botones,turno_actual):
    puntos_botones = [[sg.Column(puntos_jugador)],
                      [sg.Column(puntos_cpu)],
                      [sg.Column(botones)],
                      [sg.Column(turno_actual)]]
    return puntos_botones

def Letras_jugador():
    letrasJ = ['',  '',  '',  '',  '',  '',  '']
    letras_jugador = [[sg.Button(letrasJ[x],  key=str(x)+'J',  size=(3, 1),
                       pad=board_padd_size)for x in range(7)]]
    return letras_jugador

def Letras_cpu():
    letrasC = ['',  '',  '',  '',  '',  '',  '']
    letras_cpu = [[sg.Button(letrasC[x],  key=str(x)+'C',  size=(3, 1),
                   pad=board_padd_size)for x in range(7)]]
    return letras_cpu

def Botones_Turno():
    botones_turno = [[sg.Button('Cambiar Fichas',
                                     size=button_size),
                           sg.Button('Fin De Turno',
                                     size=button_size)]]
    return botones_turno

def Atril_jugador(letras_jugador,botones_turno):
    atril_jugador = [[sg.Text('Atril Jugador',
                              size=text_atril_size)],
                     [sg.Column(letras_jugador)],
                     [sg.Column(botones_turno)]]
    return atril_jugador

def Atril_cpu(letras_cpu):
    atril_cpu = [[sg.Text('Atril CPU',
                          size=text_atril_size)],
                 [sg.Column(letras_cpu)]]
    return atril_cpu

def Layout(tablero,puntos_botones,atril_jugador,atril_cpu):
    layout = [[sg.Column(tablero),
               sg.Column(puntos_botones)],
              [sg.Column(atril_jugador),
               sg.Column(atril_cpu)]]
    return layout

def Window(layout,nivel):
    window = sg.Window('Tablero de juego nivel '+nivel,
                       margins=marg_size,
                       element_padding=padd_size,
                       font=font_size,
                       location=window_location).Layout(layout).Finalize()
    return window

def Crear_Tablero(colores,window):
    matriz_tablero = {str(x)+','+str(y): {'letra': '',  'color_casilla': ''}
                      for x in range(15)for y in range(15)}
    for color,  casillas in colores.items():
        for casilla in casillas:
            window.Element(casilla).Update(button_color=('black', color))
            matriz_tablero[casilla]['color_casilla'] = color
    return matriz_tablero
