import json
from Tableros import *
from PySimpleGUI import Popup, PopupScrolled


def CargarPartida():
    ''' Esta funcion se encarga de cargar una partida existente '''
    try:
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
        nueva_matriz={}
        matriz_tablero = juego_tablero['Posiciones']
        for key in matriz_tablero:
            nueva_matriz[(int(key.strip('[] ').split(', ')[0]),int(key.strip('[] ').split(', ')[1]))]=matriz_tablero[key]
        for casilla, contenido in nueva_matriz.items():
            if contenido['letra'] != '':
                window.Element(casilla).Update(contenido['letra'])
        partida=True
    except (FileNotFoundError):
        print('No hay ninguna partida guardada')
        partida=False
        window,matriz_tablero,nivel=0,0,0
        Popup('No hay ninguna partida guardada')
    finally:
        return window, nueva_matriz, nivel, partida


def GuardarPartida(matriz_tablero, nivel):
    ''' Esta funcion se encarga de guardar una partida en un archivo en formato
        json'''
    nueva_matriz={}
    for key in matriz_tablero:
        nueva_matriz[json.dumps(key)]=matriz_tablero[key]
    juego_tablero = {'Nivel': nivel, 'Posiciones': nueva_matriz}

    archivo_juego = open('Partida.json', 'w')
    json.dump(juego_tablero, archivo_juego, indent=2)
    archivo_juego.close()


def order(elem):
    # lambda elem: elem['puntaje']
    return elem['puntaje']


def Cargar_TopDiez(data):
    ''' Esta funcion carga en un archivo en formato json el top 10 de jugadores'''
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
    ''' Esta funcion permite mostrar mediante la interfaz el top 10 de jugadores'''
    try:
        PopupScrolled(open('topten.txt').read(),
                      title='ScrabbleAR',
                      size=(24, 18))
    except FileNotFoundError:
        Popup('Sin records aún',
              title='ScrabbleAR',
              custom_text='Aceptar')
