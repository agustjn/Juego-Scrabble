from const import puntos_medio
from const import puntos_dificil
from const import puntos_por_color


class Puntaje:

    def __init__(self, puntaje_inicial=0,dificultad='FÁCIL'):
        self._puntos = puntaje_inicial
        self._dificultad=dificultad

    def get_puntos(self):
        return self._puntos

    def set_puntos(self, puntaje):
        self._puntos = puntaje

    def get_dificultad(self):
        return self._dificultad

    def set_dificultad(self, dificultad):
        self._dificultad = dificultad

    def sumar(self, color,puntaje_letra):
        if color is 'red':
            self._puntos -= int(puntos_por_color[self._dificultad]['jugador']['puntos_rojo'][-1:])
        elif color is 'green':
            self._puntos+=puntaje_letra*int(puntos_por_color[self._dificultad]['jugador']['puntos_verde'][-1:])
        elif color is 'blue':
            self._puntos += puntaje_letra+int(puntos_por_color[self._dificultad]['jugador']['puntos_azul'][-1:])
        elif color is 'yellow':
            self._puntos += puntaje_letra+int(puntos_por_color[self._dificultad]['jugador']['puntos_amarillo'][-1:])
        elif color is '':
            self._puntos += puntaje_letra+int(puntos_por_color[self._dificultad]['jugador']['puntos_gris'][-1:])
