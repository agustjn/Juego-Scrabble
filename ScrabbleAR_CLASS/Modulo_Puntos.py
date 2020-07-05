from const import puntos_facil
from const import puntos_medio
from const import puntos_dificil
from const import puntos_por_color
import random


class Puntaje:
    _dificultad = ''

    def __init__(self, puntaje_inicial):
        self._puntos = 0

    def get_puntos(self):
        return (self.puntos)

    def set_puntos(self, puntaje):
        self._puntos = puntaje

    def get_dificultad(self):
        return self._dificultad

    def set_dificultad(self, dificultad):
        self._dificultad = dificultad

    def sumar(self, color):
        if color is 'rojo':
            self._puntos -= int(puntos_por_color[self._dificultad]['jugador']['puntos_rojo'][-1:])
        elif color is 'verde':
            self._puntos *= int(puntos_por_color[self._dificultad]['jugador']['puntos_verde'][-1:])
        elif color is 'azul':
            self._puntos += int(puntos_por_color[self._dificultad]['jugador']['puntos_azul'][-1:])
        elif color is 'amarillo':
            self._puntos += int(puntos_por_color[self._dificultad]['jugador']['puntos_amarillo'][-1:])
        elif color is 'grey':
            self._puntos += int(puntos_por_color[self._dificultad]['jugador']['puntos_gris'][-1:])
