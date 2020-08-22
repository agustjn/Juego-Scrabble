from mod_archivos import Archivos, partida_json
from mod_interfaz import Interfaz
from parametros import Parametros
from mod_popups import Popups
from mod_turno import Turno
from layout import *
from const import *
import mod_cpu as cpu
import json


class Main(Interfaz):

    def __init__(self):
        self._parametros = Parametros()
        Interfaz.__init__(self, self._parametros)
        self._turno = Turno(self._parametros)
        self._popups = Popups()
        self._archivos = Archivos()
        self._window = window_menu

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
                    self._parametros.set_tiempo_total(values['tiempo_total'])
                else:
                    self._parametros.set_dificultad(event)
                break
            #print(self._parametros.get_bolsa())
            if event is 'puntos_por_letra' and not self.puntos_por_letra(self._window):
                return False
            #print(self._parametros.get_bolsa())
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
                          'puntos_bot': self._parametros.get_puntos_bot(),
                          'historial': self._parametros.get_historial()},
                         self._parametros.get_atril_jugador(),
                         self._parametros.get_atril_bot(),
                         self._parametros.get_matriz())
        else:   # SI NO HAY PARTIDA GUARDADA, SOLO CARGA NUEVOS ATRILES
            self.repartir_fichas(self._parametros.get_atril_jugador(), self._window)
            self.repartir_fichas(self._parametros.get_atril_bot(), self._window)
        cant_letras_total, bolsa = 0, self._parametros.get_bolsa()
        for i in bolsa:
            cant_letras_total += bolsa[i]['cantidad']
        self._parametros.set_fichas(cant_letras_total)
        const_Update(self._window, # HAYA O NO PARTIDA GUARDADA, CARGA LOS PARÁMETROS GENÉRICOS COMO LAS REGLAS
                     {'reglas': reglas(self._parametros.get_dificultad(),
                                       self._parametros.get_tiempo_por_turno(),
                                       self._parametros.get_tiempo_total()),
                      'fichas_jugador': 'MIS FICHAS ~~~~~~ TOTAL DE FICHAS: '+str(cant_letras_total)},
                     color_botones[self._parametros.get_dificultad()],
                     puntos_botones[self._parametros.get_dificultad()]['jugador'])
        Interfaz.set_dificultad(self)   # SETEA LA DIFICULTAD A LA CLASE PUNTAJE (PADRE DE INTERFAZ)
        const_Update(self._window, {'tiempo': 'TIEMPO DE RONDA: '+str(self._parametros.get_segundos()), 'tiempo_total': 'TIEMPO TOTAL: '+str(self._parametros.get_contador_total()['minutos'])+':'+str(self._parametros.get_contador_total()['segundos']), 'turno': 'JUGADOR' if self._parametros.get_turno() else '       BOT'})


    def fin(self):
        if (self._parametros.get_puntos_jugador() > self._parametros.get_puntos_bot()): # GUARDA EL PUNTAJE COMO RECORD SI LOS PUNTOS FUERON MAYORES A LOS DEL BOT
            self._archivos.cargar_records_json(self._parametros.get_puntos_jugador(),
                                               self._parametros.get_dificultad())

    def juego(self):
        self.inicio()
        while True:
            event, values = self._window.Read(timeout=100)  # CADA 100 MILISEGUNDOS SALTA DEL .Read()
            self._turno.conteo(self._window)    # ACTUALIZA EL CONTEO EN PANTALLA MAS LAS VARIABLES CONTADORAS
            if self._parametros.get_contador_total()['minutos'] == 0 and self._parametros.get_contador_total()['segundos'] == 0:
                self._popups.popup('FIN DEL TIEMPO.')
                self.fin()
                break
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
                    if self._parametros.get_palabra():  # SI _palabra CONTIENE ELEMENTOS (SI PUSO LETRAS)
                        if not self.control_bolsa('jugador'):
                            if not self.primer_turno(): # ESTA FUNCION DETERMINA SI PERMANECEMOS EN EL PRIMER TURNO O NO. SI LA VARIABLE _primer_turno ES False NO ESTAMOS EN EL PRIMER TURNO, SI ES True, SI. SI _primer_turno ES False, LA FUNCIÓN REGULA SI SE PUSO O NO UNA LETRA EN E CENTRO PARA TERMINAR EL PRIMER TURNO O NO
                                if self.calcular_palabra(self._window, 'jugador'):  # CALCULA LA PALABRA
                                    self._parametros.actualizar_atril(self._window, 'jugador')
                                else:
                                    self._popups.popup('PALABRA INVALIDA')
                                    self.devolver_fichas(self._window, 'jugador')
                                self._turno.fin_de_turno(self._window)  # CAMBIA EL TURNO Y BORRA LAS LETRAS USADAS DE LA BOLSA
                            else: # SI ESTAMOS EN EL PRIMER TURNO
                                self.devolver_fichas(self._window, 'jugador')   # DEVUELVE LAS FICHAS PUESTAS EN LA MATRIZ HACIA EL ATRIL PORQUE SE UBICARON INCORRECTAMENTE
                                self._popups.popup('TURNO PERDIDO. NO INGRESÓ NINGUNA LETRA\nDE LA PALABRA EN EL CENTRO DEL TABLERO')   # NO SE INGRESÓ NINGUNA LETRA EN EL TROCEN
                                self._turno.fin_de_turno(self._window)
                            self._parametros.borrar_palabra()   # POR CADA TURNO LA BORRA (EN _palabra SOLO SE UBICAN LAS LETRAS POR TURNO)
                            self._parametros.set_letra_ficha('')
                        else:
                            self._popups.popup('NO ES POSIBLE REPONER FICHAS, FIN DEL JUEGO')
                            self.fin()
                            break
                    else:
                        self._turno.fin_de_turno(self._window)
                        self._parametros.set_letra_ficha('')
                    #print('aca llega', self._parametros.get_fichas())
                if event in atril_jugador:
                    self._parametros.set_ficha({event: self._window.Element(event).GetText()})  # GUARDA LA FICHA SELECCIONADA, LA SETEA EN _ficha
                if event in matriz and self._parametros.get_letra_ficha() != '' and self._window.Element(event).GetText() == '' and self.evaluar_posicion(self._window, event, self._parametros.get_palabra()):    # SI EL EVENTO ESTÁ EN LA MATRIZ Y SE SETEÓ ALGUNA FICHA (ES DECIR, NO ESTÁ VACÍA)
                    self.mover_ficha(self._window, event)   # MUEVE LA FICA DESDE EL ATRIL HASTA LA MATRIZ
                if event is 'cambiar_fichas':
                    if not self._parametros.get_palabra():  # SOLO SE PUEDEN CAMBIAR LAS FICHAS CUANDO NO SE HAYA PUESTO NINGUNA
                        if not self.control_bolsa('jugador'):
                            if self._parametros.get_cambiar_fichas_j() < 3:   # SI SE CAMBIÓ MÁS DE 3 VECES, PIERDE
                                self._parametros.add_cambiar_fichas_j()   # AUMENTA EL CONTADOR DE 'CAMBIAR FICHAS' (MÁXIMO 3, LLEGA A 3 Y PIERDE)
                                self.repartir_fichas(self._parametros.get_atril_jugador(), self._window)    # REPARTE 7 NUEVAS FICHAS
                                self._parametros.set_letra_ficha('')
                                self._turno.fin_de_turno(self._window)
                            else:
                                return self._popups.popup('HAS PERDIDO EL JUEGO\nSUPERASTE EL LIMITE DE CAMBIO DE FICHAS')   # EL RETURN ES SOLO PARA QUE SALGA DE 'juego()' Y ESTE TERMINE
                        else:
                            self._popups.popup('NO ES POSIBLE REPONER FICHAS, FIN DEL JUEGO')
                            break
                    else:
                        self._popups.popup('NO SE PUEDEN CAMBIAR FICHAS SI YA\nPUSO ALGUNA DURANTE EL TURNO')   # SI '_palabra' CONTIENE FICHAS, ES DECIR, PUSO ALGUNA LETRA, NO PUEDE CAMBIARLAS HASTA SU SIGUIENTE TURNO
            else:
                # TURNO DEL BOT:
                if self._parametros.limite_bot():
                    cpu.create_word(self._parametros._a_bot.values(), self._parametros._dificultad, self._parametros)
                    cpu.colocar_palabra_bot(self._window, self._parametros,self.calcular_palabra,self.repartir_fichas)
                else:
                    self._popups.popup('EL BOT HA PERDIDO DEBIDO A QUE SUPERO\nEL LIMITE DE CAMBIO DE FICHAS')
                    self.fin()
                    break
                if not self.control_bolsa('bot'):
                    self._parametros.actualizar_atril(self._window, 'bot')
                    self._turno.fin_de_turno(self._window)
                    self._parametros.borrar_palabra()
                else:
                    self._popups.popup('EL BOT NO PUDO REPONER FICHAS, GANASTE')
                    self.fin()
                    break
                #print('aca llega', self._parametros.get_fichas())

    def run(self):
        if self.menu():
            self._window.Close()
            self.juego()
        self._window.Close()


main = Main()
main.run()
