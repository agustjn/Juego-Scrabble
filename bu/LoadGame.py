import json
from Tableros import *


def CargarPartida():
    juego_tablero = json.load(open('Partida.json', 'r'))
    nivel = juego_tablero['Nivel']
    if nivel == 'Facil':
        window, matriz_tablero, nivel = TableroFacil()
    elif nivel == 'Medio':
        window, matriz_tablero, nivel = TableroMedio()
    elif nivel == 'Dificil':
        window, matriz_tablero, nivel = TableroDificil()
    archivo_juego.close()
    matriz_tablero = juego_tablero['Posiciones']
    for casilla, contenido in matriz_tablero.items():
        if contenido['letra'] != '':
            window.Element(casilla).Update(contenido['letra'])
    return window, matriz_tablero, nivel


def GuardarPartida(matriz_tablero, nivel):
    juego_tablero = {'Nivel': nivel, 'Posiciones': matriz_tablero}
    json.dump(juego_tablero, open('Partida.json', 'w'), indent=2)
