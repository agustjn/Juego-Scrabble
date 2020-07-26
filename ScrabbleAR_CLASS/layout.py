from PySimpleGUI import Window, Frame, Column, Button, Drop, Spin, Text, Listbox


boton_opcion = 'media/boton_opcion.png'
boton_salir = 'media/boton_salir.png'
window_color = '#1c1c1c'
spin_rango = [time for time in range(10, 41)]
spin_rango_total = [time for time in range(5, 16)]
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
rules_size = (18, 8)


# ~~~~~~~~~~~~~~~ Elementos del menú ~~~~~~~~~~~~~~~
botones_de_opcion_menu = [[Button(button_text='FÁCIL',
                                  key='FÁCIL',
                                  pad=(0, 6),
                                  image_filename=boton_opcion)],
                          [Button(button_text='MEDIO',
                                  key='MEDIO',
                                  pad=(0, 6),
                                  image_filename=boton_opcion)],
                          [Button(button_text='DIFICIL',
                                  key='DIFICIL',
                                  pad=(0, 6),
                                  image_filename=boton_opcion)],
                          [Button(button_text='CARGAR PARTIDA',
                                  key='cargar_partida',
                                  pad=(0, 6),
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
                             [Text(text='TIEMPO TOTAL          ',
                                   background_color=window_color),
                              Spin(values=spin_rango_total,
                                   key='tiempo_total')],
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
window_menu = Window(title='ScrabbleAR',
                     font=font_size,
                     margins=margins_size,
                     background_color=window_color).Layout(layout_menu)


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
                      button_color=('Red',  'Red'),#button_color=('White',  'White'),
                      size=boton_tablero_size,
                      image_data='iVBORw0KGgoAAAANSUhEUgAAAB8AAAAaCAIAAADAARDdAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADuSURBVEhLpY3RFYQgEAMtxE/778we7iA6hhVUYJ6PS3azuWVft2VJr76/nudqo/QazVH0FOa00r1QpYb0+ij50T/wBuyl+IrdN+632IMwdf2MJ9GyBWHnugoBZVzXIUHItUNMW9dPkCONAN/e7Tsc6OZVy3YQLt2GSY73w70qWnocWlTEy2QW7+JlMg4tKmrpEbhXhdswyfEeuNSxWz6f56NvcKMz1yJMgm1Cjqhrh5i2ruuQUMh1FQLKuI6w09r1A8SUdH3BVAvXrxBWvrBukj/X+bADb8A2pkNQpYb0ukEPQ8nRo59iNAdV+7r9AJ5KYMzAUVISAAAAAElFTkSuQmCC',
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
                       pad=frame_size,
                       title_color='white'),
                 Frame(layout=[[Column(layout=letras_bot,
                                       background_color=window_color)]],
                       title='SUS FICHAS',
                       key='fichas_bot',
                       background_color=window_color,
                       pad=frame_size,title_color='white')]]
puntos = [[Text(text='MIS PUNTOS: ',
                size=text_puntos_de_quien_size,
                background_color=window_color,text_color='white'),
           Text(text='0',
                key='puntos_jugador',
                size=text_puntos_size,
                background_color=window_color,text_color='white')],
          [Text(text='SUS PUNTOS: ',
                size=text_puntos_de_quien_size,
                background_color=window_color,text_color='white'),
           Text(text='0',
                key='puntos_bot',
                size=text_puntos_size,
                background_color=window_color,text_color='white')]]
frame_reglas = [[Frame(layout=[[Column(layout=[[Text(text='',
                                                     key='reglas',
                                                     size=rules_size,
                                                     pad=(0, 0),
                                                     background_color=window_color,
                                                     text_color='white')]],
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
                       background_color=window_color,
                       title_color='white')]]
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
                                   image_filename=boton_opcion)],
                           [Text(text='', size=(4, 1), background_color=window_color),
                            Frame(title='TURNO',
                                  pad=(0, 0),
                                  layout=[[Text(text='',
                                                key='turno',
                                                font=24,
                                                size=(9, 1),
                                                text_color='White',
                                                background_color=window_color)]],
                                  background_color=window_color,title_color='white')]]
columna_de_juego_derecha = [[Column(layout=puntos,
                                    background_color=window_color)],
                            [Column(layout=frame_reglas,
                                    background_color=window_color)],
                            [Column(layout=botones_de_opcion_juego,
                                    background_color=window_color)]]
historial = [[Listbox(values=[],
                      key='historial',
                      size=(20, 26),
                      text_color='Black',
                      background_color='White')]]
frame_historial = [[Frame(title='HISTORIAL',
                          layout=historial,
                          pad=(2, 1),
                          background_color=window_color,title_color='white')]]
columna_tablero = [[Column(layout=tablero,
                           background_color=window_color),
                    Column(layout=columna_de_juego_derecha,
                           background_color=window_color)],
                   [Column(layout=frame_letras,
                           background_color=window_color)]]
puntos = [[Text(text='',
                size=(20, 1),
                font=24,
                text_color='White',
                key='tiempo',
                background_color=window_color),
           Text(text='',
                size=(20, 1),
                font=24,
                text_color='White',
                key='tiempo_total',
                background_color=window_color)]]
layout_juego = [[Frame(title='TIEMPOS',
                       layout=puntos,
                       background_color=window_color,
                       title_color='white'),
                 Text(text='Grupo 24: Leidi Agustin, Rodriguez Sandoval Felix, Diz Rendani Matias.',
                      text_color='White',
                      background_color=window_color)],
                [Column(layout=frame_historial,
                        background_color=window_color),
                 Column(layout=columna_tablero,
                        background_color=window_color)]]
window_juego = Window(title='ScrabbleAR',
                      font=font_size,
                      margins=margins_size,
                      background_color=window_color).Layout(layout_juego)
