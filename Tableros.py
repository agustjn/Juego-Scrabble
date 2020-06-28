from ElementosTableros import *
from const import colores_Facil,colores_Medio,colores_Dificil
def TableroFacil():
    ''' Esta funcion consiste en generar el tablero de juego nivel facil con sus
        casillas predeterminadas'''
    tablero = Tablero()
    botones = Botones()
    puntos_jugador = Puntos_jugador()
    puntos_cpu = Puntos_cpu()
    turno_actual=Turno_actual()
    puntos_botones = Puntos_Y_Botones(puntos_jugador,puntos_cpu,botones,turno_actual)
    letras_jugador = Letras_jugador()
    letras_cpu = Letras_cpu()
    botones_turno = Botones_Turno()
    atril_jugador = Atril_jugador(letras_jugador,botones_turno)
    atril_cpu = Atril_cpu(letras_cpu)
    layout = Layout(tablero,puntos_botones,atril_jugador,atril_cpu)
    window = Window(layout,'Facil')
    matriz_tablero = Crear_Tablero(colores_Facil,window)
    return window,  matriz_tablero,  'Facil'

def TableroMedio():
    ''' Esta funcion consiste en generar el tablero de juego nivel medio con sus
        casillas predeterminadas'''
    tablero = Tablero()
    botones = Botones()
    puntos_jugador = Puntos_jugador()
    puntos_cpu = Puntos_cpu()
    turno_actual=Turno_actual()
    puntos_botones = Puntos_Y_Botones(puntos_jugador,puntos_cpu,botones,turno_actual)
    letras_jugador = Letras_jugador()
    letras_cpu = Letras_cpu()
    botones_turno = Botones_Turno()
    atril_jugador = Atril_jugador(letras_jugador,botones_turno)
    atril_cpu = Atril_cpu(letras_cpu)
    layout = Layout(tablero,puntos_botones,atril_jugador,atril_cpu)
    window = Window(layout,'Medio')
    matriz_tablero = Crear_Tablero(colores_Medio,window)
    return window,  matriz_tablero,  'Medio'

def TableroDificil():
    ''' Esta funcion consiste en generar el tablero de juego nivel dificil con sus
        casillas predeterminadas'''
    tablero = Tablero()
    botones = Botones()
    puntos_jugador = Puntos_jugador()
    puntos_cpu = Puntos_cpu()
    turno_actual=Turno_actual()
    puntos_botones = Puntos_Y_Botones(puntos_jugador,puntos_cpu,botones,turno_actual)
    letras_jugador = Letras_jugador()
    letras_cpu = Letras_cpu()
    botones_turno = Botones_Turno()
    atril_jugador = Atril_jugador(letras_jugador,botones_turno)
    atril_cpu = Atril_cpu(letras_cpu)
    layout = Layout(tablero,puntos_botones,atril_jugador,atril_cpu)
    window = Window(layout,'Dificil')
    matriz_tablero = Crear_Tablero(colores_Dificil,window)
    return window,  matriz_tablero,  'Dificil'


def TableroPersonalizado(nivel):
    ''' Esta funcion consiste en generar el tablero de juego segun que
        configuracion especifica haya escogido el usuario retornando el tablero
        especifico con sus casillas predeterminadas'''
    if nivel == 'Facil':
        window, matriz_tablero, nivel = TableroFacil()
    elif nivel == 'Medio':
        window, matriz_tablero, nivel = TableroMedio()
    elif nivel == 'Dificil':
        window, matriz_tablero, nivel = TableroDificil()
    return window, matriz_tablero, nivel
