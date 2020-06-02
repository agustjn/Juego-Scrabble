import PySimpleGUI as sg
import json
import time
from Tableros import TableroFacil, TableroMedio, TableroDificil, TableroPersonalizado
from ScoreControl import ScoreControl as sc
from LoadGame import CargarPartida,GuardarPartida
from Atril import AtrilP
from Interfaz import InterfazAtril

def MenuPrincipal():
    menu = [[sg.Button("Iniciar"), sg.Button("Cargar Partida"), sg.Button("Salir")]
    ]
    window=sg.Window("Menu de juego").Layout(menu)
    event,values=window.Read()
    window.Close()
    return event

def Dificultad():
    dificultad = [[sg.Button('Facil', size=(10, 2))]+ [sg.Button('Medio', size=(10, 2))]+ [sg.Button('Dificil', size=(10, 2))]+
                  [sg.Button('Personalizado', size=(10, 2))]
    ]
    window=sg.Window("Dificultad de juego").Layout(dificultad)
    nivel,values=window.Read()
    window.Close()
    return nivel

def MenuPersonalizado():
    niveles=['Facil', 'Medio', 'Dificil']
    personalizado = [[sg.Text("Nivel"),sg.InputCombo(niveles, size = (10, 8), key='Nivel')],
                     [sg.Text("Tiempo"),sg.InputText(size = (10, 8), key='Tiempo')],
                     [sg.Button('Iniciar')]

    ]
    window=sg.Window("Juego personalizado").Layout(personalizado)
    event, values=window.Read()
    return event, values

def Tablero(window,matriz_tablero,nivel):
    puntos=sc(0)
    #jugador=at(0)
    #letras=jugador.get_letras()
    bolsa_fichas={'A':9, 'B':8, 'C':5, 'D':4, 'E':7, 'F':6, 'G':5, 'H':4, 'I':3,
			'J':4,'K':3, 'L':4, 'LL':1, 'M':2, 'N':1, 'Ñ':2, 'O':4, 'P':4,
			'Q':4, 'R':3, 'RR':3, 'S':3, 'T':2, 'U':2, 'V':2, 'W':2, 'X':1,
			'Y':1, 'Z':1}
    letras_juego=[]
    for letra,cantidad in bolsa_fichas.items():
        if(letra not in letras_juego):
            letras_juego.append(letra)
    mano_jugador=[]
    jugador=AtrilP(mano_jugador,letras_juego)
    jugador.repartirFichas()
    print(jugador._mano_jugador)
    #print(jugador._bolsa_fichas)
    windowAtril=InterfazAtril(jugador._mano_jugador)
    while True:# estructura para manejar el tablero termina al precionar terminar
        while True: # estructura para leer las letras del atril
            eventAtril,valuesAtril=windowAtril.Read()
            if(eventAtril=='Fin De Turno'):
                windowAtril.Close()
                break;
            elif (int(eventAtril)>=0) & (int(eventAtril)<=6):
                l=windowAtril.Element(eventAtril).GetText()
                event,values=window.Read()
                window.Element(event).Update(l)
        event,values=window.Read()
        if event in (None, 'Terminar'):
            break;
        if (event == 'Guardar Partida'):
            GuardarPartida(matriz_tablero,nivel)
            sg.Popup('Partida Guardada en el archivo')
        if event in matriz_tablero:
            puntos.multiplicar(matriz_tablero[event]['color_casilla'])
            print(puntos.get_puntos)

def Jugar(opcion_menu):
    if(opcion_menu == 'Iniciar'):
        nivel=Dificultad()
        if (nivel=='Facil'):
            window, matriz_tablero, nivel=TableroFacil()
        elif(nivel=='Medio'):
            window, matriz_tablero, nivel=TableroMedio()
        elif(nivel=='Dificil'):
            window, matriz_tablero, nivel=TableroDificil()
        elif(nivel=='Personalizado'):
            event, values=MenuPersonalizado()
            window, matriz_tablero, nivel=TableroPersonalizado(values['Nivel'])
        Tablero(window, matriz_tablero, nivel)
    elif (opcion_menu == 'Cargar Partida'):
        window, matriz_tablero, nivel=CargarPartida()
        Tablero(window, matriz_tablero, nivel)

Jugar(MenuPrincipal())
