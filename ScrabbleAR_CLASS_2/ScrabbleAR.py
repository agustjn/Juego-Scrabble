from mod_archivos import Archivos, partida_json
from mod_interfaz import Interfaz
from parametros import Parametros
from mod_popups import Popups
from mod_turno import Turno
from layout import *
from const import *
# from Modulo_Jugador import Jugador
import json


# Hay algunos errores que arreglar
class Main(Interfaz):

    def __init__(self):
        self._parametros = Parametros()
        Interfaz.__init__(self, self._parametros)
        self._turno = Turno(self._parametros)
        self._popups = Popups()
        self._archivos = Archivos()
        self._window = window_menu
        self._ficha = ''

    def menu(self):
        while True:
            event, values = self._window.Read()
            if event in ('salir', None):
                return False
            if event in ('FÁCIL', 'MEDIO', 'DIFICIL', 'personalizado'):
                if event is 'personalizado':
                    self._parametros.set_dificultad(values['dificultad'])
                    self._parametros.set_tiempo_por_turno(values['tiempo_por_turno'])
                    self._parametros.set_segundos(values['tiempo_por_turno'])
                else:
                    self._parametros.set_dificultad(event)
                break
            if event is 'cargar_partida':
                partida = self._archivos.leer_json(partida_json)
                if not partida:
                    self._popups.popup('NO HAY PARTIDA GUARDADA')
                else:
                    self._parametros.cargar_parametros(partida)
                    break
        return True

    def inicio(self):
        # Carga la partida guardada si se quizo desde el menú,
        # sino, solo carga los parametros generales.
        self._window = window_juego.Finalize()
        if self._parametros.get_hay_partida():
            const_Update(self._window,
                         {'puntos_jugador': self._parametros.get_puntos_jugador(),
                          'puntos_bot': self._parametros.get_puntos_bot()},
                         self._parametros.get_atril_jugador(),
                         self._parametros.get_atril_bot(),
                         self._parametros.get_matriz())
        else:
            self.repartir_fichas(self._parametros.get_atril_jugador(), self._window)
            self.repartir_fichas(self._parametros.get_atril_bot(), self._window)
            const_Update(self._window, {('jugador', 0): 'A'})
        const_Update(self._window,
                     {'reglas': reglas(self._parametros.get_dificultad(),
                                       self._parametros.get_tiempo_por_turno()),
                      'fichas_jugador': 'MIS FICHAS~~~~~~~TOTAL DE FICHAS: '+str(self._parametros.get_fichas())},
                     color_botones[self._parametros.get_dificultad()],
                     puntos_botones[self._parametros.get_dificultad()]['jugador'])
        Interfaz.set_dificultad(self)

    def fin(self):
        if (self._parametros.get_puntos_jugador() > self._parametros.get_puntos_bot()):
            self._archivos.cargar_records_json(self._parametros.get_puntos_jugador(),
                                               self._parametros.get_dificultad())

    def juego(self):
        while True:
            event, values = self._window.Read(timeout=100)
            self._turno.conteo(self._window)
            const_Update(self._window, {'tiempo': self._parametros.get_segundos()})
            if event in ('terminar', None):
                self.fin()
                break
            if event is 'guardar_partida':
                self._popups.popup('PARTIDA GUARDADA')
                self._archivos.escribir_json(self._parametros.guardar_parametros(), partida_json, 'w')
            if event is 'top_diez':
                self._popups.popup_scrolled(self._archivos.cargar_records_txt())
            if self._parametros.get_turno():
                # TURNO DEL USUARIO:
                if ((event is 'fin_de_turno') or (self._parametros.get_segundos() == 0)):
                    self._turno.fin_de_turno()
                    self.calcular_palabra(self._window, 'jugador')
                    self._parametros.borrar_palabra()
                if event in atril_jugador:
                    self._parametros.set_ficha({event: self._window.Element(event).GetText()})
                if ((event in matriz) & (self._parametros.get_letra_ficha() != '')):
                    self.mover_ficha(self._window, event)
                if event is 'cambiar_fichas':
                    self.repartir_fichas(self._parametros.get_atril_jugador(), self._window)
            else:
                # TURNO DEL BOT:
                # if self._parametros.get_segundos() == 0:
                #     self._turno.fin_de_turno()
                #     self.calcular_palabra(self._window, 'bot')
                #     self._parametros.borrar_palabra()
                self._turno.fin_de_turno()

    def run(self):
        if self.menu():
            self._window.Close()
            self.inicio()
            self.juego()
        self._window.Close()


main = Main()
main.run()
