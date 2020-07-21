from PySimpleGUI import Window, Frame, Column, Button, Drop, Spin, Text


#
# LLAVES (KEYS) DEL TABLERO, LOS ATRILES Y EL HISTORIAL DE PUNTUACIONES
#
matriz = [(x, y) for x in range(15) for y in range(15)]
atril_jugador = [('jugador', y) for y in range(7)]
atril_bot = [('bot', y) for y in range(7)]
historial = [('puntuacion', i) for i in range(50)]

#
# COLOR DE LOS BOTONES SEGÚN LA DIFICULTAD
#
color_botones = {'FÁCIL': {('Black', 'Yellow'):   [(1,  1), (7, 0), (13, 1), (0, 7), (7, 7), (14, 7), (1,  13), (7, 14), (13, 13)],
                           ('Black', 'Green'):    [(0,  0), (14, 0), (0, 14), (14, 14), (6, 3), (7, 4), (8,  3), (3, 6), (4, 7), (3, 8), (11, 6), (10, 7), (11, 8), (6, 11), (7, 12), (8, 11)],
                           ('Black', 'Blue'):     [(2,  4), (4, 1), (10, 1), (12, 4), (6, 6), (6, 8), (8,  6), (8, 8), (2, 10), (3, 13), (12, 10), (10, 13)],
                           ('Black', 'Red'):      [(3,  3), (7, 3), (11, 3), (2, 7), (12, 7), (3, 11), (7,  11), (11, 11)],
                           ('Black', 'Grey'):     [(0, 1), (0, 2), (0, 3), (0, 5), (0, 6), (0, 8), (0, 9), (0, 11), (0, 12), (0, 13), (1, 0), (1, 2), (1, 3), (1, 5), (1, 8), (1, 10), (1, 11), (1, 12), (1, 14), (2, 1), (2, 3), (2, 8), (2, 9), (2, 11), (2, 13), (3, 0), (3, 2), (3, 5), (3, 9), (3, 12), (3, 14), (4, 3), (4, 5), (4, 6), (4, 8), (4, 9), (4, 11), (4, 13), (5, 1), (5, 2), (5, 4), (5, 6), (5, 8), (5, 10), (5, 12), (5, 13), (6, 0), (6, 1), (6, 4), (6, 5), (6, 9), (6, 10), (6, 13), (6, 14), (7, 4), (7, 6), (7, 8), (7, 10), (8, 0), (8, 1), (8, 4), (8, 5), (8, 9), (8, 10), (8, 13), (8, 14), (9, 1), (9, 2), (9, 4), (9, 6), (9, 8), (9, 10), (9, 12), (9, 13), (10, 2), (10, 3), (10, 5), (10, 6), (10, 8), (10, 9), (10, 11), (10, 14), (11, 0), (11, 2), (11, 5), (11, 9), (11, 12), (11, 14), (12, 1), (12, 3), (12, 5), (12, 8), (12, 9), (12, 11), (12, 13), (13, 0), (13, 2), (13, 3), (13, 5), (13, 8), (13, 10), (13, 11), (13, 12), (13, 14), (14, 1), (14, 2), (14, 3), (14, 5), (14, 6), (14, 8), (14, 9), (14, 11), (14, 12), (14, 13)]},
                 'MEDIO': {('Black', 'Yellow'):   [(0, 0), (4, 4), (7, 7), (4, 10), (0, 14), (10, 4), (14, 0), (10, 10), (14, 14), (2, 4), (2, 10), (4, 12), (10, 12), (12, 4), (12, 10), (4, 2), (10, 2)],
                           ('Black', 'Green'):    [(2, 2), (6, 6), (6, 8), (2, 12), (8, 6), (12, 2), (8, 8), (12, 12), (0, 4), (0, 10), (4, 14), (10, 14), (14, 4), (14, 10), (4, 0), (10, 0)],
                           ('Black', 'Blue'):     [(7, 1), (7, 5), (7, 9), (7, 13), (9, 7), (13, 7), (5, 7), (1, 7)],
                           ('Black', 'Red'):      [(7, 3), (7, 11), (11, 7), (3, 7), (2, 6), (2, 8), (6, 12), (8, 12), (12, 6), (12, 8), (6, 2), (8, 2)],
                           ('Black', 'Grey'):     [(0, 1), (0, 2), (0, 3), (0, 5), (0, 6), (0, 8), (0, 9), (0, 11), (0, 12), (0, 13), (1, 0), (1, 2), (1, 3), (1, 5), (1, 8), (1, 10), (1, 11), (1, 12), (1, 14), (2, 1), (2, 3), (2, 8), (2, 9), (2, 11), (2, 13), (3, 0), (3, 2), (3, 5), (3, 9), (3, 12), (3, 14), (4, 3), (4, 5), (4, 6), (4, 8), (4, 9), (4, 11), (4, 13), (5, 1), (5, 2), (5, 4), (5, 6), (5, 8), (5, 10), (5, 12), (5, 13), (6, 0), (6, 1), (6, 4), (6, 5), (6, 9), (6, 10), (6, 13), (6, 14), (7, 4), (7, 6), (7, 8), (7, 10), (8, 0), (8, 1), (8, 4), (8, 5), (8, 9), (8, 10), (8, 13), (8, 14), (9, 1), (9, 2), (9, 4), (9, 6), (9, 8), (9, 10), (9, 12), (9, 13), (10, 2), (10, 3), (10, 5), (10, 6), (10, 8), (10, 9), (10, 11), (10, 14), (11, 0), (11, 2), (11, 5), (11, 9), (11, 12), (11, 14), (12, 1), (12, 3), (12, 5), (12, 8), (12, 9), (12, 11), (12, 13), (13, 0), (13, 2), (13, 3), (13, 5), (13, 8), (13, 10), (13, 11), (13, 12), (13, 14), (14, 1), (14, 2), (14, 3), (14, 5), (14, 6), (14, 8), (14, 9), (14, 11), (14, 12), (14, 13)]},
                 'DIFICIL': {('Black', 'Yellow'): [(5, 0), (11, 4), (6, 6), (0, 7), (1, 7), (13, 7), (14, 7), (8, 8), (3, 10), (9, 14)],
                             ('Black', 'Green'):  [(2, 0), (12, 0), (4, 2), (10, 2), (2, 5), (13, 5), (4, 7), (5, 7), (9, 7), (10, 7), (1, 9), (13, 9), (4, 12), (10, 12), (2, 14), (12, 14)],
                             ('Black', 'Blue'):   [(7, 0), (9, 0), (7, 2), (3, 4), (8, 6), (3, 7), (6, 7), (8, 7), (11, 7), (6, 8), (11, 10), (7, 12), (5, 14), (7, 14)],
                             ('Black', 'Red'):    [(1, 1), (3, 1), (11, 1), (13, 1), (3, 3), (5, 3), (9, 3), (11, 3), (1, 4), (13, 4), (5, 5), (7, 5), (9, 5), (1, 6), (13, 6), (2, 7), (7, 7), (12, 7), (1, 8), (13, 8), (5, 9), (7, 9), (9, 9), (1, 10), (13, 10), (3, 11), (5, 11), (9, 11), (11, 11), (1, 13), (3, 13), (11, 13), (13, 13)],
                             ('Black', 'Grey'):   [(0, 1), (0, 2), (0, 3), (0, 5), (0, 6), (0, 8), (0, 9), (0, 11), (0, 12), (0, 13), (1, 0), (1, 2), (1, 3), (1, 5), (1, 8), (1, 10), (1, 11), (1, 12), (1, 14), (2, 1), (2, 3), (2, 8), (2, 9), (2, 11), (2, 13), (3, 0), (3, 2), (3, 5), (3, 9), (3, 12), (3, 14), (4, 3), (4, 5), (4, 6), (4, 8), (4, 9), (4, 11), (4, 13), (5, 1), (5, 2), (5, 4), (5, 6), (5, 8), (5, 10), (5, 12), (5, 13), (6, 0), (6, 1), (6, 4), (6, 5), (6, 9), (6, 10), (6, 13), (6, 14), (7, 4), (7, 6), (7, 8), (7, 10), (8, 0), (8, 1), (8, 4), (8, 5), (8, 9), (8, 10), (8, 13), (8, 14), (9, 1), (9, 2), (9, 4), (9, 6), (9, 8), (9, 10), (9, 12), (9, 13), (10, 2), (10, 3), (10, 5), (10, 6), (10, 8), (10, 9), (10, 11), (10, 14), (11, 0), (11, 2), (11, 5), (11, 9), (11, 12), (11, 14), (12, 1), (12, 3), (12, 5), (12, 8), (12, 9), (12, 11), (12, 13), (13, 0), (13, 2), (13, 3), (13, 5), (13, 8), (13, 10), (13, 11), (13, 12), (13, 14), (14, 1), (14, 2), (14, 3), (14, 5), (14, 6), (14, 8), (14, 9), (14, 11), (14, 12), (14, 13)]}}

#
# PUNTOS DE LOS BOTONES SEGÚN LA DIFICULTAD
#
puntos_botones = {'FÁCIL': {'jugador': {'puntos_verde': 'x2',
                                        'puntos_azul': '+4',
                                        'puntos_amarillo': '+3',
                                        'puntos_gris': '+2',
                                        'puntos_rojo': '-1'},
                            'bot': {'puntos_verde': 'x2',
                                    'puntos_azul': '+3',
                                    'puntos_amarillo': '+2',
                                    'puntos_gris': '+1',
                                    'puntos_rojo': '-3'}},
                  'MEDIO': {'jugador': {'puntos_verde': 'x2',
                                        'puntos_azul': '+3',
                                        'puntos_amarillo': '+2',
                                        'puntos_gris': '+1',
                                        'puntos_rojo': '-1'},
                            'bot': {'puntos_verde': 'x2',
                                    'puntos_azul': '+3',
                                    'puntos_amarillo': '+2',
                                    'puntos_gris': '+1',
                                    'puntos_rojo': '-1'}},
                  'DIFICIL': {'jugador': {'puntos_verde': 'x1',
                                          'puntos_azul': '+3',
                                          'puntos_amarillo': '+2',
                                          'puntos_gris': '+1',
                                          'puntos_rojo': '-1'},
                              'bot': {'puntos_verde': 'x2',
                                      'puntos_azul': '+4',
                                      'puntos_amarillo': '+3',
                                      'puntos_gris': '+2',
                                      'puntos_rojo': '-1'}}}

#
# BOLSA PREDETERMINADA
#
bolsa = {'A': {'cantidad': 9, 'puntaje': 1}, 'E': {'cantidad': 9, 'puntaje': 1},
         'O': {'cantidad': 8, 'puntaje': 1}, 'S': {'cantidad': 7, 'puntaje': 1},
         'I': {'cantidad': 6, 'puntaje': 1}, 'U': {'cantidad': 6, 'puntaje': 1},
         'N': {'cantidad': 5, 'puntaje': 1}, 'R': {'cantidad': 4, 'puntaje': 1},
         'T': {'cantidad': 4, 'puntaje': 1}, 'C': {'cantidad': 4, 'puntaje': 2},
         'D': {'cantidad': 4, 'puntaje': 2}, 'G': {'cantidad': 2, 'puntaje': 2},
         'M': {'cantidad': 3, 'puntaje': 3}, 'B': {'cantidad': 2, 'puntaje': 3},
         'H': {'cantidad': 2, 'puntaje': 4}, 'V': {'cantidad': 2, 'puntaje': 4},
         'Y': {'cantidad': 2, 'puntaje': 4}, 'J': {'cantidad': 2, 'puntaje': 6},
         'K': {'cantidad': 1, 'puntaje': 8}, 'Ñ': {'cantidad': 1, 'puntaje': 8},
         'Q': {'cantidad': 1, 'puntaje': 8}, 'W': {'cantidad': 2, 'puntaje': 8},
         'X': {'cantidad': 2, 'puntaje': 8}, 'Z': {'cantidad': 2, 'puntaje': 10},
         'L': {'cantidad': 4, 'puntaje': 1}, 'P': {'cantidad': 2, 'puntaje': 3},
         'F': {'cantidad': 2, 'puntaje': 4}}


#
# ~~~~~~~~~~ FUNCIONES
#
def reglas(dificultad, tiempo): # SE IMPRIMEN LAS RESPECTIVAS REGLAS SEGÚN LA DIFICULTAD. EL TIEMPO ES OPCIONAL SEGÚN LO INGRESADO DESDE EL MENÚ (PREDETERMINADAMENTE ENTRAN 20 SEGUNDOS)
    if dificultad == 'FÁCIL':
        return '     DIFICULTAD:\n           '+dificultad+'.\n      PALABRAS\n    HABILITADAS:\n          TODAS.\n     TIEMPO POR\n       TURNO: '+str(tiempo)+'\n      SEGUNDOS'
    else:
        return '    DIFICULTAD:\n         '+dificultad+'.\n      PALABRAS\n    HABILITADAS:\n      ADJETIVOS\n       Y VERBOS.\n     TIEMPO POR\n       TURNO: '+str(tiempo)+'\n      SEGUNDOS'


def const_Update(window, *args):
    for keys in args: # PARA CADA VARIABLE DENTRO DE LOS ARGUMENTOS
        if keys:  # SI ESTA NÓ ESTÁ VACÍA
            if type(list(keys.values())[0]) is not list:  # SI EL VALOR DE LA LLAVE NO ES UNA LISTA
                for key in keys:  # PARA CADA LLAVE EN EL DICCIONARIO
                    window.Element(key).Update(keys[key]) # SE ACTUALIZA LA VENTANA CON EL VALOR DE ESA LLAVE
            else: # SI EL VALOR DE LA LLAVE ES UNA LISTA
                for i in keys:
                    for j in keys[i]:
                        window.Element(j).Update(button_color=i)  # ESTA ACTUALIZACIÓN SOLO SIRVE PARA ASIGNAR COLORES
