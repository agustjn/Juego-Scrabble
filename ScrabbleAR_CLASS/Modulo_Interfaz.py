from PySimpleGUI import Window, Popup, Frame, Column, Button, Drop, Spin, Text
from const import llaves_tablero
from const import parametros
import json


# Imagenes y colores ~~~~~~~~~~~~~~~
# Para editar el color de fondo, 'window_color',
# pueden usar este link: https://www.google.com/search?q=rgb+color+picker&oq=rgb+color+picker&aqs=chrome..69i57.2461j0j4&sourceid=chrome&ie=UTF-8
window_color = '#5c2a2d'
boton_opcion = 'media/botones/boton_opcion.png'
boton_salir = 'media/botones/boton_salir.png'
boton_rojo = 'media/botones/boton_rojo.png'
boton_verde = 'media/botones/boton_verde.png'
boton_azul = 'media/botones/boton_azul.png'
boton_amarillo = 'media/botones/boton_amarillo.png'
boton_gris = 'media/botones/boton_gris.png'
colores_facil = {'amarillo':   [(1,  1), (7, 0), (13, 1), (0, 7), (7, 7), (14, 7),
                                (1,  13), (7, 14), (13, 13)],
                 'verde':    [(0,  0), (14, 0), (0, 14), (14, 14), (6, 3), (7, 4),
                              (8,  3), (3, 6), (4, 7), (3, 8), (11, 6), (10, 7),
                              (11, 8), (6, 11), (7, 12), (8, 11)],
                 'azul':     [(2,  4), (4, 1), (10, 1), (12, 4), (6, 6), (6, 8),
                              (8,  6), (8, 8), (2, 10), (3, 13), (12, 10), (10, 13)],
                 'rojo':      [(3,  3), (7, 3), (11, 3), (2, 7), (12, 7), (3, 11),
                               (7,  11), (11, 11)]}
colores_medio = {'amarillo':   [(0, 0), (4, 4), (7, 7), (4, 10), (0, 14), (10, 4),
                                (14, 0), (10, 10), (14, 14), (2, 4), (2, 10), (4, 12),
                                (10, 12), (12, 4), (12, 10), (4, 2), (10, 2)],
                 'verde':    [(2, 2), (6, 6), (6, 8), (2, 12), (8, 6), (12, 2),
                              (8, 8), (12, 12), (0, 4), (0, 10), (4, 14), (10, 14),
                              (14, 4), (14, 10), (4, 0), (10, 0)],
                 'azul':     [(7, 1), (7, 5), (7, 9), (7, 13), (9, 7), (13, 7),
                              (5, 7), (1, 7)],
                 'rojo':      [(7, 3), (7, 11), (11, 7), (3, 7), (2, 6), (2, 8),
                               (6, 12), (8, 12), (12, 6), (12, 8), (6, 2), (8, 2)]}
colores_dificil = {'amarillo': [(5, 0), (11, 4), (6, 6), (0, 7), (1, 7), (13, 7),
                                (14, 7), (8, 8), (3, 10), (9, 14)],
                   'verde':  [(2, 0), (12, 0), (4, 2), (10, 2), (2, 5), (13, 5),
                              (4, 7), (5, 7), (9, 7), (10, 7), (1, 9), (13, 9),
                              (4, 12), (10, 12), (2, 14), (12, 14)],
                   'azul':   [(7, 0), (9, 0), (7, 2), (3, 4), (8, 6), (3, 7),
                              (6, 7), (8, 7), (11, 7), (6, 8), (11, 10), (7, 12),
                              (5, 14), (7, 14)],
                   'rojo':    [(1, 1), (3, 1), (11, 1), (13, 1), (3, 3), (5, 3),
                               (9, 3), (11, 3), (1, 4), (13, 4), (5, 5), (7, 5),
                               (9, 5), (1, 6), (13, 6), (2, 7), (7, 7), (12, 7),
                               (1, 8), (13, 8), (5, 9), (7, 9), (9, 9), (1, 10),
                               (13, 10), (3, 11), (5, 11), (9, 11), (11, 11),
                               (1, 13), (3, 13), (11, 13), (13, 13)]}
color_botones = {'FÁCIL': colores_facil,
                 'MEDIO': colores_medio,
                 'DIFICIL': colores_dificil}


# Tamaños ~~~~~~~~~~~~~~~
spin_rango = [time for time in range(10, 31)]
boton_opcion_size = (23, 5)
boton_tablero_size = (3, 1)
boton_tablero_pad = (0, 0)
text_puntos_de_quien_size = (12, 1)
text_puntos_size = (4, 1)
text_puntos_por_boton = (14, 1)
text_size = (16, 1)
frame_size = (10, 0)
frame_padd = (0, 0)
column_pad = (0, 0)
margins_size = (0, 0)
font_size = 24
fichas_pad = (6, 0)
drop_size = (6, 1)
rules_size = (14, 2)


# ~~~~~~~~~~~~~~~ Elementos del menú ~~~~~~~~~~~~~~~
botones_de_opcion_menu = [[Button(button_text='FÁCIL',
                                  key='FÁCIL',
                                  image_filename=boton_opcion)],
                          [Button(button_text='MEDIO',
                                  key='MEDIO',
                                  image_filename=boton_opcion)],
                          [Button(button_text='DIFICIL',
                                  key='DIFICIL',
                                  image_filename=boton_opcion)],
                          [Button(button_text='CARGAR PARTIDA',
                                  key='cargar_partida',
                                  image_filename=boton_opcion)]]
frame_menu = [[Frame(layout=[[Text(text='DIFICULTAD    ',
                                   background_color=window_color),
                              Drop(values=['FÁCIL', 'MEDIO', 'DIFICIL'],
                                   default_value='FÁCIL',
                                   key='dificultad_personalizada',
                                   size=drop_size)],
                             [Text(text='TIEMPO DE TURNO',
                                   background_color=window_color),
                              Spin(values=spin_rango,
                                   key='tiempo_de_turno')],
                             [Button(button_text='ACEPTAR',
                                     key='personalizado',
                                     image_filename=boton_opcion)]],
                     title='PERZONALIZADO',
                     background_color=window_color)]]
columna_menu = [[Column(layout=botones_de_opcion_menu,
                        background_color=window_color),
                 Column(layout=frame_menu,
                        background_color=window_color)]]
layout_menu = [[Frame(layout=columna_menu,
                      title='INICIAR',
                      background_color=window_color)],
               [Button(button_text='',
                       key='salir',
                       image_filename=boton_salir)]]
window_menu = Window(layout=layout_menu,
                     title='ScrabbleAR',
                     font=font_size,
                     margins=margins_size,
                     background_color=window_color)


# ~~~~~~~~~~~~~~~ Elementos del juego ~~~~~~~~~~~~~~~
tablero = [[Button(button_text='',
                   size=boton_tablero_size,
                   button_color=('black',  'grey'),
                   pad=boton_tablero_pad,
                   key=(x, y)) for x in range(15)] for y in range(15)]
letras_jugador = [[Button(button_text='',
                          key=('jugador', y),
                          button_color=('black',  'grey'),
                          size=boton_tablero_size,
                          pad=fichas_pad,) for y in range(7)]]
letras_bot = [[Button(button_text='',
                      key=('bot', y),
                      button_color=('black',  'grey'),
                      size=boton_tablero_size,
                      pad=fichas_pad,) for y in range(7)]]
frame_letras = [[Frame(layout=[[Column(layout=letras_jugador,
                                       background_color=window_color)],
                               [Button(button_text='CAMBIAR FICHAS',
                                       key='cambiar_fichas',
                                       image_filename=boton_opcion),
                                Button(button_text='FIN DE TURNO',
                                       key='fin_de_turno',
                                       image_filename=boton_opcion)]],
                       title='MIS FICHAS',
                       background_color=window_color,
                       pad=frame_size),
                 Frame(layout=[[Column(layout=letras_bot,
                                       background_color=window_color)]],
                       title='SUS FICHAS',
                       background_color=window_color,
                       pad=frame_size)]]
puntos = [[Text(text='MIS PUNTOS:',
                size=text_puntos_de_quien_size,
                background_color=window_color),
           Text(text='0',
                key='puntos_jugador',
                size=text_puntos_size,
                background_color=window_color)],
          [Text(text='SUS PUNTOS:',
                size=text_puntos_de_quien_size,
                background_color=window_color),
           Text(text='0',
                key='puntos_bot',
                size=text_puntos_size,
                background_color=window_color)]]
frame_reglas = [[Frame(layout=[[Text(text='SOLO VERBOS\nHABLITADOS',
                                     key='reglas',
                                     size=rules_size,
                                     background_color=window_color)],
                               [Button(image_filename=boton_verde),
                                Text(text=': +0 PUNTOS',
                                     size=text_puntos_por_boton,
                                     background_color=window_color)],
                               [Button(image_filename=boton_amarillo),
                                Text(text=': +0 PUNTOS',
                                     size=text_puntos_por_boton,
                                     background_color=window_color)],
                               [Button(image_filename=boton_azul),
                                Text(text=': +0 PUNTOS',
                                     size=text_puntos_por_boton,
                                     background_color=window_color)],
                               [Button(image_filename=boton_gris),
                                Text(text=': +0 PUNTOS',
                                     size=text_puntos_por_boton,
                                     background_color=window_color)],
                               [Button(image_filename=boton_rojo),
                                Text(text=': -0 PUNTOS',
                                     size=text_puntos_por_boton,
                                     background_color=window_color)]],
                       title='REGLAS',
                       background_color=window_color)]]
botones_de_opcion_juego = [[Button(button_text='TOP 10',
                                   key='top_diez',
                                   pad=boton_opcion_size,
                                   image_filename=boton_opcion)],
                           [Button(button_text='POSPONER',
                                   key='guardar_partida',
                                   pad=boton_opcion_size,
                                   image_filename=boton_opcion)],
                           [Button(button_text='TERMINAR',
                                   key='salir',
                                   pad=boton_opcion_size,
                                   image_filename=boton_opcion)]]
columna_de_juego_derecha = [[Column(layout=puntos,
                                    background_color=window_color)],
                            [Column(layout=frame_reglas,
                                    background_color=window_color)],
                            [Column(layout=botones_de_opcion_juego,
                                    background_color=window_color)]]
layout_juego = [[Column(layout=tablero,
                        background_color=window_color),
                 Column(layout=columna_de_juego_derecha,
                        background_color=window_color)],
                [Column(layout=frame_letras,
                        background_color=window_color)]]
window_tablero = Window(layout=layout_juego,
                        title='ScrabbleAR',
                        font=font_size,
                        margins=margins_size,
                        background_color=window_color)


class Interfaz():

    # Inicializa una variable para la ventana.
    def __init__(self):
        self._window = None

    # Carga la ventana
    def set_window(self, window):
        self._window = window.Finalize()

    # Devuelve la ventana
    def get_window(self):
        return self._window

    def set_menu_window(self):
        self.set_window(window_menu)

    def set_tablero_window(self):
        self.set_window(window_tablero)

    # Cierra la ventana
    def cerrar(self):
        self._window.Close()
        self._window = None

    # Función para solo actualizar parámetros de tipo valor,
    # keys = {Clave del elemento i: Valor a actualizar del elemento i}.
    def update(self, keys):
        for key in keys:
            self._window[key].Update(keys[key])

    # Para cada tipo de color, inserta la imagen respectiva
    # en cada botón. Inserta la imagen 'gris' según los
    # colores insertados.
    def colorear(self, colores):
        coordenadas_no_gris = []
        for coor in colores['rojo']:
            coordenadas_no_gris.append(coor)
            self._window[coor].Update(image_filename=boton_rojo)
        for coor in colores['verde']:
            coordenadas_no_gris.append(coor)
            self._window[coor].Update(image_filename=boton_verde)
        for coor in colores['azul']:
            coordenadas_no_gris.append(coor)
            self._window[coor].Update(image_filename=boton_azul)
        for coor in colores['amarillo']:
            coordenadas_no_gris.append(coor)
            self._window[coor].Update(image_filename=boton_amarillo)
        for coordenadas in llaves_tablero:
            for coor in coordenadas:
                if coor not in coordenadas_no_gris:
                    self._window[coor].Update(image_filename=boton_gris)

    # _parametros_tablero = {'dificultad': '',
    #                        'matriz': {(x, y): 'caracter'}}
    # Carga los colores según la dificultad desde 'colorear'.
    # Traduce la matriz de llaves tipo string a tuplas de enteros.
    def cargar_parametros(self, parametros_juego):
        self.colorear(color_botones[parametros_juego['dificultad']])
        matriz_formateada = {}
        for key in parametros_juego['matriz']:
            matriz_formateada[(int(key.strip('[ ]').split(', ')[0]), int(key.strip('[ ]').split(', ')[1]))] = parametros_juego['matriz'][key]
        self.update(matriz_formateada)

    # Devuelve los parametros actuales en formato JSON para cargarse.
    def guardar_parametros(self, dificultad):
        parametros_juego = parametros
        parametros_juego['dificultad'] = dificultad
        for keys in llaves_tablero:
            for key in keys:
                parametros_juego['matriz'][json.dumps(key)] = self._window[key].GetText()
        return parametros_juego

    # Imprime un Popup con 'titulo' como valor.
    def mensaje(self, titulo):
        Popup(titulo,
              title='ScrabbleAR',
              custom_text='ACEPTAR',
              font=font_size)
