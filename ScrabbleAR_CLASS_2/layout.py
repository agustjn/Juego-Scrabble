from PySimpleGUI import Window, Frame, Column, Button, Drop, Spin, Text


boton_opcion = 'media/boton_opcion.png'
boton_salir = 'media/boton_salir.png'
window_color = '#1c1c1c'
spin_rango = [time for time in range(10, 31)]
boton_opcion_size = (23, 5)
boton_tablero_size = (3, 1)
boton_tablero_pad = (0, 0)
text_puntos_de_quien_size = (12, 1)
text_segundos_size = (2, 1)
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
rules_size = (14, 8)


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
                                   key='dificultad',
                                   size=drop_size)],
                             [Text(text='TIEMPO DE TURNO',
                                   background_color=window_color),
                              Spin(values=spin_rango,
                                   key='tiempo_por_turno')],
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
                   button_color=('White',  'Grey'),
                   pad=boton_tablero_pad,
                   key=(x, y)) for x in range(15)] for y in range(15)]
letras_jugador = [[Button(button_text='',
                          key=('jugador', y),
                          button_color=('White',  'Grey'),
                          size=boton_tablero_size,
                          pad=fichas_pad,) for y in range(7)]]
letras_bot = [[Button(button_text='',
                      key=('bot', y),
                      button_color=('White',  'Grey'),
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
                       title='MIS FICHAS~~~~~~~TOTAL DE FICHAS: ',
                       key='fichas_jugador',
                       background_color=window_color,
                       pad=frame_size),
                 Frame(layout=[[Column(layout=letras_bot,
                                       background_color=window_color)]],
                       title='SUS FICHAS',
                       key='fichas_bot',
                       background_color=window_color,
                       pad=frame_size)]]
puntos = [[Text(text='MIS PUNTOS: ',
                size=text_puntos_de_quien_size,
                background_color=window_color),
           Text(text='0',
                key='puntos_jugador',
                size=text_puntos_size,
                background_color=window_color)],
          [Text(text='SUS PUNTOS: ',
                size=text_puntos_de_quien_size,
                background_color=window_color),
           Text(text='0',
                key='puntos_bot',
                size=text_puntos_size,
                background_color=window_color)]]
frame_reglas = [[Frame(layout=[[Column(layout=[[Text(key='reglas',
                                                     size=rules_size,
                                                     background_color=window_color)]],
                                       background_color=window_color)],
                               [Column(layout=[[Button(button_text='',
                                                       key='puntos_verde',
                                                       button_color=('White', 'Green'),
                                                       size=boton_tablero_size,
                                                       pad=boton_tablero_pad),
                                                Button(button_text='',
                                                       key='puntos_azul',
                                                       button_color=('White', 'Blue'),
                                                       size=boton_tablero_size,
                                                       pad=boton_tablero_pad),
                                                Button(button_text='',
                                                       key='puntos_amarillo',
                                                       button_color=('Black', 'Yellow'),
                                                       size=boton_tablero_size,
                                                       pad=boton_tablero_pad),
                                                Button(button_text='',
                                                       key='puntos_rojo',
                                                       button_color=('White', 'Red'),
                                                       size=boton_tablero_size,
                                                       pad=boton_tablero_pad),
                                                Button(button_text='',
                                                       key='puntos_gris',
                                                       button_color=('White', 'Grey'),
                                                       size=boton_tablero_size,
                                                       pad=boton_tablero_pad)]],
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
                                   key='terminar',
                                   pad=boton_opcion_size,
                                   image_filename=boton_opcion)]]
columna_de_juego_derecha = [[Column(layout=puntos,
                                    background_color=window_color)],
                            [Column(layout=frame_reglas,
                                    background_color=window_color)],
                            [Text(text='         T I E M P O: ',
                                  background_color=window_color),
                             Text(key='tiempo',
                                  size=text_segundos_size,
                                  background_color=window_color)],
                            [Column(layout=botones_de_opcion_juego,
                                    background_color=window_color)]]
layout_juego = [[Column(layout=tablero,
                        background_color=window_color),
                 Column(layout=columna_de_juego_derecha,
                        background_color=window_color)],
                [Column(layout=frame_letras,
                        background_color=window_color)]]
window_juego = Window(layout=layout_juego,
                      title='ScrabbleAR',
                      font=font_size,
                      margins=margins_size,
                      background_color=window_color)