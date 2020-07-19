from const import puntos_botones, color_botones, bolsa


class Puntaje:

    def __init__(self):
        self._dificultad = ''

    def _set_dificultad(self, dificultad):
        self._dificultad = dificultad

    def _calcular_palabra(self, quien, palabra):
        ''' CALCULA Y DEVUELVE EL PUNTAJE DE LA PALABRA ENTRANTE
            SEGÚN EL COLOR DEL BOTÓN Y LA PUNTUACIÓN DE LA LETRA.'''
        if palabra == '':
            return 0
        puntos, color = 0, ''
        for key in palabra:
            for colores in color_botones[self._dificultad]:
                if key in color_botones[self._dificultad][colores]:
                    color = colores[1]
                    break
            puntos += self._sumar(color, bolsa[palabra[key]]['puntaje'], quien)
        return puntos

    def _sumar(self, color, puntaje_letra, quien):
        ''' DEVUELVE LA SUMA DE LA PUNTUACIÓN DE LA LETRA POR EL COLOR'''
        if color == 'Red':
            return - int(puntos_botones[self._dificultad][quien]['puntos_rojo'][-1:])
        elif color == 'Green':
            return puntaje_letra*int(puntos_botones[self._dificultad][quien]['puntos_verde'][-1:])
        elif color == 'Blue':
            return puntaje_letra+int(puntos_botones[self._dificultad][quien]['puntos_azul'][-1:])
        elif color == 'Yellow':
            return puntaje_letra+int(puntos_botones[self._dificultad][quien]['puntos_amarillo'][-1:])
        elif color == 'Grey':
            return puntaje_letra+int(puntos_botones[self._dificultad][quien]['puntos_gris'][-1:])
