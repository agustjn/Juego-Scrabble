import PySimpleGUI as sg
from const import *

colores_Facil = {'yellow':   ['1,1', '7,0', '13,1', '0,7', '7,7', '14,7',
                              '1,13', '7,14', '13,13'],
                 'green':    ['0,0', '14,0', '0,14', '14,14', '6,3', '7,4',
                              '8,3', '3,6', '4,7', '3,8', '11,6', '10,7',
                              '11,8', '6,11', '7,12', '8,11'],
                 'blue':     ['2,4', '4,1', '10,1', '12,4', '6,6', '6,8',
                              '8,6', '8,8', '2,10', '3,13', '12,10', '10,13'],
                 'red':      ['3,3', '7,3', '11,3', '2,7', '12,7', '3,11',
                              '7,11', '11,11']}
colores_Medio = {'yellow':   ['0,0', '4,4', '7,7', '4,10', '0,14', '10,4',
                              '14,0', '10,10', '14,14', '2,4', '2,10', '4,12',
                              '10,12', '12,4', '12,10', '4,2', '10,2'],
                 'green':    ['2,2', '6,6', '6,8', '2,12', '8,6', '12,2',
                              '8,8', '12,12', '0,4', '0,10', '4,14', '10,14',
                              '14,4', '14,10', '4,0', '10,0'],
                 'blue':     ['7,1', '7,5', '7,9', '7,13', '9,7', '13,7',
                              '5,7', '1,7'],
                 'red':      ['7,3', '7,11', '11,7', '3,7', '2,6', '2,8',
                              '6,12', '8,12', '12,6', '12,8', '6,2', '8,2']}
colores_Dificil = {'yellow': ['5,0', '11,4', '6,6', '0,7', '1,7', '13,7',
                              '14,7', '8,8', '3,10', '9,14', ],
                   'green':  ['2,0', '12,0', '4,2', '10,2', '2,5', '13,5',
                              '4,7',  '5,7', '9,7', '10,7', '1,9', '13,9',
                              '4,12', '10,12', '2,14', '12,14', ],
                   'blue':   ['7,0', '9,0', '7,2', '3,4', '8,6', '3,7',
                              '6,7', '8,7', '11,7', '6,8', '11,10', '7,12',
                              '5,14', '7,14'],
                   'red':    ['1,1', '3,1', '11,1', '13,1', '3,3', '5,3',
                              '9,3', '11,3', '1,4', '13,4', '5,5', '7,5',
                              '9,5', '1,6', '13,6', '2,7', '7,7', '12,7',
                              '1,8', '13,8', '5,9', '7,9', '9,9', '1,10',
                              '13,10', '3,11', '5,11', '9,11', '11,11',
                              '1,13', '3,13', '11,13', '13,13']}


def TableroFacil():
    tablero = [[sg.Button('{},{}'.format(x, y),
                size=board_button_size,
                button_color=('black',  'grey'),
                key=str(x)+','+str(y),
                pad=board_padd_size)
                for x in range(15)]for y in range(15)]
    botones = [[sg.Button('POSPONER', size=button_size)],
               [sg.Button('TERMINAR', size=button_size)],
               [sg.Button('TOP 10', size=button_size)],
               [sg.Button('REGLAS', size=button_size)]]
    lista = []
    puntos_jugador = [[sg.Text('Puntaje Jugador',
                               size=(13, 1),
                               justification='center')],
                      [sg.Listbox(lista,
                                  key='Puntos_jugador',
                                  size=button_size,
                                  no_scrollbar=True,)]]
    puntos_cpu = [[sg.Text('Puntaje CPU',
                           size=(13, 1),
                           justification='center')],
                  [sg.Listbox(lista,
                              key='Puntos_cpu',
                              size=button_size,
                              no_scrollbar=True,)]]
    puntos_botones = [[sg.Column(puntos_jugador, justification='center')],
                      [sg.Column(puntos_cpu, justification='center')],
                      [sg.Column(botones, justification='center')]]
    letrasC = ['',  '',  '',  '',  '',  '',  '']
    letrasJ = ['',  '',  '',  '',  '',  '',  '']
    letras_jugador = [[sg.Button(letrasJ[x],  key=str(x)+'J',  size=(3, 1),
                       pad=board_padd_size)for x in range(7)]]
    letras_cpu = [[sg.Button(letrasC[x],  key=str(x)+'C',  size=(3, 1),
                   pad=board_padd_size)for x in range(7)]]
    botones_especiales = [[sg.Button('Cambiar Fichas',
                                     size=button_size),
                           sg.Button('Fin De Turno',
                                     size=button_size)]]
    atril_jugador = [[sg.Text('Atril Jugador',
                              size=text_atril_size,
                              justification='center')],
                     [sg.Column(letras_jugador,
                                justification='center')],
                     [sg.Column(botones_especiales,
                                justification='center')]]
    atril_cpu = [[sg.Text('Atril CPU',
                          size=text_atril_size,
                          justification='center')],
                 [sg.Column(letras_cpu,
                            justification='center')]]
    layout = [[sg.Column(tablero),
               sg.Column(puntos_botones)],
              [sg.Column(atril_jugador),
               sg.Column(atril_cpu)]]
    window = sg.Window('Tablero de juego nivel Facil',
                       margins=marg_size,
                       element_padding=padd_size,
                       font=font_size,
                       location=window_location).Layout(layout).Finalize()
    matriz_tablero = {str(x)+','+str(y): {'letra': '',  'color_casilla': ''}
                      for x in range(15)for y in range(15)}
    colores = colores_Facil
    for color,  casillas in colores.items():
        for casilla in casillas:
            window.Element(casilla).Update(button_color=('black', color))
            matriz_tablero[casilla]['color_casilla'] = color
    return window,  matriz_tablero,  'Facil'


def TableroMedio():
    tablero = [[sg.Button(size=(3, 1), button_color=('black', 'grey'),
                key=str(x)+','+str(y),
                pad=board_padd_size) for x in range(15)]for y in range(15)]
    botones = [[sg.Button('POSPONER', size=button_size)],
               [sg.Button('TERMINAR', size=button_size)],
               [sg.Button('TOP 10', size=button_size)],
               [sg.Button('REGLAS', size=button_size)]]
    lista = []
    puntos_jugador = [[sg.Text('Puntaje Jugador',
                               size=(13, 1),
                               justification='center')],
                      [sg.Listbox(lista,
                                  key='Puntos_jugador',
                                  size=button_size,
                                  no_scrollbar=True,)]]
    puntos_cpu = [[sg.Text('Puntaje CPU',
                           size=(13, 1),
                           justification='center')],
                  [sg.Listbox(lista,
                              key='Puntos_cpu',
                              size=button_size,
                              no_scrollbar=True,)]]
    puntos_botones = [[sg.Column(puntos_jugador, justification='center')],
                      [sg.Column(puntos_cpu, justification='center')],
                      [sg.Column(botones, justification='center')]]
    letrasC = ['',  '',  '',  '',  '',  '',  '']
    letrasJ = ['',  '',  '',  '',  '',  '',  '']
    letras_jugador = [[sg.Button(letrasJ[x],  key=str(x)+'J',  size=(3, 1),
                       pad=board_padd_size)for x in range(7)]]
    letras_cpu = [[sg.Button(letrasC[x],  key=str(x)+'C',  size=(3, 1),
                   pad=board_padd_size)for x in range(7)]]
    botones_especiales = [[sg.Button('Cambiar Fichas',
                                     size=button_size),
                           sg.Button('Fin De Turno',
                                     size=button_size)]]
    atril_jugador = [[sg.Text('Atril Jugador',
                              size=text_atril_size,
                              justification='center')],
                     [sg.Column(letras_jugador,
                                justification='center')],
                     [sg.Column(botones_especiales,
                                justification='center')]]
    atril_cpu = [[sg.Text('Atril CPU',
                          size=text_atril_size,
                          justification='center')],
                 [sg.Column(letras_cpu,
                            justification='center')]]
    layout = [[sg.Column(tablero),
               sg.Column(puntos_botones)],
              [sg.Column(atril_jugador),
               sg.Column(atril_cpu)]]
    window = sg.Window('Tablero de juego nivel Medio',
                       margins=marg_size,
                       element_padding=padd_size,
                       font=font_size,
                       location=window_location).Layout(layout).Finalize()
    matriz_tablero = {str(x)+','+str(y): {'letra': '',  'color_casilla': ''}
                      for x in range(15)for y in range(15)}
    colores = colores_Medio
    for color,  casillas in colores.items():
        for casilla in casillas:
            window.Element(casilla).Update(button_color=('black',  color))
            matriz_tablero[casilla]['color_casilla'] = color
    return window,  matriz_tablero,  'Medio'


def TableroDificil():
    tablero = [[sg.Button(size=(3, 1), button_color=('black', 'grey'),
                key=str(x)+','+str(y),
                pad=board_padd_size) for x in range(15)]for y in range(15)]
    botones = [[sg.Button('POSPONER', size=button_size)],
               [sg.Button('TERMINAR', size=button_size)],
               [sg.Button('TOP 10', size=button_size)],
               [sg.Button('REGLAS', size=button_size)]]
    lista = []
    puntos_jugador = [[sg.Text('Puntaje Jugador',
                               size=(13, 1),
                               justification='center')],
                      [sg.Listbox(lista,
                                  key='Puntos_jugador',
                                  size=button_size,
                                  no_scrollbar=True,)]]
    puntos_cpu = [[sg.Text('Puntaje CPU',
                           size=(13, 1),
                           justification='center')],
                  [sg.Listbox(lista,
                              key='Puntos_cpu',
                              size=button_size,
                              no_scrollbar=True,)]]
    puntos_botones = [[sg.Column(puntos_jugador, justification='center')],
                      [sg.Column(puntos_cpu, justification='center')],
                      [sg.Column(botones, justification='center')]]
    letrasC = ['',  '',  '',  '',  '',  '',  '']
    letrasJ = ['',  '',  '',  '',  '',  '',  '']
    letras_jugador = [[sg.Button(letrasJ[x],  key=str(x)+'J',  size=(3, 1),
                       pad=board_padd_size)for x in range(7)]]
    letras_cpu = [[sg.Button(letrasC[x],  key=str(x)+'C',  size=(3, 1),
                   pad=board_padd_size)for x in range(7)]]
    botones_especiales = [[sg.Button('Cambiar Fichas',
                                     size=button_size),
                           sg.Button('Fin De Turno',
                                     size=button_size)]]
    atril_jugador = [[sg.Text('Atril Jugador',
                              size=text_atril_size,
                              justification='center')],
                     [sg.Column(letras_jugador,
                                justification='center')],
                     [sg.Column(botones_especiales,
                                justification='center')]]
    atril_cpu = [[sg.Text('Atril CPU',
                          size=text_atril_size,
                          justification='center')],
                 [sg.Column(letras_cpu,
                            justification='center')]]
    layout = [[sg.Column(tablero),
               sg.Column(puntos_botones)],
              [sg.Column(atril_jugador),
               sg.Column(atril_cpu)]]
    window = sg.Window('Tablero de juego nivel Dificil',
                       margins=marg_size,
                       element_padding=padd_size,
                       font=font_size,
                       location=window_location).Layout(layout).Finalize()
    matriz_tablero = {str(x)+','+str(y): {'letra': '',  'color_casilla': ''}
                      for x in range(15)for y in range(15)}
    colores = colores_Dificil
    for color,  casillas in colores.items():
        for casilla in casillas:
            window.Element(casilla).Update(button_color=('black',  color))
            matriz_tablero[casilla]['color_casilla'] = color
    return window,  matriz_tablero,  'Dificil'


def TableroPersonalizado(nivel):
    if nivel == 'Facil':
        window, matriz_tablero, nivel = TableroFacil()
    elif nivel == 'Medio':
        window, matriz_tablero, nivel = TableroMedio()
    elif nivel == 'Dificil':
        window, matriz_tablero, nivel = TableroDificil()
    return window, matriz_tablero, nivel
