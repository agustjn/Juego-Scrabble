from PySimpleGUI import Window, Popup, Frame, Column, Button, Drop, Spin, Text
from Modulo_Archivos import Archivos
from Modulo_Interfaz import Interfaz
from Modulo_Puntos import Puntos
from const import *


class Main():
    def __init__(self):
        self._archivos = Archivos(enlaces_json)
        self._window = Interfaz()
        self._parametros_tablero = parametros
        self._puntos_jugador = Puntos(0)
        self._puntos_bot = Puntos(0)

    def run(self):
        if self.menu():
            self.juego()

    def menu(self):
        self._window.set_menu_window()
        while True:
            event, values = self._window.get_window().Read()
            if event in ('salir', None):
                return False
            if event in ('FÁCIL', 'MEDIO', 'DIFICIL', 'personalizado'):
                if event is 'personalizado':
                    self._parametros_tablero['dificultad'] = values['dificultad_personalizada']
                else:
                    self._parametros_tablero['dificultad'] = event
                break
            if event is 'cargar_partida':
                self._parametros_tablero = self._archivos.leer_json(juego_guardado_json)
                if not self._parametros_tablero:
                    self._window.mensaje('NO HAY PARTIDA GUARDADA')
                    self._parametros_tablero = parametros
                else:
                    break
        self._window.cerrar()
        return True

    def juego(self):
        self._window.set_tablero_window()
        self._window.cargar_parametros(self._parametros_tablero)
        self._window.definir_puntaje(self._parametros_tablero['dificultad'])
        while True:
            event, values = self._window.get_window().Read()
            if event in ('salir', None):
                break
            if event is 'guardar_partida':
                self._archivos.escribir_json(self._window.guardar_parametros(self._parametros_tablero['dificultad']), juego_guardado_json, 'w')
                self._window.mensaje('PARTIDA GUARDADA')
            if event is 'top_diez':
                if not self._archivos.ver_top_diez():
                    self._window.mensaje('NO HAY RECORDS')
        self._archivos.cargar_record(self._parametros_tablero['dificultad'])
        self._window.cerrar()


ScrabbleAR = Main()
ScrabbleAR.run()
