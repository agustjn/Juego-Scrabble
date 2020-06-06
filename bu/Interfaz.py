import PySimpleGUI as sg
import random


def InterfazAtril(letras_jugador):
    letras = [[sg.Button(letras_jugador[x], key=str(x), size=(5, 3))]
              for x in range(7)]
    botones_especiales = [[sg.Button('Cambiar Fichas')],
                          [sg.Button('Fin De Turno')]]
    layout = [[sg.Column(letras)],
              [sg.Column(botones_especiales)]]
    window = sg.Window('Atril').Layout(layout)
    return window


def MenuPrincipal():
    menu = [[sg.Button('Iniciar'),
             sg.Button('Cargar Partida'),
             sg.Button('Salir')]]
    window = sg.Window('Menu de juego').Layout(menu)
    event, values = window.Read()
    window.Close()
    return event


def Dificultad():
    dificultad = [[sg.Button('Facil', size=(10, 2)),
                  sg.Button('Medio', size=(10, 2)),
                  sg.Button('Dificil', size=(10, 2)),
                  sg.Button('Personalizado', size=(10, 2))]]
    window = sg.Window('Dificultad de juego').Layout(dificultad)
    event, values = window.Read()
    window.Close()
    return event


def MenuPersonalizado():
    niveles = ['Facil', 'Medio', 'Dificil']
    personalizado = [[sg.Text('Nivel'), sg.InputCombo(niveles, size=(10, 8),
                      key='Nivel')],
                     [sg.Text('Tiempo'), sg.InputText(size=(10, 8),
                      key='Tiempo')],
                     [sg.Button('Iniciar')]]
    window = sg.Window('Juego personalizado').Layout(personalizado)
    event, values = window.Read()
    return event, values

def InterfazReglas(nivel):
    if (nivel=='Facil'):
        texto='En este nivel se permite cualquier tipo de palabra'
    elif(nivel=='Medio'):
        texto='En este nivel se permiten unicamente verbos'
    elif(nivel=='Dificil'):
        texto='En este nivel solo se permiten'
    sg.Popup(nivel,texto)
