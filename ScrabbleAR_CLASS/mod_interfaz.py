from pattern.es import verbs, tag, spelling, lexicon, parse
from mod_puntos import Puntaje
from mod_popups import Popups
import const


class Interfaz(Puntaje):

    def __init__(self, parametros):
        self._parametros = parametros
        self._popups = Popups()
        Puntaje.__init__(self)

    def primer_turno(self):
        if not self._parametros.get_primer_turno(): # SI NO ES EL PRIMER TURNO
            return False
        if self._parametros.get_palabra():  # SI HAY FICHAS EN LA PALABRA, ES DECIR, SE INGRESÓ UNA PALABRA
            for key in self._parametros.get_palabra():  # PARA CADA UBICACIÓN DE LAS LETRAS
                if key == (7, 7):   # SI SE UBICÓ ALGUNA EN EL CENTRO
                    self._parametros.set_primer_turno(False) # FINALIZA EL PRIMER TURNO
                    return False
        return True # SI ESTAMOS EN EL PRIMER TURNO, O HASTA ACÁ LO ESTUVIMOS (DEPENDE DE LA LÍNEA 20)

    def devolver_fichas(self, window, quien):
        palabra = self._parametros.get_palabra()
        atril = getattr(self._parametros, 'get_atril_'+quien)() # EL ATRÍL SEGÚN QUIÉN, 'jugador' o 'bot'
        if len(getattr(self._parametros, 'get_atril_'+quien)()) == 7:   # SI EL TAMAÑO DEL ATRIL SEGÚN QUIÉN ES IGUAL AL MÁXIMO, 7
            for key in palabra: # PARA CADA UBICACIÓN DE LAS LETRAS
                self._parametros.add_letra_bolsa(palabra[key])  # SUMA LA LETRA A LA BOLSA
                self._parametros.add_fichas()   # Y AUMENTA EN 1 EL TOTAL DE FICHAS, (TOTAL DE LETRAS SI SE QUIERE)
            const.const_Update(window, {key: '' for key in palabra})    # ACTUALIZA LA VENTANA, "LAS BORRA DE LA MATRIZ"
            self._parametros.set_matriz({}) # BORRA LA MATRIZ
            const.const_Update(window, {'fichas_jugador': 'MIS FICHAS ~~~~~~ TOTAL DE FICHAS: '+str(self._parametros.get_fichas())})    # ACTUALIZA EL TOTAL DE FICHAS
            return False
        keys, viejo_atril, i, j = getattr(const, 'atril_'+quien), {}, 0, 0  # KEYS ES EL ATRIL DE QUIÉN ('jugador' o 'bot')
        for key in keys:    # PARA CADA LLAVE EN EL ATRIL
            if key in atril:    # SI LA LLAVE ESTÁ EN EL ATRIL CON LAS FICHAS
                viejo_atril[key] = atril[key]   # LA ESCRIBE EN EL VIEJO ATRIL
            else:
                viejo_atril[(quien, i)] = list(palabra.values())[j] # SINO, AGREGA LA LA QUE SE PUSO EN LA MATRIZ
                j += 1
            i += 1
        self._parametros.set_matriz({}) # BORRA LA MATRIZ
        getattr(self._parametros, 'set_atril_'+quien)(viejo_atril)  # SETEA EL ATRIL VIEJO
        const.const_Update(window, {key: '' for key in palabra}, viejo_atril)   # ACTUALIZA LA MATRIZ Y EL ATRIL

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
        const.const_Update(window, {'fichas_jugador': 'MIS FICHAS ~~~~~~ TOTAL DE FICHAS: '+str(self._parametros.get_fichas())})    # ACTUALIZA LA CANTIDAD TOTAL DE FICHAS EN LA VENTANA

    def _validar_palabra(self):
        ''' TRADUCE LAS FICHAS Y LAS ORDENA HORIZONTAL Y VERTICALMENTE. SI DE
            ALGUNA DE ESAS DOS MANERAS EXISTE LA PALABRA EN LOS LISTADOS DE
            PALABRAS, LA DEVUELVE, SINO, DEVUELVE UN STRING NULO "".'''
        palabra_en_x, palabra_en_y, palabra = '', '', self._parametros.get_palabra()    # DEFINIMOS LAS PALABRAS EN x E y Y LA PALABRA ACTUAL
        for key in {key: value for key, value in sorted(palabra.items(), key=lambda elem: elem[0][0])}: # ESCRIBE LA PALABRA ORIENTADA EN x
            palabra_en_x += palabra[key]
        for key in {key: value for key, value in sorted(palabra.items(), key=lambda elem: elem[0][1])}: # ESCRIBE LA PALABRA ORIENTADA EN y
            palabra_en_y += palabra[key]
        if self._parametros.get_dificultad() == 'FÁCIL':
            return palabra if palabra_en_x in lexicon or palabra_en_x in spelling or palabra_en_y in lexicon or palabra_en_y in spelling else {} # SI LA PALABRA EXISTE, INDEPENDIENTEMENTE DEL TIPO QUE SEA (YA QUE ESTAMOS EN DIFICULTAD FÁCIL), LA DEVUELVE, SINO, UN DICT VACÍO (DE ESTA MANERA SE PUEDE CORROVORAR SI LA PALABRA EXISTE PREGUNTANDO POR EL DICT VACIÓ O NO 'if not palabra' - 'if palabra')
        tipo = parse(str().join(list(self._parametros.get_palabra().values()))).split('/')[1]  # TIPO DE LA PALABRA. SI LA PALABRA ES UN VERBO, EL TIPO ES 'VB', SI ES UN ADJETIVO, 'JJ'. SOLO ESOS 2 TIPOS DE PALABRAS VALEN PARA 'MEDIO' O 'DIFICIL'. NO ES NECESARIO CORROVORAR SI LA PALABRA EXISTE EN SPELLING O LEXICON, PORQUE CUALFUERA ELA PALABRA, SI NO LA RECONOCE COMO VERBO 'VB' O ADJETIVO 'JJ', NO ES VÁLIDA. SOLAMENTE LAS RECONOCE COMO VERBO O ADJETIVO SI SE ENCUENTRA DENTRO DE SPELLING O LEXICON
        print(tipo)
        return palabra if tipo == 'VB' or tipo == 'JJ' else {}   # SI LA DIFICULTAD NO ES FÁCIL, INDEPENDIENTEMENTE DE LA PALABRA QUE SE HAYA ESCRITO, SI ES UN VERBO O UN ADJETIVO, LA DEVUELVE, SINO DEVUELVE UN DICT VACÍO (AL IGUAL QUE EN FÁCIL)

    def calcular_palabra(self, window, quien):
        ''' CALCULA Y DEVUELVE EL PUNTAJE GANADO O PERDIDO AL FINALIZAR UN TURNO'''
        palabra = self._validar_palabra() # palabra RECIBE LA PALABRA SI ES VÁLIDA, SINO, UN DICT VACÍO (PALABRA VACÍA)
        if palabra: # ENTONCES, SI LA PALABRA ES VÁLIDA, SI palabra CONTIENE ELEMENTOS
            puntos = self.calcular_puntos(quien, palabra) # CALCULA LOS PUNTOS DE TAL PALABRA
            getattr(self._parametros, 'add_puntos_'+quien)(puntos)    # SUMA LOS PUNTOS CALCULADOS A QUIEN LE CORRESPONDA SEGÚN 'quien'
            const.const_Update(window, {'puntos_'+quien: getattr(self._parametros, 'get_puntos_'+quien)()}, {self._parametros.get_key_historial(): str().join(list(palabra.values()))+':\n'+str(puntos)}) # ACTUALIZA EL PUNTAJE ACTUAL Y EL HISTORIAL
        else:   # SI LA PALABRA NO ES VÁLIDA
            const.const_Update(window, {self._parametros.get_key_historial(): str(str().join(list(self._parametros.get_palabra().values())))+':'+'\nINVÁLIDA'})
        self._parametros.add_key_historial()

    def set_dificultad(self):
        self._set_dificultad(self._parametros.get_dificultad())

    def check_orientation(self,palabra):
        lista_posiciones=list(palabra.keys())
        firstPosition=lista_posiciones[0]
        lastPosition=lista_posiciones[-1]
        firstCol=lista_posiciones[0][0]
        lastCol=lista_posiciones[-1][0]
        if firstCol == lastCol:
            return 'Vertical'
        else:
            return 'Horizontal'


    def evaluar_posicion(self,window,event,palabra):
        lista_posiciones=list(palabra.keys())
        if not palabra:
            '''Si el diccionario es vacio'''
            pass
        else:
            orientacion=self.check_orientation(palabra)
            '''Si la posicion (x,y) que recibí esta fuera del rango,
               borro la letra de _palabra y actualizo el boton de la matriz '''
            if orientacion=='Horizontal':

                if event[1] != lista_posiciones[0][1]:
                    print('EVENTO[1]', event[1])
                    print('LIST[0][1] ' , lista_posiciones[0][1])
                    sg.popup('Error de colocacion de letra')
                    self._parametros.del_ficha_palabra(event)
                    window.Element(event).Update('')
            else:
                if event[0] != lista_posiciones[0][0]:
                    sg.popup('Error de colocacion de letra')
                    self._parametros.del_ficha_palabra(event)
                    window.Element(event).Update('')