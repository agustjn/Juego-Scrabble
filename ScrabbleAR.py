import json
import time
import PySimpleGUI as sg
from ScoreControl import ScoreControl as sc
from ModuloAtril import *
from Tableros import *
from LoadGame import *
from Interfaz import *
from const import *
import VerificadorPalabra as verif
from random import *
from Procesos import *

def Turno():
    jugadores=['jugador','cpu']
    if (choice(jugadores)=='jugador'):
        return True,False
    else:
        return False,True

def Tablero(window, matriz_tablero, nivel):
    puntos = sc(0)
    mano_jugador = []
    mano_cpu = []
    cont = 0
    jg,cp=Turno()
    print('Turno jugador = ',jg,' Turno cpu = ',cp)
    # jugador = Atril(mano_jugador)
    lista_de_posiciones = []
    lista_de_posiciones_cpu=[]
    jugador = Atril(['H', 'O', 'L', 'A', 'U', 'B', 'E'])
    cpu = Atril(mano_cpu)
    jugador.repartirFichas()
    cpu.repartirFichas()
    ActualizarFichas(window, jugador, cpu)
    while True:
        if (jg)&(not cp):
            window.Element('Turno').Update('Jg')
            event, values = window.Read()
            if event in (None, 'TERMINAR'):
                Cargar_TopDiez({'puntaje': puntos.get_puntos,
                                'fecha': time.strftime('%d/%m/%Y'),
                                'nivel': nivel})
                break
            elif event == 'POSPONER':
                GuardarPartida(matriz_tablero, nivel)
                sg.Popup('Partida guardada en el archivo')
            elif event == 'TOP 10':
                Ver_TopDiez()
            elif event == 'REGLAS':
                InterfazReglas(nivel)
            elif(('J' in event) & (len(event) == 2)):
                letra_turno = window.Element(event).GetText()
                print('LETRA TURNO = ',letra_turno)
                event, values = window.Read()
                print('EVENTO = ',event , 'LEN = ',len(event))
                if len(event) >= 3:
                    # casilla_actual=event
                    # print(casilla_actual)
                    #print(len(lista_de_posiciones))
                    if(len(lista_de_posiciones) == 0):
                        lista_de_posiciones,cont,matriz_tablero=Primera_Letra(lista_de_posiciones,cont,event,letra_turno,matriz_tablero,window)
                        columna = int(event.split(',')[0])
                        fila = int(event.split(',')[1])
                        print('columna = ', columna,' fila = ', fila)
                    else:
                        if cont==1:
                            lista_de_posiciones,cont,matriz_tablero=Segunda_Letra(lista_de_posiciones,cont,event,columna,fila,letra_turno,matriz_tablero,window)
                        elif cont == 2:
                            columna = int(lista_de_posiciones[-1].split(',')[0])
                            fila = int(lista_de_posiciones[-1].split(',')[1])
                            print('columna = ', columna,' fila = ', fila)
                            orientacion = verif.checkOrientation(lista_de_posiciones)
                            print(orientacion)
                            if (orientacion == 'Horizontal'):
                                lista_de_posiciones,matriz_tablero=Letras_Horizontal(lista_de_posiciones,event,columna,fila,letra_turno,matriz_tablero,window)
                            elif(orientacion == 'Vertical'):
                                lista_de_posiciones,matriz_tablero=Letras_Vertical(lista_de_posiciones,event,columna,fila,letra_turno,matriz_tablero,window)

                    print(lista_de_posiciones)
            if event == 'Fin De Turno':
                orientacion = verif.checkOrientation(lista_de_posiciones)
                if (verif.checkOrientation(lista_de_posiciones) == 'Vertical'):
                    # Ordeno las posiciones por columna
                    lista_de_posiciones.sort(key=lambda tup: tup.split(',')[0])
                    print('La palabra es en sentido vertical')
                else:
                    lista_de_posiciones.sort(key=lambda tup: tup.split(',')[1])
                    print('La palabra es en sentido horizontal')
                word = verif.checkWord(lista_de_posiciones, matriz_tablero)
                print(word)
                verif.verifyWord(word)
                lista_de_posiciones = []
                jg=False
                cp=True
            if event in matriz_tablero:
                puntos.multiplicar(matriz_tablero[event]['color_casilla'])
                print(puntos.get_puntos)
        else:
            window.Element('Turno').Update('CPU')
            mano_cpu=['C','O','R','R','E','R','o']

            palabra_cpu=verif.Validar_Palabra_CPU(mano_cpu,nivel)
            if palabra_cpu!='':
                casilla='0,0'
                col='5'
                fila='7'
                lista_palabra_cpu=[]
                for letra in palabra_cpu:
                    lista_palabra_cpu.append(letra)
                print(lista_palabra_cpu)
            for i in range(len(lista_palabra_cpu)):
                window.Element(col+','+fila).Update(lista_palabra_cpu[i])
                colint=int(col)+1
                col=str(colint)
                print('algo')
            print('Palabra valida encontrada = ',palabra_cpu)
            #algo2=input('Este es el turno del cpu Ingrese algo para confirmar')
            jg=True
            cp=False

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
        elif nivel== 'Volver':
            Jugar(MenuPrincipal())
        if nivel!='Volver':
            Tablero(window, matriz_tablero, nivel)
    elif opcion == 'Cargar Partida':
        window, matriz_tablero, nivel = CargarPartida()
        Tablero(window, matriz_tablero, nivel)


Jugar(MenuPrincipal())
