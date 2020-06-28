import PySimpleGUI as sg
import random
from const import *

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
    dificultad = [[sg.Button('Facil',
                             size=button_size),
                   sg.Button('Medio',
                             size=button_size)],
                  [sg.Button('Dificil',
                             size=button_size),
                   sg.Button('Personalizado',
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
    niveles = ['Facil', 'Medio', 'Dificil']
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
    if (nivel == 'Facil'):
        texto = 'En este nivel se permite cualquier tipo de palabra'
    elif(nivel == 'Medio'):
        texto = 'En este nivel se permiten unicamente verbos'
    elif(nivel == 'Dificil'):
        texto = 'En este nivel solo se permiten'
    sg.Popup(nivel, texto,
             title='ScrabbleAR',
             font=font_size,
             custom_text='Volver')
