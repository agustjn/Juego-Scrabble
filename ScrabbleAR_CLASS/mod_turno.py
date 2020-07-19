from const import const_Update, reglas


class Turno:
    def __init__(self, parametros):
        self._parametros = parametros
        self._MS = 0

    def conteo(self, window):
        ''' MANTIENE ACTUALIZADO EL TIEMPO.'''
        self._MS += 100
        if self._MS == 1000:
            self._MS = 0
            self._parametros.set_segundos(self._parametros.get_segundos()-1 if self._parametros.get_segundos() != 0 else self._parametros.get_tiempo_por_turno())

    def fin_de_turno(self):
        ''' CAMBIA EL TURNO Y REINICIA EL TIEMPO.'''
        self._parametros.set_turno(not self._parametros.get_turno())
        self._parametros.set_segundos(self._parametros.get_tiempo_por_turno())
        self._MS = 900
