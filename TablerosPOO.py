import json
import PySimpleGUI as sg
from const import *
class Tableros:
    '''
    Segun la dificultad, devuelve el diccionario de colores y posiciones
    '''
    def cargarColor(self,difficult):
        arch = open('matriz_colores.json','r')
        matriz_colores=json.load(arch)
        print(matriz_colores['colores_facil'].items())
        print('.....')
        if difficult == 'Facil':
            matriz=matriz_colores['colores_facil'].items()
        if difficult == 'Medio':
            matriz=matriz_colores['colores_medio'].items()
        if difficult == 'Dificil':
            matriz=matriz_colores['colores_Dificil'].items()
        arch.close()
        return matriz

    '''
    Carga la matriz segun su color, la recorre asignando el color y las letras vacias
    a cada boton del tablero segun su dificultad
    '''
    def cargarMatriz(self,difficult,window):
            matriz_tablero = {str(x)+','+str(y): {'letra': '',  'color_casilla': ''} for x in range(15)for y in range(15)}
            colores=self.cargarColor(difficult)
            for color,  casillas in colores:
                for casilla in casillas:
                    window.Element(casilla).Update(button_color=('black', color))
                    matriz_tablero[casilla]['color_casilla'] = color




    def __init__(self,difficult):     #'{},{}'.format(x, y),
        '''PRIVADO'''
        tablero = [[sg.Button(size=board_button_size,button_color=('black',  'grey'),key=str(x)+','+str(y),pad=board_padd_size)for x in range(15)]for y in range(15)]
        '''PRIVADO'''
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
        puntos_cpu = [[sg.Text('Puntaje CPU',size=(13, 1),justification='center')],
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
        window = sg.Window('Tablero de juego ',
                       margins=marg_size,
                       element_padding=padd_size,
                       font=font_size,
                       location=window_location).Layout(layout).Finalize()
        self.cargarMatriz(difficult,window)

Tableros('Dificil')
while True:
    int(input())
