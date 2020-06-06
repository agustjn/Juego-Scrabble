import json
import time
import PySimpleGUI as sg
from ScoreControl import ScoreControl as sc
from ModuloAtril import *
from Tableros import *
from LoadGame import *
from Interfaz import *


def Tablero(window, matriz_tablero, nivel):
    puntos = sc(0)
    mano_jugador = []
    mano_cpu = []
    jugador = Atril(mano_jugador)
    cpu = Atril(mano_cpu)
    jugador.repartirFichas()
    cpu.repartirFichas()
    ActualizarFichas(window,jugador,cpu)
    while True:
        event, values = window.Read()
        if (event == 'TERMINAR') | (event == None):
            break;
        elif event == 'POSPONER':
            GuardarPartida(matriz_tablero, nivel)
            sg.Popup('Partida guardada en el archivo')
        elif event == 'TOP 10':
            sg.Popup('En Mantenimiento')
        elif event =='REGLAS':
            InterfazReglas(nivel)
        elif(('J' in event) & (len(event) == 2)):
            letra_turno = window.Element(event).GetText()
            event, values = window.Read()
            if len(event) != 2:
                matriz_tablero[event]['letra'] = letra_turno
                window.Element(event).Update(letra_turno)

        if event in matriz_tablero:
            puntos.multiplicar(matriz_tablero[event]['color_casilla'])
            print(puntos.get_puntos)


def Jugar(opcion):
    if opcion == 'Iniciar':
        nivel = Dificultad()
        if nivel == 'Facil':
            window, matriz_tablero, nivel = TableroFacil()
        elif nivel == 'Medio':
            window, matriz_tablero, nivel = TableroMedio()
        elif nivel == 'Dificil':
            window, matriz_tablero, nivel = TableroDificil()
        elif nivel == 'Personalizado':
            event, values = MenuPersonalizado()
            window, matriz_tablero, nivel = TableroPersonalizado(values['Nivel'])
        Tablero(window, matriz_tablero, nivel)
    elif opcion == 'Cargar Partida':
        window, matriz_tablero, nivel = CargarPartida()
        Tablero(window, matriz_tablero, nivel)


Jugar(MenuPrincipal())
