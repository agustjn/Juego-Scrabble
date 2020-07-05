from PySimpleGUI import Window, Frame, Column, Button, Drop, Spin, Text
from os import getcwd


# ~~~~~~~~~~~~~~~ Funciones ~~~~~~~~~~~~~~~
def top_diez_txt_format(data):
    nuevo_top_diez = []
    for top in data:
        nuevo_top_diez.append('Puntos: {}\nFecha: {}\nDificultad: {}\n\n'.format(top['puntaje'], top['fecha'], top['dificultad']))
    return nuevo_top_diez

def detectEvent(evento):
    x=evento[0]
    y=evento[1]
    if (x=='jugador') | (x=='bot') | (x==int):
        return True
    else:
        return False

def manipularEvento(evento):
    x=evento[0]
    y=evento[1]
    if(type(x)==int): #SI CLICKIE EN LA MATRIZ
        return 'event_in_matriz'
    else:
        return 'event_in_atril'

 





# ~~~~~~~~~~~~~~~ Archivos ~~~~~~~~~~~~~~~
# JSON ~~~~~~~~~~~~~~~
juego_guardado_json = 'archivos/juego_guardado.json'
top_diez_json = 'archivos/top_diez.json'
enlaces_json = [juego_guardado_json, top_diez_json]
# TXT ~~~~~~~~~~~~~~~
top_diez_txt = '{}\\archivos\\top_diez.txt'.format(getcwd())


# ~~~~~~~~~~~~~~~ Parámetros del tablero ~~~~~~~~~~~~~~~
llaves_tablero = [[(x, y) for x in range(15)] for y in range(15)]
parametros = {'dificultad': '',
              'puntos_jugador': 0,
              'puntos_bot': 0,
              'matriz': {}}
puntos_facil = {'jugador': {'puntos_verde': ': x2',
                            'puntos_azul': ': +4',
                            'puntos_amarillo': ': +3',
                            'puntos_gris': ': +2',
                            'puntos_rojo': ': -1'},
                'bot': {'puntos_verde': ': x2',
                        'puntos_azul': ': +3',
                        'puntos_amarillo': ': +2',
                        'puntos_gris': ': +1',
                        'puntos_rojo': ': -3'}}
puntos_medio = {'jugador': {'puntos_verde': ': x2',
                            'puntos_azul': ': +3',
                            'puntos_amarillo': ': +2',
                            'puntos_gris': ': +1',
                            'puntos_rojo': ': -1'},
                'bot': {'puntos_verde': ': x2',
                        'puntos_azul': ': +3',
                        'puntos_amarillo': ': +2',
                        'puntos_gris': ': +1',
                        'puntos_rojo': ': -1'}}
puntos_dificil = {'jugador': {'puntos_verde': ': x1',
                              'puntos_azul': ': +3',
                              'puntos_amarillo': ': +2',
                              'puntos_gris': ': +1',
                              'puntos_rojo': ': -1'},
                  'bot': {'puntos_verde': ': x2',
                          'puntos_azul': ': +4',
                          'puntos_amarillo': ': +3',
                          'puntos_gris': ': +2',
                          'puntos_rojo': ': -1'}}
puntos_por_color = {'FÁCIL': puntos_facil,
                    'MEDIO': puntos_medio,
                    'DIFICIL': puntos_dificil}
