from pattern.es import verbs, tag, spelling, lexicon, parse, split
from mod_puntos import Puntaje
import const


class Interfaz(Puntaje):

    def __init__(self, parametros):
        self._parametros = parametros
        Puntaje.__init__(self)

    def primer_turno(self):
        if not self._parametros.get_primer_turno():
            return False
        if self._parametros.get_palabra():
            for key in self._parametros.get_palabra():
                if key == (7, 7):
                    self._parametros.set_primer_turno()
                    return False
        return True

    def devolver_fichas(self, window, quien):
        palabra = self._parametros.get_palabra()
        atril = getattr(self._parametros, 'get_atril_'+quien)()
        if len(getattr(self._parametros, 'get_atril_'+quien)()) == 7:
            for key in palabra:
                self._parametros.add_letra_bolsa(palabra[key])
                self._parametros.add_fichas()
            const.const_Update(window, {key: '' for key in palabra})
            self._parametros.borrar_palabra()
            self._parametros.set_matriz({})
            const.const_Update(window, {'fichas_jugador': 'MIS FICHAS ~~~~~~ TOTAL DE FICHAS: '+str(self._parametros.get_fichas())})
            return False
        keys, viejo_atril, i, j = getattr(const, 'atril_'+quien), {}, 0, 0
        for key in keys:
            if key in atril:
                viejo_atril[key] = atril[key]
            else:
                viejo_atril[(quien, i)] = list(palabra.values())[j]
                j += 1
            i += 1
        self._parametros.set_matriz({})
        getattr(self._parametros, 'set_atril_'+quien)(viejo_atril)
        const.const_Update(window, {key: '' for key in palabra}, viejo_atril)
        self._parametros.borrar_palabra()

    def mover_ficha(self, window, key):
        ''' ESTA FUNCIÓN CUMPLE CON EL MOVIMIENTO DE LA FICHA
            SELECCIONADA (EN MANO) DESDE EL ATRIL HASTA LA MATRIZ.'''
        self._parametros.sacar_ficha_atril_jugador()
        self._parametros.agregar_ficha_matriz(key)
        self._parametros.add_ficha_palabra({key: self._parametros.get_letra_ficha()})
        const.const_Update(window,{self._parametros.get_key_ficha(): '', key: self._parametros.get_letra_ficha()})
        self._parametros.set_letra_ficha('')

    def repartir_fichas(self, atril, window):
        ''' AGREGA LAS FICHAS SIN USAR A LA BOLSA. REPARTE HASTA 7 NUEVAS FICHAS.'''
        self._parametros.dec_fichas(7-len(atril))
        for key in atril:
            self._parametros.add_letra_bolsa(atril[key])
        if atril == self._parametros.get_atril_jugador():
            for i in range(7):
                letra = {('jugador', i): self._parametros.letra_random()}
                self._parametros.agregar_ficha_atril_jugador(letra)
                self._parametros.dec_letra_bolsa(list(letra.values())[0])
                const.const_Update(window, letra)
        else:
            for i in range(7):
                letra = {('bot', i): self._parametros.letra_random()}
                self._parametros.agregar_ficha_atril_bot(letra)
                self._parametros.dec_letra_bolsa(list(letra.values())[0])
                const.const_Update(window, letra)
        const.const_Update(window, {'fichas_jugador': 'MIS FICHAS ~~~~~~ TOTAL DE FICHAS: '+str(self._parametros.get_fichas())})

    def _validar_palabra(self, palabra):
        ''' TRADUCE LAS FICHAS Y LAS ORDENA HORIZONTAL Y VERTICALMENTE. SI DE
            ALGUNA DE ESAS DOS MANERAS EXISTE LA PALABRA EN LOS LISTADOS DE
            PALABRAS, LA DEVUELVE, SINO, DEVUELVE UN STRING NULO "".'''
        palabra_en_x, palabra_en_y = '', ''
        for key in {key: value for key, value in sorted(palabra.items(), key=lambda elem: elem[0][0])}:
            palabra_en_x += palabra[key]
        for key in {key: value for key, value in sorted(palabra.items(), key=lambda elem: elem[0][1])}:
            palabra_en_y += palabra[key]
        if ((palabra_en_x.lower() in lexicon) or (palabra_en_x.lower() in spelling) or (palabra_en_y.lower() in lexicon) or (palabra_en_y.lower() in spelling)):
            return self._parametros.get_palabra()
        else:
            return ''

    def calcular_palabra(self, window, quien):
        ''' CALCULA Y DEVUELVE EL PUNTAJE GANADO O PERDIDO AL FINALIZAR UN TURNO'''
        getattr(self._parametros, 'add_puntos_'+quien)(self._calcular_palabra(quien, self._validar_palabra(self._parametros.get_palabra())))
        const.const_Update(window, {'puntos_'+quien: int(window.Element('puntos_'+quien).Get())+getattr(self._parametros, 'get_puntos_'+quien)()})

    def set_dificultad(self):
        self._set_dificultad(self._parametros.get_dificultad())
