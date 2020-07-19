from pattern.es import verbs, tag, spelling, lexicon, parse, split
from mod_puntos import Puntaje
import const


class Interfaz(Puntaje):

    def __init__(self, parametros):
        self._parametros = parametros
        Puntaje.__init__(self)

    def primer_turno(self):
        if not self._parametros.get_primer_turno(): # SI NO ES EL PRIMER TURNO
            return False
        if self._parametros.get_palabra():  # SI HAY FICHAS EN LA PALABRA, ES DECIR, SE INGRESÓ UNA PALABRA
            for key in self._parametros.get_palabra():  # PARA CADA UBICACIÓN DE LAS LETRAS
                if key == (7, 7):   # SI SE UBICÓ ALGUNA EN EL CENTRO
                    self._parametros.set_primer_turno() # FINALIZA EL PRIMER TURNO
                    return False
        return True

    def devolver_fichas(self, window, quien):
        palabra = self._parametros.get_palabra()
        atril = getattr(self._parametros, 'get_atril_'+quien)() # EL ATRÍL SEGÚN QUIÉN, 'jugador' o 'bot'
        if len(getattr(self._parametros, 'get_atril_'+quien)()) == 7:   # SI EL TAMAÑO DEL ATRIL SEGÚN QUIÉN ES IGUAL AL MÁXIMO, 7
            for key in palabra: # PARA CADA UBICACIÓN DE LAS LETRAS
                self._parametros.add_letra_bolsa(palabra[key])  # SUMA LA LETRA A LA BOLSA
                self._parametros.add_fichas()   # Y AUMENTA EN 1 EL TOTAL DE FICHAS, (TOTAL DE LETRAS SI SE QUIERE)
            const.const_Update(window, {key: '' for key in palabra})    # ACTUALIZA LA VENTANA, "LAS BORRA DE LA MATRIZ"
            self._parametros.borrar_palabra()   # COMO FINALIZA EL TURNO, BORRA LA PALABRA
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
        self._parametros.borrar_palabra()   # FINALIZA EL TURNO, ASÍ QUE BORRA LA PALABRA

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

    def _validar_palabra(self, palabra):
        ''' TRADUCE LAS FICHAS Y LAS ORDENA HORIZONTAL Y VERTICALMENTE. SI DE
            ALGUNA DE ESAS DOS MANERAS EXISTE LA PALABRA EN LOS LISTADOS DE
            PALABRAS, LA DEVUELVE, SINO, DEVUELVE UN STRING NULO "".'''
        palabra_en_x, palabra_en_y = '', ''
        for key in {key: value for key, value in sorted(palabra.items(), key=lambda elem: elem[0][0])}: # ESCRIBE LA PALABRA EN X PARA VERIFICAR SI ASÍ EXISTE
            palabra_en_x += palabra[key]
        for key in {key: value for key, value in sorted(palabra.items(), key=lambda elem: elem[0][1])}: # ESCRIBE LA PALABRA EN Y PARA VERIFICAR SI ASÍ EXISTE
            palabra_en_y += palabra[key]
        if ((palabra_en_x.lower() in lexicon) or (palabra_en_x.lower() in spelling) or (palabra_en_y.lower() in lexicon) or (palabra_en_y.lower() in spelling)):    # SI EXISTE LA DEVUELVE, SINO, DEVUELVE UN STRING NULO, SIMULANDO UNA PALABRA INVÁLIDA
            return self._parametros.get_palabra()
        else:
            return ''

    def calcular_palabra(self, window, quien):
        ''' CALCULA Y DEVUELVE EL PUNTAJE GANADO O PERDIDO AL FINALIZAR UN TURNO'''
        getattr(self._parametros, 'add_puntos_'+quien)(self._calcular_palabra(quien, self._validar_palabra(self._parametros.get_palabra())))    # CALCULA LA PALABRA SI ES VÁLIDA Y DEVUELVE SU PUNTAJE CORRESPONDIENTE SEGÚN LA SUMA DE LAS LETRAS EN REFERENCIA A SU PUNTUACIÓN Y COLOR EN LA QUE ESTÉN UBICADAS
        const.const_Update(window, {'puntos_'+quien: getattr(self._parametros, 'get_puntos_'+quien)()}) # ACTUALIZA EL PUNTAJE EN PANTALLA

    def set_dificultad(self):
        self._set_dificultad(self._parametros.get_dificultad())
