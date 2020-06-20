from PySimpleGUI import Window, Frame, Column, Button, Drop, Spin, Text
from os import getcwd


# ~~~~~~~~~~~~~~~ Funciones ~~~~~~~~~~~~~~~
def top_diez_txt_format(data):
    nuevo_top_diez = []
    for top in data:
        nuevo_top_diez.append('Puntos: {}\nFecha: {}\nDificultad: {}\n\n'.format(top['puntaje'], top['fecha'], top['dificultad']))
    return nuevo_top_diez


# ~~~~~~~~~~~~~~~ Archivos ~~~~~~~~~~~~~~~
# JSON ~~~~~~~~~~~~~~~
juego_guardado_json = 'archivos/juego_guardado.json'
top_diez_json = 'archivos/top_diez.json'
enlaces_json = [juego_guardado_json, top_diez_json]
# TXT ~~~~~~~~~~~~~~~
top_diez_txt = '{}\\archivos\\top_diez.txt'.format(getcwd())


# ~~~~~~~~~~~~~~~ Parámetros del tablero ~~~~~~~~~~~~~~~
llaves_tablero = [[(x, y) for x in range(15)] for y in range(15)]
parametros = {'dificultad': '', 'matriz': {}}
