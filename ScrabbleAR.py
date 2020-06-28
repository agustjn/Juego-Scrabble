import json
import time
import PySimpleGUI as sg
from ScoreControl import ScoreControl as sc
from Modulo_Atril import *
from Tableros import *
from Load_Game import *
from Interfaces import *
from const import *
import VerificadorPalabra as verif
from random import *
from Restricciones_Jugador import *
from Logica_CPU import *

def Turno():
    jugadores=['jugador','cpu']
    if (choice(jugadores)=='jugador'):
        return True,False
    else:
        return False,True

def Comenzar_Juego(window, matriz_tablero, nivel,partida):
    ''' Esta Funcion es en donde se ejecutan todas las operaciones que permiten
        la interaccion con el tablero y las manos de los jugadores entre otras
        cosas'''

    puntos = sc(0)
    mano_jugador = []
    mano_cpu = []
    cont = 0
    jg=True
    cp=False
    #jg,cp=Turno()
    #print('Turno jugador = ',jg,' Turno cpu = ',cp)
    # jugador = Atril(mano_jugador)
    lista_de_posiciones = []
    lista_de_posiciones_cpu=[]
    lista_palabra_cpu=[]
    casillas_invalidas=[]
    casillas_cpu=[]
    #print(matriz_tablero)
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
            elif 'Jugador' in event: #(len(event) == 2):
                letra_turno = window.Element(event).GetText()
                print('LETRA TURNO = ',letra_turno)
                event, values = window.Read()
                print('EVENTO = ',event , 'LEN = ',len(event))
                if 'Jugador' not in event:
                    # casilla_actual=event
                    # print(casilla_actual)
                    #print(len(lista_de_posiciones))
                    if(len(lista_de_posiciones) == 0):
                        lista_de_posiciones,cont,matriz_tablero=Primera_Letra(lista_de_posiciones,cont,event,letra_turno,matriz_tablero,window)
                        #casillas_cpu.append(int(event.split()[0])+1)
                        casillas_invalidas.append(event)
                        columna = event[0]
                        fila = event[1]
                        print('columna = ', columna,' fila = ', fila)
                    else:
                        if cont==1:
                            lista_de_posiciones,cont,matriz_tablero=Segunda_Letra(lista_de_posiciones,cont,event,columna,fila,letra_turno,matriz_tablero,window)
                        elif cont == 2:
                            columna = lista_de_posiciones[-1][0]
                            fila = lista_de_posiciones[-1][1]
                            print('columna = ', columna,' fila = ', fila)
                            orientacion = verif.checkOrientation(lista_de_posiciones)
                            print(orientacion)
                            if (orientacion == 'Horizontal'):
                                lista_de_posiciones,matriz_tablero=Letras_Horizontal(lista_de_posiciones,event,columna,fila,letra_turno,matriz_tablero,window)
                            elif(orientacion == 'Vertical'):
                                lista_de_posiciones,matriz_tablero=Letras_Vertical(lista_de_posiciones,event,columna,fila,letra_turno,matriz_tablero,window)

                    print(lista_de_posiciones)
            if event == 'Fin De Turno':
                word = verif.checkWord(lista_de_posiciones, matriz_tablero)
                print(word)
                verif.verifyWord(word)
                lista_de_posiciones = []
                print(lista_de_posiciones)
                cont=0
                jg=False
                cp=True
            if event in matriz_tablero:
                puntos.multiplicar(matriz_tablero[event]['color_casilla'])
                print(puntos.get_puntos)
        else:
            window.Element('Turno').Update('CPU')
            mano_cpu=['C','O','R','R','E','R','o']
            casilla_cpu=choice(list(matriz_tablero.keys()))
            es_valida=False
            print('Casilla random ',casilla_cpu)
            palabra_cpu=verif.Validar_Palabra_CPU(mano_cpu,nivel)
            while not es_valida:
                x=casilla_cpu[0]
                y=casilla_cpu[1]
                print('Texto boton = ',window.Element((0,0)).GetText())
                if palabra_cpu!='':
                    linea=Evaluar_Posiciones(window,x,y,0,palabra_cpu,matriz_tablero)
                    print(linea)
                    if linea == 'Horizontal':
                        Colocar_Letras(window,lista_palabra_cpu,casilla_cpu[0],casilla_cpu[1],0,palabra_cpu)
                        es_valida=True
                    else:
                        linea=Evaluar_Posiciones(window,x,y,1,palabra_cpu,matriz_tablero)
                        if linea == 'Vertical':
                            Colocar_Letras(window,lista_palabra_cpu,casilla_cpu[0],casilla_cpu[1],1,palabra_cpu)
                            es_valida=True
                        else:
                            print('La letra no se puede colocar')
                            casilla_cpu=choice(list(matriz_tablero.keys()))
                    '''
                    if Evaluar_Posiciones(window,x,y,0,palabra_cpu,matriz_tablero)=='Horizontal':
                        Colocar_Letras(window,lista_palabra_cpu,casilla_cpu[0],casilla_cpu[1],0,palabra_cpu)
                        es_valida=True
                    elif Evaluar_Posiciones(window,x,y,1,palabra_cpu,matriz_tablero)=='Vertical':
                        Colocar_Letras(window,lista_palabra_cpu,casilla_cpu[0],casilla_cpu[1],1,palabra_cpu)
                        es_valida=True
                    else:
                        print('La letra no se puede colocar')
                        casilla_cpu=choice(list(matriz_tablero.keys()))'''
                '''if (matriz_tablero[(7,7)]['letra']==''):
                    col=5
                    fila=7
                else:
                    print('algo')
                lista_palabra_cpu=[]
                for letra in palabra_cpu:
                    lista_palabra_cpu.append(letra)
                print(lista_palabra_cpu)
                #lista_palabra_cpu=[]
                for i in range(len(lista_palabra_cpu)):
                    window.Element((col,fila)).Update(lista_palabra_cpu[i])
                    col+=1'''
            else:
                print('No tengo palabra')
            print('Palabra valida encontrada = ',palabra_cpu)
            #algo2=input('Este es el turno del cpu Ingrese algo para confirmar')
            jg=True
            cp=False

def Jugar(opcion):
    ''' Esta funcion trata de la configuracion del juego en donde se presentan
        2 menus el primero el cual contiene el boton Iniciar, CargarPartida y
        Salir y el segundo el cual se despliega al presionar el boton Iniciar
        que permite al usuario escoger que nivel de juego desea o si quiere
        configurar otros aspectos del juego'''
    if opcion == 'Iniciar':
        nivel = Dificultad()
        ok=True
        if nivel == 'Facil':
            window, matriz_tablero, nivel = TableroFacil()
        elif nivel == 'Medio':
            window, matriz_tablero, nivel = TableroMedio()
        elif nivel == 'Dificil':
            window, matriz_tablero, nivel = TableroDificil()
        elif nivel == 'Personalizado':
            event, values = MenuPersonalizado()
            if event!=None:
                window, matriz_tablero, nivel = TableroPersonalizado(values['Nivel'])
            else:
                ok=False
        elif nivel== 'Volver':
            Jugar(MenuPrincipal())
        if ((nivel!='Volver')&(nivel!=None)&(ok)):
            Comenzar_Juego(window, matriz_tablero, nivel,False)
    elif opcion == 'Cargar Partida':
        window, matriz_tablero, nivel,partida = CargarPartida()
        if (partida):
            Comenzar_Juego(window, matriz_tablero, nivel,partida)


Jugar(MenuPrincipal())
