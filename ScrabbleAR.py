import PySimpleGUI as sg
import json
import time
from Tableros import TableroFacil, TableroMedio, TableroDificil, TableroPersonalizado
from ScoreControl import ScoreControl as sc
from LoadGame import CargarPartida,GuardarPartida
from Atril import AtrilP
from Interfaz import InterfazAtril,MenuPrincipal,Dificultad,MenuPersonalizado


def Tablero(window,matriz_tablero,nivel):
    puntos=sc(0)
    #jugador=at(0)
    #letras=jugador.get_letras()
    bolsa_fichas={'A':11,'E':11,'O':8,'S':7,'I':6,'U':6,'N':5,'L':4,'R':4,'T':4,
	              'C':4,'D':4,'G':2,'M':3,'B':2,'P':2,'F':2,'H':2,'V':2,'Y':1,
	              'J':2,'K':1,'LL':1,'Ñ':1,'Q':1,'RR':1,'W':1,'X':1,'Z':1}
    letras_juego=[]
    for letra,cantidad in bolsa_fichas.items():
        if(letra not in letras_juego):
            letras_juego.append(letra)
    mano_jugador=[]
    jugador=AtrilP(mano_jugador,letras_juego)
    jugador.repartirFichas()
    print(jugador._mano_jugador)
    for i in range(7):
        window.Element(str(i)+'J').Update(jugador._mano_jugador[i])
    #print(jugador._bolsa_fichas)
    #windowAtril=InterfazAtril(jugador._mano_jugador)
    while True:# estructura para manejar el tablero termina al precionar terminar
        '''while True: # estructura para leer las letras del atril
            eventAtril,valuesAtril=windowAtril.Read()
            if(eventAtril=='Fin De Turno'):
                windowAtril.Close()
                break;
            elif (int(eventAtril)>=0) & (int(eventAtril)<=6):
                l=windowAtril.Element(eventAtril).GetText()
                event,values=window.Read()
                window.Element(event).Update(l)'''
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
