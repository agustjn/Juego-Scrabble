from PySimpleGUI import Window, Popup, Frame, Column, Button, Drop, Spin, Text
from Modulo_Archivos import Archivos
from Modulo_Interfaz import Interfaz
from Modulo_Puntos import Puntaje
from Modulo_Player import Jugador#,Bot #FALTA CLASE BO
from const import *
from Modulo_Matriz import Matriz


class Main():
    def __init__(self):
        self._archivos = Archivos(enlaces_json)
        self._interfaz = Interfaz()
        self._parametros_tablero = parametros
        self._jugador1 = Jugador()
        self._bot = Jugador()#Bot() #Clase que deriva a la clase Jugador()
        self._matriz=Matriz()

    def run(self):
        if self.menu():
            self.juego()

    def menu(self):
        self._interfaz.set_menu_window()
        while True:
            event, values = self._interfaz.get_window().Read()

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
                    self._interfaz.mensaje('NO HAY PARTIDA GUARDADA')
                    self._parametros_tablero = parametros
                else:
                    break
        self._interfaz.cerrar()
        return True

    def juego(self):
        self._interfaz.set_tablero_window()
        self._jugador1._letras_atril=['H','O','L','A','C','A','T']
        #self._interfaz.update()
        #self._interfaz._window['bot',0].Update('F') UPDATE DE LA VENTANA
        self._interfaz.cargar_parametros(self._jugador1._letras_atril,'jugador')
        self._interfaz.cargar_parametros(self._bot._letras_atril,'bot')
        #self._matriz=Matriz()
        #self._interfaz.definir_puntaje(self._parametros_tablero['dificultad'])
        while True:
            event, values = self._interfaz.get_window().Read()
            #print('EVENT: ',event,' - VALUES: ',values)
            if detectEvent(event) == True:   #HICE UN EVENTO EN LA MATRIZ O EN EL ATRIL
                item=self._interfaz._window[event].GetText()   #devuelve '' si seleccione matriz, devuelve 'Letra' si selecciona atril
                where=manipularEvento(event)   #devuelve si event_in_matriz o si event_in_atril
                if(where=='event_in_atril'):
                    self._jugador1.descontarLetra(item)
                    event, values = self._interfaz.get_window().Read()  #ESPERO QUE SELECCIONE MATRIZ
                    where=manipularEvento(event)
                if (where=='event_in_matriz'):
                    self._matriz.actualizarMatriz(item,event)
                    self._interfaz.actualizarBtn(event,item)
                    #self._interfaz.update({'P':[(5,9),(5,10),(5,11)]})
            if event in ('salir', None):
                break
            if event is 'fin_de_turno':
                    print(self._matriz._lista_letras)
                    ok=self._matriz.enviarPalabra()
                    if ok==True:
                        print('HI')
                        #puntosDePalabra=self._matriz.devolverPuntaje()
                        #self._jugador1._puntos+=puntosDePalabra
                        #print(self._jugador1._puntos)


            if event is 'guardar_partida':
                self._archivos.escribir_json(self._interfaz.guardar_parametros(self._parametros_tablero['dificultad']), juego_guardado_json, 'w')
                self._interfaz.mensaje('PARTIDA GUARDADA')
            if event is 'top_diez':
                if not self._archivos.ver_top_diez():
                    self._interfaz.mensaje('NO HAY RECORDS')
        self._archivos.cargar_record(self._parametros_tablero['dificultad'])
        self._interfaz.cerrar()


ScrabbleAR = Main()
ScrabbleAR.run()
