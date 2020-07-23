from const import const_Update, reglas


class Turno:
    def __init__(self, parametros):
        self._parametros = parametros
        self._MS = 0    # MILISEGUNDOS

    def conteo(self, window):
        ''' MANTIENE ACTUALIZADO EL TIEMPO.'''
        self._MS += 100
        if self._MS == 1000:    # SI SE LLEGÓ AL SEGUNDO (MIL MILISEGUNDOS)
            self._MS = 0    # SE RESETEN LOS MILISEGUNDOS
            if self._parametros.get_turno():    # SI ES EL TURNO DEL JUGADOR (osea True)
                self._parametros.dec_contador_total() # LE VAMOS DESCONTANDO EL TIEMPO TOTAL
            self._parametros.set_segundos(int(self._parametros.get_segundos())-1 if int(self._parametros.get_segundos()) != 0 else int(self._parametros.get_tiempo_por_turno()))   # SI SE LLEGÓ AL TIEMPO LÍMITE, SE REINICIA EL CONTADOR PARA EL SIGUIENTE TURNO, SINO, SE RESTA EN 1 EL TIEMPO ACTUAL
            const_Update(window, {'tiempo': 'TIEMPO DE RONDA: '+str(self._parametros.get_segundos()), 'tiempo_total': 'TIEMPO TOTAL: '+str(self._parametros.get_contador_total()['minutos'])+':'+str(self._parametros.get_contador_total()['segundos'])})

    def fin_de_turno(self, window):
        ''' CAMBIA EL TURNO Y REINICIA EL TIEMPO.'''
        const_Update(window, {'turno': 'BOT'}) if self._parametros.get_turno() else const_Update(window, {'turno': 'JUGADOR'})
        if len(self._parametros._palabra) == 0: # Fue turno del bot
            for letter in self._parametros._palabra_bot:
                self._parametros.dec_letra_bolsa(letter, 1)
        else:
            for pos, letter in self._parametros._palabra.items():    # Fue turno del jugador
                self._parametros.dec_letra_bolsa(letter, 1)
        self._parametros.set_turno(not self._parametros.get_turno())    # CAMBIA EL TURNO
        self._parametros.set_segundos(self._parametros.get_tiempo_por_turno())  # REINICIA EL CONTADOR A EL TIEMPO TOTAL POR TURNO
        self._MS = 900  # AL FINALIZAR EL TURNO, Y SE LLAME A conteo, SE SUMAN 100 MILISEGUNDOS Y CONTINUA NORMALMENTE
