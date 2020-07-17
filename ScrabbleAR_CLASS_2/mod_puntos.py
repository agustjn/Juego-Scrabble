from const import puntos_botones, color_botones, bolsa


class Puntaje:

    def __init__(self):
        self._dificultad = ''

    def _set_dificultad(self, dificultad):
        self._dificultad = dificultad

    def _calcular_palabra(self, quien, palabra):
        ''' CALCULA Y DEVUELVE EL PUNTAJE DE LA PALABRA ENTRANTE
            SEGÚN EL COLOR DEL BOTÓN Y LA PUNTUACIÓN DE LA LETRA.'''
        if palabra is None:     
            return 0
        puntos, color = 0, ''
        if quien == 'jugador':
            for key in palabra:
                for colores in color_botones[self._dificultad]:
                    if key in color_botones[self._dificultad][colores]:
                        color = colores[1]
                        break
                puntos += self._sumar_jugador(color, bolsa[palabra[key]]['puntaje'])
            return puntos
        elif quien == 'bot':
            for key in palabra:
                for colores in color_botones[self._dificultad]:
                    if key in color_botones[self._dificultad][colores]:
                        color = colores[1]
                        break
                puntos += self._sumar_bot(color, bolsa[palabra[key]]['puntaje'])
            return puntos

    def _sumar_jugador(self, color, puntaje_letra):
        ''' DEVUELVE LA SUMA DE LA PUNTUACIÓN DE LA LETRA POR EL COLOR'''
        if color == 'Red':
            return - int(puntos_botones[self._dificultad]['jugador']['puntos_rojo'][-1:])
        elif color == 'Green':
            return puntaje_letra*int(puntos_botones[self._dificultad]['jugador']['puntos_verde'][-1:])
        elif color == 'Blue':
            return puntaje_letra+int(puntos_botones[self._dificultad]['jugador']['puntos_azul'][-1:])
        elif color == 'Yellow':
            return puntaje_letra+int(puntos_botones[self._dificultad]['jugador']['puntos_amarillo'][-1:])
        elif color == 'Grey':
            return puntaje_letra+int(puntos_botones[self._dificultad]['jugador']['puntos_gris'][-1:])

    def _sumar_bot(self, color, puntaje_letra):
        ''' DEVUELVE LA SUMA DE LA PUNTUACIÓN DE LA LETRA POR EL COLOR'''
        if color == 'Red':
            return - int(puntos_botones[self._dificultad]['bot']['puntos_rojo'][-1:])
        elif color == 'Green':
            return puntaje_letra*int(puntos_botones[self._dificultad]['bot']['puntos_verde'][-1:])
        elif color == 'Blue':
            return puntaje_letra+int(puntos_botones[self._dificultad]['bot']['puntos_azul'][-1:])
        elif color == 'Yellow':
            return puntaje_letra+int(puntos_botones[self._dificultad]['bot']['puntos_amarillo'][-1:])
        elif color == 'Grey':
            return puntaje_letra+int(puntos_botones[self._dificultad]['bot']['puntos_gris'][-1:])
