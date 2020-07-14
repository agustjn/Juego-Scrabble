import PySimpleGUI as sg
from const import *
#Elementos del Tablero
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

def Lista_Palabras():
    lista=[[sg.Text('HISTORIAL')],[sg.Listbox([],key='Palabras',size=(18,28))]
    ]
    return lista
def Puntos_Y_Botones(puntos_jugador,puntos_cpu,botones,turno_actual):
    ''' Esta Funcion consiste en colocar en colocar en columnas los distintos
        elementos que presenta el tablero '''
    puntos_botones = [[sg.Column(puntos_jugador)],
                      [sg.Column(puntos_cpu)],
                      [sg.Column(botones)],
                      [sg.Column(turno_actual)],
                      ]
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

def Layout(tablero,puntos_botones,atril_jugador,atril_cpu,lista):
    ''' Esta funcion consiste en juntar todos los elementos anteriores para
        formar el tablero y las demas funcionalidades del juego'''
    Tablero_Y_Atril=[[sg.Column(tablero)],
              [sg.Column(atril_jugador),
              sg.Column(atril_cpu)]]
    layout = [[sg.Column(lista),sg.Column(Tablero_Y_Atril),sg.Column(puntos_botones)],
              ]
    '''layout = [[sg.Column(tablero),
               sg.Column(puntos_botones)],
              [sg.Column(atril_jugador),
               sg.Column(atril_cpu)]]'''
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
    matriz_tablero = {(x,y): {'letra': '',  'color_casilla': 'grey'}
                      for x in range(15)for y in range(15)}
    for color,  casillas in colores.items():
        for casilla in casillas:
            window.Element(casilla).Update(button_color=('black',color))
            matriz_tablero[casilla]['color_casilla'] = color
    return matriz_tablero
#Fin de Elementos del Tablero

#Menus
def MenuPrincipal():
    ''' Esta funcion despliega el menu principal antes de iniciar el juego el
        cual permite escoger que se desea hacer entre iniciar una nueva partida
        o cargar una partida ya existente (solo se permite 1)'''
    menu = [[sg.Button('Iniciar',
                       size=(29, 2))],
            [sg.Button('Cargar Partida',
                       size=button_size),
             sg.Button('Salir',
                       size=button_size)]]
    window = sg.Window('Menu de juego',
                       margins=marg_size,
                       element_padding=padd_size,
                       font=font_size).Layout(menu)
    event, values = window.Read()
    window.Close()
    return event


def Dificultad():
    '''Esta funcion despliega la seleccion de nivel el cual desee el usuario
       que tambien cuenta con una configuracion personalizada que permite cambiar
       otros aspectos del juego'''

    dificultad = [[sg.Button('FACIL',
                             size=button_size),
                   sg.Button('MEDIO',
                             size=button_size)],
                  [sg.Button('DIFICIL',
                             size=button_size),
                   sg.Button('PERSONALIZADO',
                             size=button_size)]]
    window_elements = [[sg.Column(dificultad)],
                       [sg.Column([[sg.Button('Volver', size=button_size)]])]]
    window = sg.Window('Dificultad de juego',
                       margins=marg_size,
                       element_padding=padd_size,
                       font=font_size).Layout(window_elements)
    event, values = window.Read()
    window.Close()

    return event


def MenuPersonalizado():
    ''' Esta funcion despliega las configuraciones personalizadas permitidas
        para el usuario '''
    niveles = ['FACIL', 'MEDIO', 'DIFICIL']
    personalizado = [[sg.Text('Nivel',
                              size=text_size),
                      sg.Drop(niveles,
                              size=drop_size,
                              key='Nivel')],
                     [sg.Text('Tiempo',
                              size=text_size),
                      sg.InputText(size=input_size,
                                   key='Tiempo')],
                                   [sg.Button('Iniciar')]]
    window_elements = [[sg.Column(personalizado)]]
    window = sg.Window('Juego personalizado',
                       margins=marg_size,
                       element_padding=padd_size,
                       font=font_size).Layout(window_elements)
    event, values = window.Read()
    if event == None:
        window.Close()
    return event, values

def InterfazReglas(nivel):
    ''' Esta funcion despliega una ventana que muestra en pantalla las reglas
        segun el nivel que el usuario selecciono previamente'''
    if (nivel == 'FACIL'):
        texto = 'En este nivel se permite cualquier tipo de palabra'
    elif(nivel == 'MEDIO'):
        texto = 'En este nivel se permiten unicamente verbos'
    elif(nivel == 'DIFICIL'):
        texto = 'En este nivel solo se permiten'
    sg.Popup(nivel, texto,
             title='ScrabbleAR',
             font=font_size,
             custom_text='Volver')
#Fin de Menus

#Tableros FACIL MEDIO DIFICIL Y PERSONALIZADO
def TableroFacil():
    ''' Esta funcion consiste en generar el tablero de juego nivel facil con sus
        casillas predeterminadas'''
    tablero = Tablero()
    botones = Botones()
    puntos_jugador = Puntos_jugador()
    puntos_cpu = Puntos_cpu()
    turno_actual=Turno_actual()
    lista=Lista_Palabras()
    puntos_botones = Puntos_Y_Botones(puntos_jugador,puntos_cpu,botones,turno_actual)
    letras_jugador = Letras_jugador()
    letras_cpu = Letras_cpu()
    botones_turno = Botones_Turno()
    atril_jugador = Atril_jugador(letras_jugador,botones_turno)
    atril_cpu = Atril_cpu(letras_cpu)
    layout = Layout(tablero,puntos_botones,atril_jugador,atril_cpu,lista)
    window = Window(layout,'FACIL')
    matriz_tablero = Crear_Tablero(colores_Facil,window)
    return window,  matriz_tablero,  'FACIL'

def TableroMedio():
    ''' Esta funcion consiste en generar el tablero de juego nivel medio con sus
        casillas predeterminadas'''
    tablero = Tablero()
    botones = Botones()
    puntos_jugador = Puntos_jugador()
    puntos_cpu = Puntos_cpu()
    turno_actual=Turno_actual()
    lista=Lista_Palabras()
    puntos_botones = Puntos_Y_Botones(puntos_jugador,puntos_cpu,botones,turno_actual)
    letras_jugador = Letras_jugador()
    letras_cpu = Letras_cpu()
    botones_turno = Botones_Turno()
    atril_jugador = Atril_jugador(letras_jugador,botones_turno)
    atril_cpu = Atril_cpu(letras_cpu)
    layout = Layout(tablero,puntos_botones,atril_jugador,atril_cpu,lista)
    window = Window(layout,'MEDIO')
    matriz_tablero = Crear_Tablero(colores_Medio,window)
    return window,  matriz_tablero,  'MEDIO'

def TableroDificil():
    ''' Esta funcion consiste en generar el tablero de juego nivel dificil con sus
        casillas predeterminadas'''
    tablero = Tablero()
    botones = Botones()
    puntos_jugador = Puntos_jugador()
    puntos_cpu = Puntos_cpu()
    turno_actual=Turno_actual()
    lista=Lista_Palabras()
    puntos_botones = Puntos_Y_Botones(puntos_jugador,puntos_cpu,botones,turno_actual)
    letras_jugador = Letras_jugador()
    letras_cpu = Letras_cpu()
    botones_turno = Botones_Turno()
    atril_jugador = Atril_jugador(letras_jugador,botones_turno)
    atril_cpu = Atril_cpu(letras_cpu)
    layout = Layout(tablero,puntos_botones,atril_jugador,atril_cpu,lista)
    window = Window(layout,'DIFICIL')
    matriz_tablero = Crear_Tablero(colores_Dificil,window)
    return window,  matriz_tablero,  'DIFICIL'


def TableroPersonalizado(nivel):
    ''' Esta funcion consiste en generar el tablero de juego segun que
        configuracion especifica haya escogido el usuario retornando el tablero
        especifico con sus casillas predeterminadas'''
    if nivel == 'FACIL':
        window, matriz_tablero, nivel = TableroFacil()
    elif nivel == 'MEDIO':
        window, matriz_tablero, nivel = TableroMedio()
    elif nivel == 'DIFICIL':
        window, matriz_tablero, nivel = TableroDificil()
    return window, matriz_tablero, nivel
#Fin de Tableros
