from PySimpleGUI import Window, Frame, Column, Button, Drop, Spin, Text, Listbox, InputText


boton_opcion = 'iVBORw0KGgoAAAANSUhEUgAAAJUAAAAVCAYAAABPEqyXAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsIAAA7CARUoSoAAAABVSURBVGhD7dIxAcAwDMCwdIDCn137DIJP6TEBn929A6HvL2RMRc5U5ExFzlTkTEXOVORMRc5U5ExFzlTkTEXOVORMRc5U5ExFzlTkTEXOVORMRWzmAWM4AbPo5MpQAAAAAElFTkSuQmCC'
boton_opcion_L = 'iVBORw0KGgoAAAANSUhEUgAAAKQAAAAVCAYAAADII0WRAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAABXSURBVGhD7dIxAcAwDMCwdIDCn137DIQP6TEBn929AxHfX0gwJCmGJMWQpBiSFEOSYkhSDEmKIUkxJCmGJMWQpBiSFEOSYkhSDEmKIUkxJCmGJMWQhMw8XkQBsw98HPIAAAAASUVORK5CYII='
boton_salir = 'iVBORw0KGgoAAAANSUhEUgAAAZMAAAAUCAYAAABI3tC1AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsIAAA7CARUoSoAAAAJwSURBVHhe7dxZjiIxDIBheh44Dtz/GFyHl2kslTWWJ0ulcJJa/k+KGqqctRyCeOifx+Px9wYAwBf+LH8BANiMwwRAN6/Xa3lV1ysWY/Azl5FL0OfzubyKIf0coU0V0faotc0Z+WxLes939jp7LbnTK7ZkTTt7W9O94jBZlJIqKnGFthXZpohuz4poO9dGz3Fbpf5F1BhGzSel1PescbX02ys2R9uotZW7HzGGM+Fnro9aUpAw/cjayvrPIv3PHkMEcni8M+RNJA6TgWobHsAY7MV4HCaT8K1mX674PGS+vlj2vb+v720p6RVrba3HXozBYfJBMuHoWnNYYqWOL57E2Vhl6+j1XP+pviJira31EIfDZKHJpyWaJrt19YTXtfbrcnQ6L196W5vDLWORNtc8n1JM6p6O1WuJVXKvpV4qvtaHJ7G5fq+Kw8SQxNCiydKSYCizaypF1/psbB7ZMoLtz661N2o8Z2HXUoquMf7hMMmwyZLajC20vk1GLXr9CnRN2YRjROawZ3NYy0yp8Ujx9JqPs9dTyN06DpOKqOSxyegL0FN0jskHrs/h6D5apcajxUvFaMF2HCad6cYrkfu5b0Rntbc5r3lOOLaovXjF/boGh8mB3O/35dU5sCnnmb3uLf3v8cOd3P0fh8lHKSnkniTOHrzf7+XVeczelNL3np7xVi053GOutf5TUuNoiZ1NxlSa99Xwv7kWPZJY2myp3xpv1ZJ65DxSSm3o2L/toyS3PtF99nwONa1zTMXbWLm/tq7EpeL1Wire2xJr+XpK20y1k2PjS3W1z5a2z4rDBADwNX7mAgB8jcMEAPCl2+0XoIZVxtxGR/wAAAAASUVORK5CYII='
boton_bot = 'iVBORw0KGgoAAAANSUhEUgAAAB8AAAAaCAIAAADAARDdAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADuSURBVEhLpY3RFYQgEAMtxE/778we7iA6hhVUYJ6PS3azuWVft2VJr76/nudqo/QazVH0FOa00r1QpYb0+ij50T/wBuyl+IrdN+632IMwdf2MJ9GyBWHnugoBZVzXIUHItUNMW9dPkCONAN/e7Tsc6OZVy3YQLt2GSY73w70qWnocWlTEy2QW7+JlMg4tKmrpEbhXhdswyfEeuNSxWz6f56NvcKMz1yJMgm1Cjqhrh5i2ruuQUMh1FQLKuI6w09r1A8SUdH3BVAvXrxBWvrBukj/X+bADb8A2pkNQpYb0ukEPQ8nRo59iNAdV+7r9AJ5KYMzAUVISAAAAAElFTkSuQmCC'
window_color = '#1c1c1c'
spin_rango = [time for time in range(10, 41)]
spin_rango_total = [time for time in range(5, 16)]
boton_opcion_size = (23, 5)
boton_tablero_size = (3, 1)
boton_tablero_pad = (0, 0)
text_puntos_de_quien_size = (12, 1)
text_segundos_size = (2, 1)
text_puntos_size = (4, 1)
size_text_letras = (12, 1)
size_text_puntos = (2, 1)
text_puntos_por_boton = (14, 1)
text_size = (16, 1)
frame_size = (10, 0)
frame_padd = (0, 0)
column_pad = (0, 0)
margins_size = (0, 0)
font_size = 24
fichas_pad = (6, 0)
opciones_menu_pad = (0, 10)
drop_size = (6, 1)
rules_size = (18, 8)


# ~~~~~~~~~~~~~~~ Elementos del menú ~~~~~~~~~~~~~~~
botones_de_opcion_menu = [[Button(button_text='FÁCIL',
                                  key='FÁCIL',
                                  pad=opciones_menu_pad,
                                  image_data=boton_opcion)],
                          [Button(button_text='MEDIO',
                                  key='MEDIO',
                                  pad=opciones_menu_pad,
                                  image_data=boton_opcion)],
                          [Button(button_text='DIFICIL',
                                  key='DIFICIL',
                                  pad=opciones_menu_pad,
                                  image_data=boton_opcion)],
                          [Button(button_text='CARGAR PARTIDA',
                                  key='cargar_partida',
                                  pad=opciones_menu_pad,
                                  image_data=boton_opcion)]]
frame_menu = [[Frame(layout=[[Text(text='DIFICULTAD    ',
                                   background_color=window_color,text_color='white'),
                              Drop(values=['FÁCIL', 'MEDIO', 'DIFICIL'],
                                   default_value='FÁCIL',
                                   key='dificultad',
                                   size=drop_size)],
                             [Text(text='TIEMPO DE TURNO',
                                   background_color=window_color,text_color='white'),
                              Spin(values=spin_rango,initial_value=10,
                                   key='tiempo_por_turno')],
                             [Text(text='TIEMPO TOTAL          ',
                                   background_color=window_color,text_color='white'),
                              Spin(values=spin_rango_total,initial_value=5,
                                   key='tiempo_total')],
                             [Button(button_text='CONFIG DE LETRAS',
                                     key='puntos_por_letra',
                                     pad=(18, 3),
                                     image_data=boton_opcion_L)],
                             [Button(button_text='ACEPTAR',
                                     key='personalizado',
                                     pad=(18, 3),
                                     image_data=boton_opcion_L)]],
                     title='PERZONALIZADO',
                     background_color=window_color,title_color='white')]]
columna_menu = [[Column(layout=botones_de_opcion_menu,
                        background_color=window_color),
                 Column(layout=frame_menu,
                        background_color=window_color)]]
layout_menu = [[Frame(layout=columna_menu,
                      title='INICIAR',
                      background_color=window_color,title_color='white')],
               [Button(button_text='',
                       key='salir',
                       image_data=boton_salir)]]
window_menu = Window(title='ScrabbleAR',
                     font=font_size,
                     margins=margins_size,
                     background_color=window_color).Layout(layout_menu)
puntos_por_letra = [[Text('       INGRESE LAS LETRAS EN LOS\n       CAMPOS DE PUNTAJE DESEADOS', size=(32, 2), font=font_size, background_color=window_color,text_color='white')],
                    [Text('1:', size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'), InputText(default_text='', size=size_text_letras, font=font_size, key='input_1'), Text('2:', size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'), InputText(default_text='', size=size_text_letras, font=font_size, key='input_2')],
                    [Text('3:', size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'), InputText(default_text='', size=size_text_letras, font=font_size, key='input_3'), Text('4:', size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'), InputText(default_text='', size=size_text_letras, font=font_size, key='input_4')],
                    [Text('5:', size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'), InputText(default_text='', size=size_text_letras, font=font_size, key='input_5'), Text('6:', size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'), InputText(default_text='', size=size_text_letras, font=font_size, key='input_6')],
                    [Text('7:', size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'), InputText(default_text='', size=size_text_letras, font=font_size, key='input_7'), Text('8:', size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'), InputText(default_text='', size=size_text_letras, font=font_size, key='input_8')],
                    [Text('9:', size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'), InputText(default_text='', size=size_text_letras, font=font_size, key='input_9'), Text('10:',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'), InputText(default_text='', size=size_text_letras, font=font_size, key='input_10')],
                    [Text('       INGRESE LAS LETRAS Y SU \n       CANTIDAD PARA LA BOLSA', size=(32, 2), font=font_size, background_color=window_color,text_color='white')],
                    [Text('Letras:',size=(6,1), font=font_size, background_color=window_color,text_color='white'),InputText(default_text='', size=size_text_letras, font=font_size, key='input_letras'),Text('Cantidad:',size=(8,1), font=font_size, background_color=window_color,text_color='white'),InputText(default_text='', size=(3,1), font=font_size, key='spin')],
                    [Button(button_text='ACEPTAR', key='puntos_personalizados', image_data=boton_opcion),Button(button_text='APLICAR', key='cantidad_letras', image_data=boton_opcion)]]
columna_letras_bolsa_1 = [
        [Text('A',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('9',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_A')],
        [Text('B',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('2',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_B')],
        [Text('C',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('4',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_C')],
        [Text('D',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('4',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_D')],
        [Text('E',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('2',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_E')],
        [Text('F',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('2',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_F')],
        [Text('G',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('2',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_G')]        


]

columna_letras_bolsa_2 = [

        [Text('H',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('2',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_H')],
        [Text('I',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('6',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_I')],
        [Text('J',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('2',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_J')],
        [Text('K',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('1',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_K')],
        [Text('L',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('4',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_L')],
        [Text('M',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('3',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_M')],
        [Text('N',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('5',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_N')]
]


columna_letras_bolsa_3= [
        [Text('Ñ',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('1',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_Ñ')],
        [Text('O',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('8',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_O')],
        [Text('P',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('2',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_P')],
        [Text('Q',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('1',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_Q')],
        [Text('R',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('4',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_R')],
        [Text('S',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('7',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_S')],
        [Text('T',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('4',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_T')]

]

columna_letras_bolsa_4 = [
        [Text('U',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('6',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_U')],
        [Text('V',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('2',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_V')],
        [Text('W',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('2',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_W')],
        [Text('X',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('2',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_X')],
        [Text('Y',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('2',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_Y')],
        [Text('Z',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white'),Text('2',size=size_text_puntos, font=font_size, background_color=window_color,text_color='white',key='letter_Z')]
]

columna_aux = [
        [Text(' CANTIDAD DE LETRAS\n EN LA BOLSA',size=(32,2), font=font_size, background_color=window_color,text_color='white')],
        [Column(layout=columna_letras_bolsa_1,background_color=window_color),Column(layout=columna_letras_bolsa_2,background_color=window_color),Column(layout=columna_letras_bolsa_3,background_color=window_color),Column(layout=columna_letras_bolsa_4,background_color=window_color)]
]
layout_puntos_por_letra = [[Column(layout=puntos_por_letra, background_color=window_color),Column(columna_aux,background_color=window_color)]]


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
                      button_color=('Red',  'Red'),#button_color=('White',  'White')
                      size=boton_tablero_size,
                      image_data=boton_bot,
                      pad=fichas_pad,) for y in range(7)]]
frame_letras = [[Frame(layout=[[Column(layout=letras_jugador,
                                       background_color=window_color)],
                               [Button(button_text='CAMBIAR FICHAS',
                                       key='cambiar_fichas',
                                       image_data=boton_opcion),
                                Button(button_text='FIN DE TURNO',
                                       key='fin_de_turno',
                                       image_data=boton_opcion)]],
                       title='MIS FICHAS -- TOTAL DE FICHAS: ',
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
                                   image_data=boton_opcion)],
                           [Button(button_text='POSPONER',
                                   key='guardar_partida',
                                   pad=boton_opcion_size,
                                   image_data=boton_opcion)],
                           [Button(button_text='TERMINAR',
                                   key='terminar',
                                   pad=boton_opcion_size,
                                   image_data=boton_opcion)],
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
