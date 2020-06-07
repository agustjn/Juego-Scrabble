import json
import time
import PySimpleGUI as sg
from ScoreControl import ScoreControl as sc
from ModuloAtril import *
from Tableros import *
from LoadGame import *
from Interfaz import *
import VerificadorPalabra as verif


def Tablero(window, matriz_tablero, nivel):
    puntos = sc(0)
    mano_jugador = []
    mano_cpu = []
    cont=0
    #jugador = Atril(mano_jugador)
    lista_de_posiciones=[]
    jugador=Atril(['H','O','L','A','U','B','E'])
    cpu = Atril(mano_cpu)
    jugador.repartirFichas()
    cpu.repartirFichas()
    ActualizarFichas(window,jugador,cpu)
    while True:
        event, values = window.Read()
        if (event == 'TERMINAR') | (event == None):
            Cargar_TopDiez({'puntaje': puntos.get_puntos,
                            'fecha': time.strftime('%d/%m/%Y'),
                            'nivel': nivel})
        elif event == 'POSPONER':
            GuardarPartida(matriz_tablero, nivel)
            sg.Popup('Partida guardada en el archivo')
        elif event == 'TOP 10':
            Ver_TopDiez()
        elif event =='REGLAS':
            InterfazReglas(nivel)
        elif(('J' in event) & (len(event) == 2)):
            letra_turno = window.Element(event).GetText()
            event, values = window.Read()
            if len(event) != 2:
                #casilla_actual=event
                #print(casilla_actual)
                print(len(lista_de_posiciones))
                if(len(lista_de_posiciones)==0):
                    lista_de_posiciones.append(event)
                    cont+=1
                    matriz_tablero[event]['letra'] = letra_turno
                    window.Element(event).Update(letra_turno)
                else:
                    columna=int(lista_de_posiciones[-1].split(',')[0])
                    print('columna = ',columna)
                    fila=int(lista_de_posiciones[-1].split(',')[1])
                    print('fila = ',fila)
                    if cont==2:
                        orientacion=verif.checkOrientation(lista_de_posiciones)
                        cont+=1
                    elif cont==1:
                        if ((int(event.split(',')[0])==columna+1)&(int(event.split(',')[1])==fila))|((int(event.split(',')[0])==columna)&(int(event.split(',')[1])==fila+1)) :#|(int(event.split(',')[1])==fila+1):
                            matriz_tablero[event]['letra'] = letra_turno
                            window.Element(event).Update(letra_turno)
                            lista_de_posiciones.append(event)
                            cont+=1
                        else:
                            sg.Popup('Casilla Invalida')
                    else:
                        print('entre en cont = 3')
                        if (orientacion=='Horizontal'):
                            print(orientacion)
                            if(int(event.split(',')[0])==columna+1)&(int(event.split(',')[1])==fila):
                                matriz_tablero[event]['letra'] = letra_turno
                                window.Element(event).Update(letra_turno)
                                lista_de_posiciones.append(event)
                            else:
                                sg.Popup('La casilla valida es '+str(columna+1)+','+str(fila))
                        elif(orientacion=='Vertical'):
                            print(orientacion)
                            if(int(event.split(',')[0])==columna)&(int(event.split(',')[1])==fila+1):
                                matriz_tablero[event]['letra'] = letra_turno
                                window.Element(event).Update(letra_turno)
                                lista_de_posiciones.append(event)
                            else:
                                sg.Popup('La casilla valida es '+str(columna)+','+str(fila+1))
                print(lista_de_posiciones)
        if event == 'Fin De Turno':
            orientacion=verif.checkOrientation(lista_de_posiciones)
            if (verif.checkOrientation(lista_de_posiciones) == 'Vertical'):
                lista_de_posiciones.sort(key=lambda tup: tup.split(',')[0])  #Ordeno las posiciones por columna
                print('La palabra es en sentido vertical')
            else:
                lista_de_posiciones.sort(key=lambda tup: tup.split(',')[1])
                print('La palabra es en sentido horizontal')
            word=verif.checkWord(lista_de_posiciones,matriz_tablero)
            print(word)
            verif.verifyWord(word)
            lista_de_posiciones=[]


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
