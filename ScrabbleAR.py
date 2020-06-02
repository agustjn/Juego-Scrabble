import PySimpleGUI as sg
import json
import time
from Tableros import TableroFacil, TableroMedio, TableroDificil, TableroPersonalizado
from ScoreControl import ScoreControl as sc
from LoadGame import CargarPartida,GuardarPartida
from ModuloAtril import Atril
from Interfaz import InterfazAtril,MenuPrincipal,Dificultad,MenuPersonalizado


def Tablero(window,matriz_tablero,nivel):
    puntos=sc(0)
    mano_jugador=[]
    mano_cpu=[]
    jugador=Atril(mano_jugador)
    cpu=Atril(mano_cpu)
    jugador.repartirFichas()
    print(jugador.getMano())
    #jugador.devolverFichas()
    #print(jugador.getMano())
    #print('Fichas al jugador',AtrilP.bolsa_fichas)
    cpu.repartirFichas()
    #print('Fichas al cpu',AtrilP.bolsa_fichas)
    #print(jugador.getMano())
    for i in range(7):
        window.Element(str(i)+'J').Update(jugador.getMano()[i])
    for i in range(7):
        window.Element(str(i)+'C').Update(cpu.getMano()[i])
    #print(jugador._bolsa_fichas)
    #windowAtril=InterfazAtril(jugador._mano_jugador)
    while True:# estructura para manejar el tablero termina al precionar terminar
        event,values=window.Read()
        if ('J' in event) &(len(event)==2):
            letra_turno=window.Element(event).GetText()
            event,values=window.Read()
            if(len(event)!=2):
                matriz_tablero[event]['letra']=letra_turno
                window.Element(event).Update(letra_turno)
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
