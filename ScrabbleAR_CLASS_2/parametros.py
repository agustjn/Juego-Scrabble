from copy import deepcopy
from random import choice
from const import bolsa
from json import dumps


class Parametros:
    ''' ESTA CLASE CUMPLE UN IGUAL FUNCIONAMIENTO QUE LAS LISTAS EN
        JAVA, VIENE A REEMPLAZAR LA CLASE "Matriz" MÁS EL
        FUNCIONAMIENTO DE TODOS LOS PARAMETROS COMO "listas".
        COMO NO HAY PUNTEROS, PUEDE USARSE UNA CLASE COMO REFERENCIA.
        POR ESO HAY VARIAS REFERENCIAS SOBRE "Parametros".'''
    def __init__(self):
        self._p_jugador = 0
        self._p_bot = 0
        self._a_jugador = {}
        self._a_bot = {}
        self._partida_g = False
        self._fichas = 100
        self._ficha = {'': ''}
        self._dificultad = ''
        self._turno = choice([True, False])
        self._tiempo_p_t = 20
        self._s = self._tiempo_p_t
        self._matriz = {}
        self._palabra = {}
        self._bolsa_fichas = deepcopy(bolsa)

    def set_puntos_jugador(self, puntos):
        self._p_jugador = puntos

    def get_puntos_jugador(self):
        return self._p_jugador

    def set_puntos_bot(self, puntos):
        self._p_bot = puntos

    def get_puntos_bot(self):
        return self._p_bot

    def set_atril_jugador(self, atril):
        self._a_jugador = atril

    def get_atril_jugador(self):
        return self._a_jugador

    def set_atril_bot(self, atril):
        self._a_bot = atril

    def get_atril_bot(self):
        return self._a_bot

    def set_hay_partida(self):
        self._partida_g = True

    def get_hay_partida(self):
        return self._partida_g

    def set_fichas(self, fichas):
        self._fichas = fichas

    def get_fichas(self):
        return self._fichas

    def set_ficha(self, ficha):
        self._ficha = ficha

    def get_ficha(self):
        return self._ficha

    def set_dificultad(self, dificultad):
        self._dificultad = dificultad

    def get_dificultad(self):
        return self._dificultad

    def set_turno(self, turno):
        self._turno = turno

    def get_turno(self):
        return self._turno

    def set_tiempo_por_turno(self, tiempo):
        self._tiempo_p_t = tiempo

    def get_tiempo_por_turno(self):
        return self._tiempo_p_t

    def set_segundos(self, tiempo):
        self._s = tiempo

    def get_segundos(self):
        return self._s

    def set_matriz(self, matriz):
        self._matriz = matriz

    def get_matriz(self):
        return self._matriz

    def set_palabra(self, palabra):
        self._palabra = palabra

    def get_palabra(self):
        return self._palabra

    def set_bolsa(self, bolsa):
        self._bolsa_fichas = bolsa

    def get_bolsa(self):
        return self._bolsa_fichas

    def borrar_palabra(self):
        ''' SETEA LA VARIABLE "_palabra" A SU ESTADO ORIGINAL (NULO).'''
        self.set_palabra({'': ''})

    def add_puntos_jugador(self, puntos):
        ''' RECIBE UNA CANTIDAD ESPECÍFICA DE PUNTOS PARA SUMAR'''
        self._p_jugador += puntos

    def add_puntos_bot(self, puntos):
        ''' RECIBE UNA CANTIDAD ESPECÍFICA DE PUNTOS PARA SUMAR'''
        self._p_bot += puntos

    def add_ficha_palabra(self, ficha):
        ''' AGREGA UNA FICHA "{LLAVE: LETRA}" A LA PALABRA.
            NO ES NECESARIO AGREGAR UNA LLAVE O LETRA SOLA.'''
        self._palabra.update(ficha)

    def del_ficha_palabra(self, ficha):
        ''' RECIBE UNA FICHA "{LLAVE: LETRA}" A ELIMINAR DE LA PALABRA'''
        self._palabra.pop(ficha)

    def add_letra_bolsa(self, letra, cant=0):
        ''' AUMENTA EN 1 O LA CANTIDAD PASADA POR PARÁMETRO A LA LETRA ESPECIFICADA'''
        self._bolsa_fichas[letra]['cantidad'] += 1 if cant == 0 else cant

    def dec_letra_bolsa(self, letra, cant=0):
        ''' DECREMENTA EN 1 O LA CANTIDAD PASADA POR PARÁMETRO A LA LETRA ESPECIFICADA'''
        if self._bolsa_fichas[letra]['cantidad'] != 0 and letra != '':
            self._bolsa_fichas[letra]['cantidad'] -= 1 if cant == 0 else cant

    def letra_random(self):
        ''' DEVUELTE UNA LETRA RANDOM DE LA BOLSA. SI NO HAY MÁS
            LETRAS EN LA BOLSA, DEVUELVE UN STRING NULO ""'''
        if self._fichas == 0:
            return ''
        letra = choice(list(self._bolsa_fichas.keys()))
        while letra == 0:
            letra = choice(list(self._bolsa_fichas.keys()))
        return letra

    def add_fichas(self, cant=-1):
        ''' AUMENTA EN 1 O LA CANTIDAD PASADA POR PARÁMETRO LAS FICHAS EN LA BOLSA'''
        self._fichas += 1 if cant == -1 else cant

    def dec_fichas(self, cant=-1):
        ''' DECREMENTA EN 1 O LA CANTIDAD PASADA POR PARÁMETRO LAS FICHAS EN LA BOLSA'''
        if self._fichas != 0:
            self._fichas -= 1 if cant == -1 else cant

    def set_key_ficha(self, key):
        ''' CAMBIA LA LLAVE DE LA LETRA SELECCIONADA (EN MANO) POR EL PARÁMETRO'''
        letra = list(self._ficha.values())[0]
        self._ficha.clear()
        self._ficha[key] = letra

    def get_key_ficha(self):
        ''' DEVUELVE LA LLAVE DE LA FICHA SELECCIONADA (EN MANO)'''
        return list(self.get_ficha().keys())[0]

    def set_letra_ficha(self, letra):
        ''' CAMBIA LA LETRA DE LA FICHA SELECCIONADA (EN MANO) POR EL PARÁMETRO'''
        self._ficha[list(self._ficha.keys())[0]] = letra

    def get_letra_ficha(self):
        ''' DEVUELVE LA LETRA DE LA FICHA SELECCIONADA (EN MANO)'''
        return list(self.get_ficha().values())[0]

    def agregar_ficha_atril_jugador(self, ficha=None):
        ''' AGREGA UNA FICHA "{LLAVE: LETRA}" AL ATRIL'''
        self._a_jugador.update(self._ficha if ficha == None else ficha)

    def sacar_ficha_atril_jugador(self):
        ''' SACA LA FICHA SELECCIONADA (EN MANO) DEL ATRIL.'''
        if self.get_letra_ficha() != '':
            self._a_jugador.pop(self.get_key_ficha())

    def agregar_ficha_atril_bot(self, ficha=None):
        ''' AGREGA UNA FICHA "{LLAVE: LETRA}" AL ATRIL.'''
        self._a_bot.update(self._ficha if ficha == None else ficha)

    def sacar_ficha_atril_bot(self):
        ''' SACA LA FICHA SELECCIONADA (EN MANO) DEL ATRIL.'''
        if self.get_letra_ficha() != '':
            self._a_bot.pop(self.get_key_ficha())

    def agregar_ficha_matriz(self, key, letra=None):
        ''' AGREGA UNA FICHA "LLAVE, LETRA" A LA MATRIZ.
            SIRVE PARA AGREGA RAPIDAMENTE LA FICHA SELECCIONADA (EN MANO).'''
        self._matriz.update({key: self.get_letra_ficha() if letra == None else letra})

    def sacar_ficha_matriz(self, key):
        ''' SACA UNA FICHA DE LA MATRIZ SEGÚN LA LLAVE PASADA POR PARÁMETRO.'''
        self._matriz.pop(key)

# ESTE ES EL FORMATO PARA GUARDAR Y CARGAR PARTIDA:
# parametros = {'jugador': {'puntos': 0, 'atril': {}},
#               'bot': {'puntos': 0, 'atril': {}},
#               'partida': False,
#               'fichas': 100,
#               'dificultad': '',
#               'turno': choice([True, False]),
#               'tiempos': {'tiempo_por_turno': 20, 'segundos': 20},
#               'matriz': {}}
    def guardar_parametros(self):
        return {'jugador':
                {'puntos': self.get_puntos_jugador(),
                 'atril': {dumps(key): value for key, value in self.get_atril_jugador().items()}},
                'bot':
                {'puntos': self.get_puntos_bot(),
                 'atril': {dumps(key): value for key, value in self.get_atril_bot().items()}},
                'fichas': self.get_fichas(),
                'dificultad': self.get_dificultad(),
                'turno': self.get_turno(),
                'tiempos':
                {'tiempo_por_turno': self.get_tiempo_por_turno(),
                 'segundos': self.get_segundos()},
                'matriz': {dumps(key): value for key, value in self.get_matriz().items()},
                'bolsa_fichas': self.get_bolsa()}

    def cargar_parametros(self, partida):
        self.set_hay_partida()
        self.set_atril_jugador({(str(key.strip('[ ]').split(', ')[0].strip('"')),
                                 int(key.strip('[ ]').split(', ')[1])):
                                value for key, value in partida['jugador']['atril'].items()})
        self.set_atril_bot({(str(key.strip('[ ]').split(', ')[0].strip('"')),
                             int(key.strip('[ ]').split(', ')[1])):
                            value for key, value in partida['bot']['atril'].items()})
        self.set_matriz({(int(key.strip('[ ]').split(', ')[0]),
                          int(key.strip('[ ]').split(', ')[1])):
                         value for key, value in partida['matriz'].items()})
        self.set_puntos_jugador(partida['jugador']['puntos'])
        self.set_puntos_bot(partida['bot']['puntos'])
        self.set_fichas(partida['fichas'])
        self.set_dificultad(partida['dificultad'])
        self.set_turno(partida['turno'])
        self.set_tiempo_por_turno(partida['tiempos']['tiempo_por_turno'])
        self.set_segundos(partida['tiempos']['segundos'])
        self.set_bolsa(partida['bolsa_fichas'])
