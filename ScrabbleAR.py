import json
import time
import PySimpleGUI as sg
from ScoreControl import ScoreControl as sc
from Modulo_Atril import *
from Tableros import *
from Load_Game import *
from Interfaces import *
from const import *
from VerificadorPalabra import *
from random import *
from Restricciones_Jugador import *
from Logica_CPU import *
#NOTA CAMBIAR LOS NOMBRES DE TODOS LOS MODULOS A MINISCULA MENOS EL PRINCIPAL SCRABBLE AR
def Turno():
    ''' Esta Funcion se encarga de escoger de manera aleatoria  que jugador va
        a empezar a jugar'''
    jugadores=['jugador','cpu']
    if (choice(jugadores)=='jugador'):
        return True,False
    else:
        return False,True
def Reiniciar_Listas(listas):# resetea las listas
    listas['pos_en_tablero']=[]
    listas['letras_en_tablero']=[]
    listas['pos_en_atril']=[]
    listas['casillas']=[]
    listas['puntos_por_letra']=[]
    return listas
def Actualizar_Puntos(objeto,player,casillas,puntos_por_letra,window):#Actualizador de puntos
    for i in range(len(casillas)):
        objeto.sumar(casillas[i],puntos_por_letra[i])
    if player =='jugador':
        window.Element('Puntos_jugador').Update(objeto.get_puntos())
    else:
        window.Element('Puntos_cpu').Update(objeto.get_puntos())

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

    listas= {'pos_en_tablero':[],'letras_en_tablero':[],'pos_en_atril':[],
             'casillas':[],'puntos_por_letra':[]}
    lista_de_posiciones_cpu=[]
    lista_palabra_cpu=[]
    casillas_cpu=[]
    #print(matriz_tablero)
    jugador = Atril(['H', 'O', 'L', 'A', 'U', 'B', 'E'],0)
    #jugador = Atril(mano_jugador,0)
    cpu=Atril(['C','O','R','R','E','R','O'],0)
    #cpu = Atril(mano_cpu,0)
    #jugador.repartirFichas()
    #cpu.repartirFichas()
    print('MANO JUGADOR = ',jugador.getMano())
    print('MANO CPU = ',cpu.getMano())
    Actualizar_Atril_Jugador(window, jugador)
    Actualizar_Atril_Cpu(window, cpu)
    while True:
        if (jg)&(not cp):
            window.Element('Turno').Update('Jg')
            event, values = window.Read() # primer read para los botones y el atril del jugador
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
            elif event == 'Fin De Turno':
                if len(listas['pos_en_tablero'])!=0:
                    word = checkWord(listas['pos_en_tablero'], matriz_tablero)
                    if not verifyWord(word):
                        matriz_tablero=Palabra_Invalida(listas,matriz_tablero,
                                                        window)
                        sg.Popup('Palabra invalida pierdes el turno')
                    else:
                        Actualizar_Puntos(jugador,'jugador',listas['casillas'],
                                          listas['puntos_por_letra'],window)
                    listas=Reiniciar_Listas(listas)

                    print(word)
                    print(verifyWord(word))
                else:
                    sg.Popup('Finalizaste el turno del jugador sin colocar una ficha')
                jg=False
                cp=True
            elif event=='Cambiar Fichas':
                jugador.devolverFichas()
                Actualizar_Atril_Jugador(window, jugador)
                #print(Atril.bolsa_fichas)
                #print(Atril.letras_bolsa)
            elif 'Jugador' in event:
                letra_turno = window.Element(event).GetText()
                key_letra = event
                print('LETRA TURNO = ',letra_turno)
                event, values = window.Read() # segundo read para colocar la letra en la casilla del tablero
                print('EVENTO = ',event)
                if event not in ('Cambiar Fichas','Fin De Turno','TOP 10','POSPONER','REGLAS','TERMINAR',None):
                    print('ENTRE!!!!!!!!!',event)
                    if len(listas['pos_en_tablero'])==0:# primera letra en el tablero
                        listas,matriz_tablero=Primera_Letra(listas,event,letra_turno,
                        matriz_tablero,window,key_letra,jugador)
                    elif len(listas['pos_en_tablero'])==1: # segunda letra en el tablero
                        listas,matriz_tablero,orientacion=Segunda_Letra(listas,
                        event,letra_turno,matriz_tablero,window,key_letra,jugador)
                    else:# siguientes letras a colocar segun la orientacion
                        if orientacion == 'Horizontal': #Letras a poner en horizontal
                            listas,matriz_tablero=Letras_Horizontal(listas,event,
                            letra_turno,matriz_tablero,window,key_letra,jugador)
                        else:#Letras a poner en vertical
                            listas,matriz_tablero=Letras_Vertical(listas,event,
                            letra_turno,matriz_tablero,window,key_letra,jugador)
                    print(listas['pos_en_tablero'])
                    print(listas['pos_en_atril'])
                    print(listas['letras_en_tablero'])
                    print(listas['casillas'])
                    print(listas['puntos_por_letra'])
        else: # turno del CPU todavia con errores
            window.Element('Turno').Update('CPU')
            palabra_cpu=Validar_Palabra_CPU(cpu.getMano(),nivel)
            print('PALABRA CPU =',palabra_cpu)
            if palabra_cpu=='':#esto quiere decir que la palabra es invalida
                if cont==1: #esto quiere decir que la maquina paso un turno para cambiar fichas
                    cpu.devolverFichas()
                    Actualizar_Atril_Cpu(window,cpu)
                elif cont>=3:
                    sg.Popup('La Cpu ha perdido paso 3 veces seguidas el turno')
                cont+=1
                print('No tengo palabra valida')
            else:
                cont=0
                if window.Element((7,7)).GetText()=='':
                    casilla_cpu=(7,7)
                else:
                    casilla_cpu=choice(list(matriz_tablero.keys()))
                linea=Evaluar_Posicion(window,casilla_cpu,palabra_cpu,
                                       matriz_tablero)
                print('Casilla random ',casilla_cpu)
                while linea == 'No Valido':
                    print(linea)
                    casilla_cpu=choice(list(matriz_tablero.keys()))
                    print(casilla_cpu)
                    linea=Evaluar_Posicion(window,casilla_cpu,palabra_cpu,
                                           matriz_tablero)
                if linea == 'Horizontal':
                    matriz_tablero=Colocar_Letras(window,lista_palabra_cpu,
                                                 casilla_cpu,'Horizontal',
                                                 palabra_cpu,matriz_tablero,
                                                 cpu,listas)
                else:
                    matriz_tablero=Colocar_Letras(window,lista_palabra_cpu,
                                                 casilla_cpu,'Vertical',
                                                 palabra_cpu,matriz_tablero,
                                                 cpu,listas)
                print('Palabra valida encontrada = ',palabra_cpu)
                print(listas['pos_en_tablero'])
                print(listas['pos_en_atril'])
                print(listas['letras_en_tablero'])
                print(listas['casillas'])
                print(listas['puntos_por_letra'])
                Actualizar_Puntos(cpu,'cpu',listas['casillas'],
                                  listas['puntos_por_letra'],window)
            listas=Reiniciar_Listas(listas)
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
