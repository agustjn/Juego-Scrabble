from pattern.es import verbs, tag, spelling, lexicon, parse
from layout import Window, layout_puntos_por_letra as ppl, font_size, margins_size, window_color
from mod_puntos import Puntaje
from mod_popups import Popups
from copy import deepcopy
import const


class Interfaz(Puntaje):

    def __init__(self, parametros):
        self._parametros = parametros
        self._popups = Popups()
        Puntaje.__init__(self)

    def puntos_por_letra(self, window):
        ''' ESTA FUNCION CONFIGURA LAS LETRAS DE LA BOLSA'''
        _window = Window(title='ScrabbleAR',
                         font=font_size,
                         margins=margins_size,
                         background_color=window_color).Layout(deepcopy(ppl))
        while True:
            _event, _values = _window.Read()     # timeout NOS PERMITE LEER LAS 2
                   # VENTANAS AL MISMO TIEMPO
             # SI DEVUELVE FALSO, CERRAMOS EL JUEGO
            if _event is None:      # SI ELIGIÓ SALIR DEL MENÚ DE MODIFICACIÓN DE PUNTAJES
                _window.Close()
                return True         # SI DEVOLVEMOS TRUE, SOLO CERRAMOS LA VENTANA LOCAL
            if _event in ('puntos_personalizados','cantidad_letras'):       # SI CLICKEÓ EN ACEPTAR, SE SETEAN MEDIANTE PUNTEROS LOS PUNTAJES MODIFICADOS
                bolsa = self._parametros.get_bolsa()    # TOMA LA BOLSA PARA EL JUEGO
                i=0
                for letras in list(_values.items()):    # EXTRACCIÓN DE LOS
                    i+=1
                    for letra in letras[1]:     # POR CADA LETRA ESCRITA
                        if letra and ord(letra) in const.minus or ord(letra) in const.mayus:    # SI LA LETRA ES VÁLIDA (ES DECIR, EXISTE EN LA BOLSA)
                            bolsa[letra.upper()]['puntaje'] = int(letras[0].split('_')[-1])     # MODIFICAMOS EL PUNTAJE (SE MODIFICA EL VALOR AL QUE APUNTA EL PUNTERO, POR ENDE, NO ES NECESARIO SETEAR LA BOLSA)
                    if i==10:
                        break
                for letra in _values['input_letras']:
                    if letra and ord(letra) in const.minus or ord(letra) in const.mayus:
                        bolsa[letra.upper()]['cantidad']=int(_values['spin'])
                if _event is 'puntos_personalizados':
                    _window.Close()
                    return True         # SI DEVOLVEMOS TRUE, SOLO CERRAMOS LA VENTANA LOCAL

    def primer_turno(self):
        ''' ESTA FUNCION DEFINE SI SE ESTA O NO EN EL PRIMER TURNO '''
        if not self._parametros.get_primer_turno(): # SI NO ES EL PRIMER TURNO
            return False
        if self._parametros.get_palabra():  # SI HAY FICHAS EN LA PALABRA, ES DECIR, SE INGRESÓ UNA PALABRA
            for key in self._parametros.get_palabra():  # PARA CADA UBICACIÓN DE LAS LETRAS
                if key == (7, 7):   # SI SE UBICÓ ALGUNA EN EL CENTRO
                    self._parametros.set_primer_turno(False) # FINALIZA EL PRIMER TURNO
                    return False
        return True # SI ESTAMOS EN EL PRIMER TURNO, O HASTA ACÁ LO ESTUVIMOS (DEPENDE DE LA LÍNEA 20)

    def control_bolsa(self, quien):
        ''' ESTA FUNCION DEFINE SI SE ALCANZA O NO A REPONER LOS ATRILES '''
        return len(getattr(self._parametros, 'get_atril_'+quien)()) + self._parametros.get_fichas() < 7

    def devolver_fichas(self, window, quien):
        ''' ESTA FUNCION SE ENCARGA DE DEVOLVER LAS FICHAS CUANDO LA PALABRA ES INVALIDA '''
        palabra, atril = self._parametros.get_palabra(), getattr(self._parametros, 'get_atril_'+quien)() # EL ATRÍL SEGÚN QUIÉN, 'jugador' o 'bot'
        letras = list(palabra.values())
        for key in getattr(const, 'atril_'+quien):  # PARA CADA LLAVE EN EL ATRIL
            if atril[key] == '':    # SI LA FICHA NO TIENE LETRA
                if letras:
                    self._parametros.add_letra_bolsa(letras[0]) # DEVOLVEMOS LA LETRA A LA BOLSA
                    self._parametros.add_fichas()   # AUMENTAMOS LA CANTIDAD DE LETRAS DE LA BOLSA EN 1
                    atril[key] = letras.pop(0)  # REUBICA LA LETRA EN EL ATRIL (.pop DEVUELVE Y ELIMINA EL ELEMENTO SEGÚN EL ÍNDICE, IGUAL QUE eliminar_en(pos) DE LISTAS EN ALGORITMOS)
        for key in palabra:
            self._parametros.pop_ficha_matriz(key) # BORRA LA MATRIZ
        getattr(self._parametros, 'set_atril_'+quien)(atril)  # RESETEA EL ATRIL
        const.const_Update(window, {key: '' for key in palabra}, atril)   # ACTUALIZA LA MATRIZ Y EL ATRIL

    def mover_ficha(self, window, key):
        ''' ESTA FUNCIÓN CUMPLE CON EL MOVIMIENTO DE LA FICHA
            SELECCIONADA (EN MANO) DESDE EL ATRIL HASTA LA MATRIZ.'''
        self._parametros.sacar_ficha_atril_jugador()    # SACA LA FICHA DEL ATRIL
        self._parametros.agregar_ficha_matriz(key)  # LA AGREGA A LA MATRIZ
        self._parametros.add_ficha_palabra({key: self._parametros.get_letra_ficha()})   # AGREGA LA FICHA A LA PALABRA
        const.const_Update(window, {self._parametros.get_key_ficha(): '', key: self._parametros.get_letra_ficha()}) # ACTUALIZA EL ATRIL Y LA MATRIZ
        self._parametros.set_letra_ficha('')    # BORRA LA LETRA DE LA FICHA

    def repartir_fichas(self, atril, window):
        ''' AGREGA LAS FICHAS SIN USAR A LA BOLSA. REPARTE HASTA 7 NUEVAS FICHAS.'''
        self._parametros.dec_fichas(7-len(atril))   # DECREMENTA LAS FICHAS SEGÚN LA CANTIDAD UTILIZADA, ES DECIR, RESTA LA CANTIDAD DE FICHAS UTILIZADAS
        for key in atril:   # PARA CADA UBICACIÓN EN EL ATRIL
            if atril[key] != '':
                self._parametros.add_letra_bolsa(atril[key])    # AGREGA LAS LETRAS NO UTILIZADAS
        if atril == self._parametros.get_atril_jugador():   # SI HABLAMOS DEL ATRIL DEL JUGADOR
            for i in range(7):  # SE REPARTEN LAS 7 NUEVAS FICHAS
                letra = {('jugador', i): self._parametros.letra_random()}   # GENERA UNA FICHA RANDOM
                self._parametros.agregar_ficha_atril_jugador(letra) # AGREGA LA FICHA RANDOM AL ATRIL
                self._parametros.dec_letra_bolsa(list(letra.values())[0])   # DECREMENTA LA CANTIDAD TOTAL DE FICHAS EN LA BOLSA
                const.const_Update(window, letra)   # ACTUALIZA EL ATRIL CON ESA LETRA
        else:   # SI HABLAMOS DEL ATRIL DEL BOT, LO MISMO QUE CON EL JUGADOR
            for i in range(7):
                letra = {('bot', i): self._parametros.letra_random()}
                self._parametros.agregar_ficha_atril_bot(letra)
                self._parametros.dec_letra_bolsa(list(letra.values())[0])
                const.const_Update(window, letra)
        const.const_Update(window, {'fichas_jugador': 'MIS FICHAS -- TOTAL DE FICHAS '+str(self._parametros.get_fichas())})    # ACTUALIZA LA CANTIDAD TOTAL DE FICHAS EN LA VENTANA

    def _validar_palabra(self):
        ''' TRADUCE LAS FICHAS Y LAS ORDENA HORIZONTAL Y VERTICALMENTE. SI DE
            ALGUNA DE ESAS DOS MANERAS EXISTE LA PALABRA EN LOS LISTADOS DE
            PALABRAS, LA DEVUELVE, SINO, DEVUELVE UN STRING NULO "".'''
        palabra_en_x, palabra_en_y, palabra = '', '', self._parametros.get_palabra()   # DEFINIMOS LAS PALABRAS EN x E y Y LA PALABRA ACTUAL
        for key in {key: value for key, value in sorted(palabra.items(), key=lambda elem: elem[0][0])}: # ESCRIBE LA PALABRA ORIENTADA EN x
            palabra_en_x += palabra[key]
            #tipo = parse(str().join(list(self._parametros.get_palabra().values()))).split('/')[1]
            #print(tipo)
            #if palabra_en_x.lower() in lexicon.keys() and palabra_en_x.lower()in spelling.keys():
            #    print('SI ESTA')
            #    print(palabra_en_x)
            #else:
                #print(palabra_en_x)
            #    print('NO ESTA')
        for key in {key: value for key, value in sorted(palabra.items(), key=lambda elem: elem[0][1])}: # ESCRIBE LA PALABRA ORIENTADA EN y
            palabra_en_y += palabra[key]

        if (palabra_en_x.lower() in lexicon.keys() and palabra_en_x.lower() in spelling.keys()) or (palabra_en_y.lower() in lexicon.keys() and palabra_en_y.lower() in spelling.keys()):
            if self._parametros.get_dificultad() == 'FÁCIL':
                #print(palabra)
                return palabra # SI LA PALABRA EXISTE, INDEPENDIENTEMENTE DEL TIPO QUE SEA (YA QUE ESTAMOS EN DIFICULTAD FÁCIL), LA DEVUELVE, SINO, UN DICT VACÍO (DE ESTA MANERA SE PUEDE CORROVORAR SI LA PALABRA EXISTE PREGUNTANDO POR EL DICT VACIÓ O NO 'if not palabra' - 'if palabra')
            else:
                tipo = parse(str().join(list(self._parametros.get_palabra().values()))).split('/')[1]  # TIPO DE LA PALABRA. SI LA PALABRA ES UN VERBO, EL TIPO ES 'VB', SI ES UN ADJETIVO, 'JJ'. SOLO ESOS 2 TIPOS DE PALABRAS VALEN PARA 'MEDIO' O 'DIFICIL'. NO ES NECESARIO CORROVORAR SI LA PALABRA EXISTE EN SPELLING O LEXICON, PORQUE CUALFUERA ELA PALABRA, SI NO LA RECONOCE COMO VERBO 'VB' O ADJETIVO 'JJ', NO ES VÁLIDA. SOLAMENTE LAS RECONOCE COMO VERBO O ADJETIVO SI SE ENCUENTRA DENTRO DE SPELLING O LEXICON
                #print(tipo)
                #print(palabra)
                return palabra if tipo == 'VB' or tipo == 'JJ' else {}   # SI LA DIFICULTAD NO ES FÁCIL, INDEPENDIENTEMENTE DE LA PALABRA QUE SE HAYA ESCRITO, SI ES UN VERBO O UN ADJETIVO, LA DEVUELVE, SINO DEVUELVE UN DICT VACÍO (AL IGUAL QUE EN FÁCIL)
        else:
            return {}

    def calcular_palabra(self, window, quien,palabra={}):
        ''' CALCULA Y DEVUELVE EL PUNTAJE GANADO O PERDIDO AL FINALIZAR UN TURNO'''
        if len(self._parametros.get_palabra()) > 1:
            if quien == 'bot' and palabra=={}:
                palabra = self._parametros.get_palabra() # palabra RECIBE LA PALABRA SI ES VÁLIDA, SINO, UN DICT VACÍO (PALABRA VACÍA)
            else:
                palabra = self._validar_palabra()
                #print('PALABRA:',palabra)
            if palabra: # ENTONCES, SI LA PALABRA ES VÁLIDA, SI palabra CONTIENE ELEMENTOS
                puntos = self.calcular_puntos(quien, palabra) # CALCULA LOS PUNTOS DE TAL PALABRA
                getattr(self._parametros, 'add_puntos_'+quien)(puntos)    # SUMA LOS PUNTOS CALCULADOS A QUIEN LE CORRESPONDA SEGÚN 'quien'
                self._parametros.add_historial(quien.upper(),'PALABRA: '+str().join(list(self._parametros.get_palabra().values())), 'VÁLIDA', ('+' if puntos > -1 else '')+str(puntos)+' PUNTOS',' ')
                const.const_Update(window, {'puntos_'+quien: getattr(self._parametros, 'get_puntos_'+quien)()}) # ACTUALIZA EL PUNTAJE ACTUAL Y EL HISTORIAL
            else:   # SI LA PALABRA NO ES VÁLIDA PARA EL JUGADOR O PARA EL BOT NO LA ENCONTRO
                self._parametros.add_historial(quien.upper(),'PALABRA: '+(str().join(list(self._parametros.get_palabra().values()) if quien=='jugador' else 'NO ENCONTRADO')), 'INVÁLIDA', '+0 PUNTOS',' ')
                self.devolver_fichas(window, quien)
            window.Element('historial').Update(self._parametros.get_historial())
            return True
        else:
            self._parametros.add_historial(quien.upper(),'PALABRA: '+str(str().join(list(self._parametros.get_palabra().values())) if quien=='jugador' else 'NO ENCONTRADO'),'INVÁLIDA', '+0 PUNTOS',' ')
            window.Element('historial').Update(self._parametros.get_historial())
            return False

    def set_dificultad(self):
        ''' SETEA LA DIFICULTAD '''
        self._set_dificultad(self._parametros.get_dificultad())

    def check_orientation(self, palabra):
        ''' ESTA FUNCION SE ENCARGA DE VERIFICAR LA ORIENTACION DE LA PALABRA
            INGRASADA EN EL TABLERO '''
        lista_posiciones = list(palabra.keys())
        firstPosition = lista_posiciones[0]
        lastPosition = lista_posiciones[-1]
        firstCol = lista_posiciones[0][0]
        lastCol = lista_posiciones[-1][0]
        if firstCol == lastCol:
            return 'Vertical'
        else:
            return 'Horizontal'
        # return 'Vertical' if lista_posiciones[0][0] == lista_posiciones[-1][0] else 'Horizontal'

    def evaluar_posicion(self, window, event, palabra):
        '''Si la posicion (x,y) que recibí esta fuera del rango,
           borro la letra de _palabra y actualizo el boton de la matriz '''
        if palabra:
            lista_posiciones = list(palabra.keys())
            if len(palabra) > 1:
                if lista_posiciones[0][0] != lista_posiciones[-1][0]:   # if self.check_orientation(palabra) == 'Horizontal':
                    if event[1] != lista_posiciones[0][1] or event[0] != lista_posiciones[-1][0]+1:
                        self._popups.popup('Error de colocacion de letra')
                        return False
                else:   # SI ES VERTICAL
                    if event[0] != lista_posiciones[0][0] or event[1] != lista_posiciones[-1][1]+1:
                        self._popups.popup('Error de colocacion de letra')
                        return False
            elif (event[0] == lista_posiciones[-1][0]+1 and (event[1] == lista_posiciones[-1][1])) or ((event[0] == lista_posiciones[-1][0]) and event[1] == lista_posiciones[-1][1]+1):
                return True
            else:
                self._popups.popup('Error de colocacion de letra')
                return False
        return True
