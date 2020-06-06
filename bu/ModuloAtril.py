from random import choice


class Atril:
    bolsa_fichas={'A':11,'E':11,'O':8,'S':7,'I':6,'U':6,'N':5,'L':4,
                  'R':4,'T':4,'C':4,'D':4,'G':2,'M':3,'B':2,'P':2,'F':2,
                  'H':2,'V':2,'Y':1,'J':2,'K':1,'LL':1,'Ñ':1,'Q':1,'RR':1,
                  'W':1,'X':1,'Z':1}
    letras_juego = ['A', 'E', 'O', 'S', 'I', 'U', 'N', 'L', 'Z',
                    'R', 'T', 'C', 'D', 'G', 'M', 'B', 'P', 'X',
                    'F', 'H', 'V', 'Y', 'J', 'K', 'Ñ', 'W', 'Q',
                    'RR', 'LL']
    letras_bolsa = 100

    def __init__(self, mano):
        self._mano_jugador = mano

    def getMano(self):
        return self._mano_jugador

    def repartirFichas(self):
        for i in range(7):
            letra = choice(Atril.letras_juego)
            if Atril.letras_bolsa != 0:
                while ((Atril.letras_bolsa != 0) &
                       (Atril.bolsa_fichas[letra] == 0)):
                    letra = choice(Atril.letras_juego)
                Atril.letras_bolsa -= 1
                Atril.bolsa_fichas[letra] -= 1
            else:
                letra = ''
            self._mano_jugador.append(letra)

    def devolverFichas(self):
        for i in range(7):
            Atril.bolsa_fichas[self._mano_jugador[i]] += 1
        for i in reversed(range(7)):
            self._mano_jugador.remove(self._mano_jugador[i])
        self.repartirFichas()

    def bolsaVacia(self):
        for letra in Atril.bolsa_fichas:
            if Atril.bolsa_fichas[letra] != 0:
                return True
        return False

def ActualizarFichas(window,jugador,cpu):
    for i in range(7):
        window.Element(str(i)+'J').Update(jugador.getMano()[i])
    for i in range(7):
        window.Element(str(i)+'C').Update(cpu.getMano()[i])
