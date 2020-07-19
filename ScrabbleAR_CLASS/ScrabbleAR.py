from mod_archivos import Archivos, partida_json
from mod_interfaz import Interfaz
from parametros import Parametros
from mod_popups import Popups
from mod_turno import Turno
from layout import *
from const import *
import json


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
        self._window = window_juego.Finalize()
        if self._parametros.get_hay_partida():  # PREGUNTA SI HAY PARTIDA
            const_Update(self._window, # SI HAY PARTIDA GUARDADA, ACTUALIZA LA VENTANA CON LOS PARÁMETROS GUARDADOS
                         {'puntos_jugador': self._parametros.get_puntos_jugador(),
                          'puntos_bot': self._parametros.get_puntos_bot()},
                         self._parametros.get_atril_jugador(),
                         self._parametros.get_atril_bot(),
                         self._parametros.get_matriz())
        else:   # SI NO HAY PARTIDA GUARDADA, SOLO CARGA NUEVOS ATRILES
            self.repartir_fichas(self._parametros.get_atril_jugador(), self._window)
            self.repartir_fichas(self._parametros.get_atril_bot(), self._window)
        const_Update(self._window, # HAYA O NO PARTIDA GUARDADA, CARGA LOS PARÁMETROS GENÉRICOS COMO LAS REGLAS
                     {'reglas': reglas(self._parametros.get_dificultad(),
                                       self._parametros.get_tiempo_por_turno()),
                      'fichas_jugador': 'MIS FICHAS ~~~~~~ TOTAL DE FICHAS: '+str(self._parametros.get_fichas())},
                     color_botones[self._parametros.get_dificultad()],
                     puntos_botones[self._parametros.get_dificultad()]['jugador'])
        Interfaz.set_dificultad(self)   # SETEA LA DIFICULTAD A LA CLASE PUNTAJE (PADRE DE INTERFAZ)

    def fin(self):
        if (self._parametros.get_puntos_jugador() > self._parametros.get_puntos_bot()): # GUARDA EL PUNTAJE COMO RECORD SI LOS PUNTOS FUERON MAYORES A LOS DEL BOT
            self._archivos.cargar_records_json(self._parametros.get_puntos_jugador(),
                                               self._parametros.get_dificultad())

    def juego(self):
        self.inicio()
        if self._parametros.get_matriz():   # SI LA MATRIZ NO ESTÁ VACÍA, NIEGA LA VARIABLE _primer_turno
            self._parametros.set_primer_turno()
        while True:
            event, values = self._window.Read(timeout=100)  # CADA 100 MILISEGUNDOS SALTA DEL .Read()
            self._turno.conteo(self._window)    # ACTUALIZA EL CONTEO EN PANTALLA MAS LAS VARIABLES CONTADORAS
            const_Update(self._window, {'tiempo': self._parametros.get_segundos()})
            if event in ('terminar', None):
                self.fin()
                break
            if event is 'guardar_partida':  # ESCRIBE EN 'partida_json' LOS PARÁMETROS DE LA PARTIDA EN JUEGO
                self._popups.popup('PARTIDA GUARDADA')
                self._archivos.escribir_json(self._parametros.guardar_parametros(), partida_json, 'w')
            if event is 'top_diez':
                self._popups.popup_scrolled(self._archivos.cargar_records_txt())
            if self._parametros.get_turno():
                # TURNO DEL USUARIO:
                if ((event is 'fin_de_turno') or (self._parametros.get_segundos() == 0)):   # SI CLICKEA EN FIN DE TURNO O SE LE TERMINA EL TIEMPO
                    self._turno.fin_de_turno()  # CAMBIA EL TURNO (DEL JUGADOR AL BOT)
                    if not self.primer_turno(): # SI NO ESTAMOS EN EL PRIMER TURNO
                        if self._parametros.get_palabra():  # SI _palabra ESTÁ VACÍA (SI NO PUSO LETRAS)
                            self.calcular_palabra(self._window, 'jugador')  # CALCULA LA PALABRA
                            self._parametros.borrar_palabra()   # POR CADA TURNO LA BORRA (EN _palabra SOLO SE UBICAN LAS LETRAS POR TURNO)
                    elif self._parametros.get_matriz(): # SI ESTAMOS EN EL PRIMER TURNO Y LA MATRIZ NO ESTÁ VACÍA (SE UBICARON LETRAS)
                        self.devolver_fichas(self._window, 'jugador')   # DEVUELVE LAS FICHAS PORQUE SE UBICARON INCORRECTAMENTE (YA QUE NO SE SETEÓ _primer_turno EN FALSO)
                if event in atril_jugador:
                    self._parametros.set_ficha({event: self._window.Element(event).GetText()})  # GUARDA LA FICHA SELECCIONADA, LA SETEA EN _ficha
                if ((event in matriz) & (self._parametros.get_letra_ficha() != '')):    # SI EL EVENTO ESTÁ EN LA MATRIZ Y SE SETEÓ ALGUNA FICHA (ES DECIR, NO ESTÁ VACÍA)
                    self.mover_ficha(self._window, event)   # MUEVE LA FICA DESDE EL ATRIL HASTA LA MATRIZ
                if event is 'cambiar_fichas':
                    self.repartir_fichas(self._parametros.get_atril_jugador(), self._window)    # REPARTE NUEVAS FICHAS
            else:
                # TURNO DEL BOT:
                # if self._parametros.get_segundos() == 0:
                #   self._turno.fin_de_turno()
                #   if not self.primer_turno():
                #       if self._parametros.get_palabra():
                #           self.calcular_palabra(self._window, 'bot')
                #           self._parametros.borrar_palabra()
                # elif self._parametros.get_matriz():
                #   self.devolver_fichas(self._window, 'bot')
                self._turno.fin_de_turno()

    def run(self):
        if self.menu():
            self._window.Close()
            self.juego()
        self._window.Close()


main = Main()
main.run()
