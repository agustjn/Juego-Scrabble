import json
import time
import PySimpleGUI as sg
from const import *
from random import *
from modulo_interfaz import MenuPrincipal,Dificultad,MenuPersonalizado,InterfazReglas,TableroFacil,TableroMedio,TableroDificil,TableroPersonalizado
from modulo_atril import Atril,Actualizar_Atril_Jugador,Actualizar_Atril_Cpu,Actualizar_Puntos
from modulo_archivos import CargarPartida,GuardarPartida,Cargar_TopDiez,Ver_TopDiez
from modulo_verificacion import checkOrientation,checkWord,verifyWord,Validar_Palabra_CPU
from modulo_restricciones import Primera_Letra,Segunda_Letra,Letras_Horizontal,Letras_Vertical,Palabra_Invalida,Evaluar_Posicion,Colocar_Letras

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



def Inicio(window, matriz_tablero, nivel,partida):# esta funcion se encarga de configurar la partida antes de iniciar
    if not partida: # si se inicio una nueva partida entonces comienza con su configuracion predeterminada
        '''jugador=Atril([],0,nivel)
        cpu=Atril([],0,nivel)
        jugador.repartirFichas()
        cpu.repartirFichas()'''
        historial=[]
        jugador = Atril(['H', 'O', 'L', 'A', 'U', 'B', 'E'],0,nivel)
        cpu=Atril(['C','O','R','R','E','R','O'],0,nivel)
        #turno_jugador,turno_cpu=Turno()
        turno_jugador,turno_cpu=True,False
        listas= {'pos_en_tablero':[],'letras_en_tablero':[],'pos_en_atril':[],
                 'casillas':[],'puntos_por_letra':[]}
        print('MANO JUGADOR = ',jugador.getMano())
        print('MANO CPU = ',cpu.getMano())
        Actualizar_Atril_Jugador(window, jugador)
        Actualizar_Atril_Cpu(window, cpu)
        Comenzar_Juego(window,matriz_tablero,nivel,jugador,cpu,turno_jugador,turno_cpu,listas,historial)
    else: # si se cargo una partida guardada se inicia desde esa partida
        jugador=Atril([],0,nivel)
        cpu=Atril([],0,nivel)
        historial=[]
        jugador.repartirFichas()
        cpu.repartirFichas()
        turno_jugador,turno_cpu=True,False
        listas= {'pos_en_tablero':[],'letras_en_tablero':[],'pos_en_atril':[],
                 'casillas':[],'puntos_por_letra':[]}
        Comenzar_Juego(window,matriz_tablero,nivel,jugador,cpu,turno_jugador,turno_cpu,listas,historial)

def Comenzar_Juego(window, matriz_tablero, nivel,jugador,cpu,turno_jugador,turno_cpu,listas,historial):
    ''' Esta Funcion es en donde se ejecutan todas las operaciones que permiten
        la interaccion con el tablero y las manos de los jugadores entre otras
        cosas'''
    while True:
        if (turno_jugador) & (not turno_cpu):
            window.Element('Turno').Update('Jg')
            event, values = window.Read() # primer read para los botones y el atril del jugador
            if event in (None, 'TERMINAR'):
                Cargar_TopDiez({'puntaje': 0,
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
                if len(listas['pos_en_tablero'])!=0:# si el jugador coloco almenos 1 letra se evalua
                    word = checkWord(listas['pos_en_tablero'], matriz_tablero)
                    if not verifyWord(word):
                        matriz_tablero=Palabra_Invalida(listas,matriz_tablero,
                                                        window)
                        sg.Popup('Palabra invalida pierdes el turno')
                    else:
                        Actualizar_Puntos(jugador,'jugador',listas['casillas'],
                                          listas['puntos_por_letra'],window,historial,word,nivel)
                        window.Element('Palabras').Update(historial)
                    listas=Reiniciar_Listas(listas)

                    print(word)
                    print(verifyWord(word))
                else: # en caso de que no coloco una letra y dio fin de turno envia un mensaje
                    sg.Popup('Finalizaste el turno del jugador sin colocar una ficha')
                turno_jugador=False
                turno_cpu=True
            elif event=='Cambiar Fichas':#FALTA AGREGAR QUE SI EL JUGADOR CAMBIA LAS FICHAS PIERDE EL TURNO
                jugador.devolverFichas()
                Actualizar_Atril_Jugador(window, jugador)
                turno_jugador=False
                turno_cpu=True
                sg.Popup('Cambiaste tus fichas pierdes el turno')
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
        else: # variables en uso para la cpu: palabra_cpu, casilla_cpu, objeto cpu, window, linea
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
                    matriz_tablero=Colocar_Letras(window,casilla_cpu,'Horizontal',
                                                 palabra_cpu,matriz_tablero,
                                                 cpu,listas)
                else:
                    matriz_tablero=Colocar_Letras(window,casilla_cpu,'Vertical',
                                                 palabra_cpu,matriz_tablero,
                                                 cpu,listas)
                print('Palabra valida encontrada = ',palabra_cpu)
                print(listas['pos_en_tablero'])
                print(listas['pos_en_atril'])
                print(listas['letras_en_tablero'])
                print(listas['casillas'])
                print(listas['puntos_por_letra'])
                Actualizar_Puntos(cpu,'cpu',listas['casillas'],
                                  listas['puntos_por_letra'],window,historial,palabra_cpu,nivel)
                window.Element('Palabras').Update(historial)
            listas=Reiniciar_Listas(listas)
            turno_jugador=True
            turno_cpu=False


def Jugar(opcion):
    ''' Esta funcion trata de la configuracion del juego en donde se presentan
        2 menus el primero el cual contiene el boton Iniciar, CargarPartida y
        Salir y el segundo el cual se despliega al presionar el boton Iniciar
        que permite al usuario escoger que nivel de juego desea o si quiere
        configurar otros aspectos del juego'''
    if opcion == 'Iniciar':
        nivel = Dificultad()
        ok=True
        if nivel == 'FACIL':
            window, matriz_tablero, nivel = TableroFacil()
        elif nivel == 'MEDIO':
            window, matriz_tablero, nivel = TableroMedio()
        elif nivel == 'DIFICIL':
            window, matriz_tablero, nivel = TableroDificil()
        elif nivel == 'PERSONALIZADO':
            event, values = MenuPersonalizado()
            if event!=None:
                window, matriz_tablero, nivel = TableroPersonalizado(values['Nivel'])
            else:
                ok=False
        elif nivel== 'Volver':
            Jugar(MenuPrincipal())
        if ((nivel!='Volver')&(nivel!=None)&(ok)):
            Inicio(window, matriz_tablero, nivel,False)
    elif opcion == 'Cargar Partida':
        window, matriz_tablero, nivel,partida = CargarPartida()
        if (partida):
            Inicio(window, matriz_tablero, nivel,partida)


Jugar(MenuPrincipal())
