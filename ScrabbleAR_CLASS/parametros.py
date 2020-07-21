from copy import deepcopy
from random import choice
from const import bolsa
from json import dumps
import const

class Parametros:
    ''' ESTA CLASE CUMPLE UN IGUAL FUNCIONAMIENTO QUE LAS LISTAS EN
        JAVA, VIENE A REEMPLAZAR LA CLASE "Matriz" MÁS EL
        FUNCIONAMIENTO DE TODOS LOS PARAMETROS COMO "listas".
        COMO NO HAY PUNTEROS, PUEDE USARSE UNA CLASE COMO REFERENCIA.
        POR ESO HAY VARIAS REFERENCIAS SOBRE "Parametros".'''
    def __init__(self):
        self._p_jugador = 0     #PUNTOS DEL JUGADOR
        self._p_bot = 0         #PUNTOS DEL BOT
        self._a_jugador = {}        #ATRIL jugador
        self._a_bot = {}            #ATRIL BOT
        self._partida_g = False     #EXISTE PARTIDA
        self._fichas = 100          #FICHAS DEL INICIO
        self._ficha = {'': ''}      #FICHA ACTUAL
        self._dificultad = ''       #DIFICULTAD DE LA PARTIDA
        self._turno = choice([True, False]) # TURNO RANDOM
        self._tiempo_p_t = 20   # TIEMPO POR TURNO
        self._s = self._tiempo_p_t  # SEGUNDOS
        self._matriz = {}   # MATRIZ INICIAL
        self._palabra = {}  # PALABRA POR RONDA
        self._ultima_puntuacion = ('puntuacion', 0) # ÚLTIMA LLAVE HABILITADA DEL HISTORIAL PARA ESCRIBIR
        self._bolsa_fichas = deepcopy(bolsa)    # COPIA PROFUNDA DE LA BOLSA, DESLIGAMIENTO DE CUALQUIER PUNTERO
        self._primer_turno = True
        self._cambiar_fichas = 0    # CANTIDAD DE CAMBIO DE FICHAS REALIZADO DURANTE LA PARTIDA
        self._palabra_bot = None    # PALABRA GENERADA DEL BOT

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

    def set_key_historial(self, key):
        self._ultima_puntuacion = key

    def get_key_historial(self):
        return self._ultima_puntuacion

    def set_bolsa(self, bolsa):
        self._bolsa_fichas = bolsa

    def get_bolsa(self):
        return self._bolsa_fichas

    def set_primer_turno(self, boolean):
        self._primer_turno = boolean

    def get_primer_turno(self):
        return self._primer_turno

    def set_cambiar_fichas(self, cambiar_fichas):
        self._cambiar_fichas = cambiar_fichas

    def get_cambiar_fichas(self):
        return self._cambiar_fichas

    def add_key_historial(self, cantidad=1):    # AUMENTA ÉL NÚMERO DE LLAVE HABILITADO PARA SU ESCRITURA EN EL HISTORIAL SEGÚN 'cantidad'
        self._ultima_puntuacion = ('puntuacion', self._ultima_puntuacion[1]+cantidad)

    def add_cambiar_fichas(self, cantidad=1):   # AUMENTA EL NÚMERO DE VECES QUE SE CAMBIÓ DE FICHAS SEGÚN 'cantidad'
        self._cambiar_fichas += cantidad

    def borrar_palabra(self):
        self.set_palabra({})

    def add_puntos_jugador(self, puntos):   # SUMA EL PUNTAJE ACTUAL MAS EL PASADO POR PARAMETRO
        ''' RECIBE UNA CANTIDAD ESPECÍFICA DE PUNTOS PARA SUMAR'''
        self._p_jugador += puntos

    def add_puntos_bot(self, puntos):   # SUMA EL PUNTAJE ACTUAL MAS EL PASADO POR PARAMETRO
        ''' RECIBE UNA CANTIDAD ESPECÍFICA DE PUNTOS PARA SUMAR'''
        self._p_bot += puntos

    def add_ficha_palabra(self, ficha): # AGREGA UNA FICHA A LA PALABRA (UNA FICHA ES UNA LLAVE, VALOR DONDE LA LLAVE ES LA POSICIÓN DE LA LETRA Y EL VALOR LA LETRA)
        ''' AGREGA UNA FICHA "{LLAVE: LETRA}" A LA PALABRA.
            NO ES NECESARIO AGREGAR UNA LLAVE O LETRA SOLA.'''
        self._palabra.update(ficha)

    def del_ficha_palabra(self, ficha): # ELIMINA LA FICHA DE LA PALABRA PASADA POR PARAMETRO DONDE LA FICHA ES UNA LLAVE, VALOR
        ''' RECIBE UNA FICHA "{LLAVE: LETRA}" A ELIMINAR DE LA PALABRA'''
        self._palabra.pop(ficha)

    def add_letra_bolsa(self, letra, cant=1):   # SUMA 1 O LA CANTIDAD PASADA POR PARAMETRO A LA LETRA ESPECIFICADA
        ''' AUMENTA EN 1 O LA CANTIDAD PASADA POR PARÁMETRO A LA LETRA ESPECIFICADA'''
        self._bolsa_fichas[letra]['cantidad'] += cant

    def dec_letra_bolsa(self, letra, cant=1):   # DECREMENTA EN 1 O LA CANTIDAD PASADA POR PARAMETRO DE LA LETRA ESPECIFICADA
        ''' DECREMENTA EN 1 O LA CANTIDAD PASADA POR PARÁMETRO A LA LETRA ESPECIFICADA'''
        if self._bolsa_fichas[letra]['cantidad'] != 0 and letra != '':
            self._bolsa_fichas[letra]['cantidad'] -= cant

    def letra_random(self): # DEVUELVE UNA LETRA RANDOM SIEMPRE Y CUANDO ÉSTA EXISTA Y HAYAN LETRAS EN LA BOLSA
        ''' DEVUELTE UNA LETRA RANDOM DE LA BOLSA. SI NO HAY MÁS
            LETRAS EN LA BOLSA, DEVUELVE UN STRING NULO ""'''
        if self._fichas == 0:
            return ''
        letra = choice(list(self._bolsa_fichas.keys()))
        while letra == 0:
            letra = choice(list(self._bolsa_fichas.keys()))
        return letra

    def add_fichas(self, cant=1):   # AUMENTA EN 1 O LA CANIDAD PASADA POR PARÁMETRO LA CANTIDAD DE FICHAS TOTALES EN LA BOLSA
        ''' AUMENTA EN 1 O LA CANTIDAD PASADA POR PARÁMETRO LAS FICHAS EN LA BOLSA'''
        self._fichas += cant

    def dec_fichas(self, cant=-1):  # AUMENTA EN 1 O LA CANTIDAD PASADA POR PARÁMETRO LA CANTIDAD TOTAL DE FICHAS EN LA BOLSA
        ''' DECREMENTA EN 1 O LA CANTIDAD PASADA POR PARÁMETRO LAS FICHAS EN LA BOLSA'''
        if self._fichas != 0:
            self._fichas -= cant

    def set_key_ficha(self, key):   # SETEA LA POSICIÓN ESPECÍFICADA EN LA FICHA ACTUAL
        ''' CAMBIA LA LLAVE DE LA LETRA SELECCIONADA (EN MANO) POR EL PARÁMETRO'''
        letra = list(self._ficha.values())[0]
        self._ficha.clear()
        self._ficha[key] = letra

    def get_key_ficha(self):    # DEVUELVE LA POSICIÓNDE LA FICHA ACTUAL
        ''' DEVUELVE LA LLAVE DE LA FICHA SELECCIONADA (EN MANO)'''
        return list(self.get_ficha().keys())[0]

    def set_letra_ficha(self, letra):   # SETEA LA LETRA ESPECIFICADA EN LA FICHA ACTUAL
        ''' CAMBIA LA LETRA DE LA FICHA SELECCIONADA (EN MANO) POR EL PARÁMETRO'''
        self._ficha[list(self._ficha.keys())[0]] = letra

    def get_letra_ficha(self):  # DEVUELVE LA LETRA SELECCIONADA ACTUALMENTE
        ''' DEVUELVE LA LETRA DE LA FICHA SELECCIONADA (EN MANO)'''
        return list(self.get_ficha().values())[0]

    def agregar_ficha_atril_jugador(self, ficha=None):  # AGREGA LA FICHA SELECCIONADA ACTUALMENTE O LA PASADA POR PARAMETRO
        ''' AGREGA UNA FICHA "{LLAVE: LETRA}" AL ATRIL'''
        self._a_jugador.update(self._ficha if ficha == None else ficha)

    def sacar_ficha_atril_jugador(self):    # SACA LA FICHA SLECCIONADA ACTUALMENTE
        ''' SACA LA FICHA SELECCIONADA (EN MANO) DEL ATRIL.'''
        self._a_jugador[self.get_key_ficha()]=''

        #if self.get_letra_ficha() != '':
        #    self._a_jugador.pop(self.get_key_ficha())

    def agregar_ficha_atril_bot(self, ficha=None):  # AGREGA LA FICHA SELECCIONADA ACTUALMENTE O LA PASADA POR PARAMETRO
        ''' AGREGA UNA FICHA "{LLAVE: LETRA}" AL ATRIL.'''
        self._a_bot.update(self._ficha if ficha == None else ficha)

    def sacar_ficha_atril_bot(self,ficha):    # SACA LA FICHA SLECCIONADA ACTUALMENTE
        ''' SACA LA FICHA SELECCIONADA (EN MANO) DEL ATRIL.'''
        self._a_bot.pop(ficha)


    def agregar_ficha_matriz(self, key, letra=None):    # AGREGA LA FICHA A LA MATRIZ
        ''' AGREGA UNA FICHA "LLAVE, LETRA" A LA MATRIZ.
            SIRVE PARA AGREGA RAPIDAMENTE LA FICHA SELECCIONADA (EN MANO).'''
        self._matriz.update({key: self.get_letra_ficha() if letra == None else letra})

    def sacar_ficha_matriz(self, key):  # SACA LA FICHA DE LA MATRIZ
        ''' SACA UNA FICHA DE LA MATRIZ SEGÚN LA LLAVE PASADA POR PARÁMETRO.'''
        self._matriz.pop(key)

    def actualizar_atril(self,window,player): #player='jugador' o 'bot'
        ''' GENERA LETRAS NUEVAS PARA EL ATRIL EN CASO QUE LOS BOTONES
            DE LA INTERFAZ ESTEN VACIOS'''
        for boton in getattr(const,'atril_'+player):
                if window[boton].GetText() == '':
                     letra_nueva=self.letra_random()
                     const.const_Update(window,{boton:letra_nueva})

# ESTE ES EL FORMATO PARA GUARDAR Y CARGAR PARTIDA:
# parametros = {'jugador': {'puntos': 0, 'atril': {}},
#               'bot': {'puntos': 0, 'atril': {}},
#               'partida': False,
#               'fichas': 100,
#               'dificultad': '',
#               'turno': choice([True, False]),
#               'tiempos': {'tiempo_por_turno': 20, 'segundos': 20},
#               'matriz': {}}
    def guardar_parametros(self):   # GUARDA TODOS LOS PARAMETROS ACTUALES DE LA PARTIDA, ES DECIR, LAS VARIABLES SETEADAS HASTA EL MOMENTO DE CLICKEAR EN 'POSPONER'
        return {'jugador':
                    {'puntos': self.get_puntos_jugador(),
                    'atril': {dumps(key): value for key, value in self.get_atril_jugador().items()}},  # GUARDA UN DICCIONARIO CON LAS 'LLAVES: VALOR' FORMATEADAS EN FORMATO JSON PARA PODER SER GUARDADAS EN EL ARCHIVO
                'bot':
                    {'puntos': self.get_puntos_bot(),
                    'atril': {dumps(key): value for key, value in self.get_atril_bot().items()}},  # GUARDA UN DICCIONARIO CON LAS 'LLAVES: VALOR' FORMATEADAS EN FORMATO JSON PARA PODER SER GUARDADAS EN EL ARCHIVO
                'fichas': self.get_fichas(),
                'dificultad': self.get_dificultad(),
                'turno': self.get_turno(),
                'tiempos':
                    {'tiempo_por_turno': self.get_tiempo_por_turno(),
                 'segundos': self.get_segundos()},
                'matriz': {dumps(key): value for key, value in self.get_matriz().items()},  # GUARDA UN DICCIONARIO CON LAS 'LLAVES: VALOR' FORMATEADAS EN FORMATO JSON PARA PODER SER GUARDADAS EN EL ARCHIVO
                'bolsa_fichas': self.get_bolsa(),
                'primer_turno': self.get_primer_turno(),
                'cambiar_fichas': self.get_cambiar_fichas()}

    def cargar_parametros(self, partida):   # CARGA TODOS LOS PARÁMETROS SEGÚN LA PARTIDA GUARDADA, SEGÚN 'partida' QUE CONTIENE EL FORMATO ACLARADO EN LA LÍNEA 213
        self.set_hay_partida()
        self.set_atril_jugador({(str(key.strip('[ ]').split(', ')[0].strip('"')),   # CARGA LOS DICCIONARIOS FORMATEADOS EN JSON Y LOS DESFORMATEA PARA PODER CARGAR LA VENTANA
                                 int(key.strip('[ ]').split(', ')[1])):
                                value for key, value in partida['jugador']['atril'].items()})
        self.set_atril_bot({(str(key.strip('[ ]').split(', ')[0].strip('"')),   # CARGA LOS DICCIONARIOS FORMATEADOS EN JSON Y LOS DESFORMATEA PARA PODER CARGAR LA VENTANA
                             int(key.strip('[ ]').split(', ')[1])):
                            value for key, value in partida['bot']['atril'].items()})
        self.set_matriz({(int(key.strip('[ ]').split(', ')[0]), # CARGA LOS DICCIONARIOS FORMATEADOS EN JSON Y LOS DESFORMATEA PARA PODER CARGAR LA VENTANA
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
        self.set_primer_turno(partida['primer_turno'])
        self.set_cambiar_fichas(partida['cambiar_fichas'])
