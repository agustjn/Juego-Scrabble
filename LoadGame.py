import json
from Tableros import *
from PySimpleGUI import Popup, PopupScrolled


def CargarPartida():
    archivo_juego = open('Partida.json', 'r')
    juego_tablero = json.load(archivo_juego)
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
    archivo_juego = open('Partida.json', 'w')
    json.dump(juego_tablero, archivo_juego, indent=2)
    archivo_juego.close()


def order(elem):
    # lambda elem: elem['puntaje']
    return elem['puntaje']


def Cargar_TopDiez(data):
    try:
        data_topdiez_json = json.load(open('topten.json'))
        data_topdiez_json.append(data)
        json.dump(sorted(data_topdiez_json, key=order, reverse=True),
                  open('topten.json', 'w'), indent=4)
    except FileNotFoundError:
        json.dump([data], open('topten.json', 'w'), indent=4)
    data_topdiez_txt = open('topten.txt', 'w')
    top_diez = 0
    for play in json.load(open('topten.json')):
        data_topdiez_txt.write('Puntaje: {}\nFecha: {}\nNivel: {}\n\n'.format(
                                play['puntaje'],
                                play['fecha'],
                                play['nivel']))
        top_diez += 1
        if top_diez == 10:
            break


def Ver_TopDiez():
    try:
        PopupScrolled(open('topten.txt').read(),
                      title='ScrabbleAR',
                      size=(24, 18),
                      font=(24))
    except FileNotFoundError:
        Popup('Sin records aún',
              title='ScrabbleAR',
              custom_text='Aceptar',
              font=24)
