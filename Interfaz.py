import PySimpleGUI as sg
import random
from const import *


def InterfazAtril(letras_jugador):
    letras = [[sg.Button(letras_jugador[x], key=str(x), size=(5, 3))]
              for x in range(7)]
    botones_especiales = [[sg.Button('Cambiar Fichas', size=button_size)],
                          [sg.Button('Fin De Turno', size=button_size)]]
    layout = [[sg.Column(letras)],
              [sg.Column(botones_especiales)]]
    window = sg.Window('Atril',
                       margins=marg_size,
                       element_padding=padd_size,
                       font=font_size).Layout(layout)
    return window


def MenuPrincipal():
    menu = [[sg.Button('Iniciar',
                       size=(27, 2))],
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
    dificultad = [[sg.Button('Facil',
                             size=button_size),
                   sg.Button('Medio',
                             size=button_size)],
                  [sg.Button('Dificil',
                             size=button_size),
                   sg.Button('Personalizado',
                             size=button_size)]]
    window_elements = [[sg.Column(dificultad)],
                       [sg.Column([[sg.Button('Volver', size=button_size)]],
                                  justification='center')]]
    window = sg.Window('Dificultad de juego',
                       margins=marg_size,
                       element_padding=padd_size,
                       font=font_size).Layout(window_elements)
    event, values = window.Read()
    window.Close()
    return event


def MenuPersonalizado():
    niveles = ['Facil', 'Medio', 'Dificil']
    personalizado = [[sg.Text('Nivel',
                              size=text_size),
                      sg.Drop(niveles,
                              size=drop_size,
                              key='Nivel')],
                     [sg.Text('Tiempo',
                              size=text_size),
                      sg.InputText(size=input_size,
                                   key='Tiempo')]]
    window_elements = [[sg.Column(personalizado,
                                  justification='center')],
                       [sg.Column([[sg.Button('Iniciar', size=button_size)]],
                                  justification='center')]]
    window = sg.Window('Juego personalizado',
                       margins=marg_size,
                       element_padding=padd_size,
                       font=font_size).Layout(window_elements)
    event, values = window.Read()
    return event, values


def InterfazReglas(nivel):
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
