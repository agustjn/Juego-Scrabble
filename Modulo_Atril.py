from random import choice
from Modulo_Puntos import Puntaje

class Atril(Puntaje):#Puntaje
    ''' Esta clase se encarga de realizar todas las operaciones entre las manos
        de los jugadores y la bolsa de fichas '''
    '''bolsa_fichas = {'A': 9, 'E': 9, 'O': 8, 'S': 7, 'I': 6, 'U': 6, 'N': 5,
                    'R': 4, 'T': 4, 'C': 4, 'D': 4, 'G': 2, 'M': 3, 'B': 2,
                    'H': 2, 'V': 2, 'Y': 2, 'J': 2, 'K': 1, 'Ñ': 1, 'Q': 1,
                    'W': 2, 'X': 2, 'Z': 2, 'L': 4, 'P': 2, 'F': 2,
                    'RR': 1, 'LL': 1}'''
    bolsa_fichas = {'A': {'cantidad':9,'puntaje':1}, 'E':{'cantidad':9,'puntaje':1},
                    'O': {'cantidad':8,'puntaje':1}, 'S': {'cantidad':7,'puntaje':1},
                    'I': {'cantidad':6,'puntaje':1}, 'U': {'cantidad':6,'puntaje':1},
                    'N': {'cantidad':5,'puntaje':1}, 'R': {'cantidad':4,'puntaje':1},
                    'T': {'cantidad':4,'puntaje':1}, 'C': {'cantidad':4,'puntaje':2},
                    'D': {'cantidad':4,'puntaje':2}, 'G': {'cantidad':2,'puntaje':2},
                    'M': {'cantidad':3,'puntaje':3}, 'B': {'cantidad':2,'puntaje':3},
                    'H': {'cantidad':2,'puntaje':4}, 'V': {'cantidad':2,'puntaje':4},
                    'Y': {'cantidad':2,'puntaje':4}, 'J': {'cantidad':2,'puntaje':6},
                    'K': {'cantidad':1,'puntaje':8}, 'Ñ': {'cantidad':1,'puntaje':8},
                    'Q': {'cantidad':1,'puntaje':8}, 'W': {'cantidad':2,'puntaje':8},
                    'X': {'cantidad':2,'puntaje':8}, 'Z': {'cantidad':2,'puntaje':10},
                    'L': {'cantidad':4,'puntaje':1}, 'P': {'cantidad':2,'puntaje':3},
                    'F': {'cantidad':2,'puntaje':4}}

    letras_juego = ['A', 'E', 'O', 'S', 'I', 'U', 'N', 'L', 'Z',
                    'R', 'T', 'C', 'D', 'G', 'M', 'B', 'P', 'X',
                    'F', 'H', 'V', 'Y', 'J', 'K', 'Ñ', 'W', 'Q',
                    'RR', 'LL']
    letras_bolsa = 98

    def __init__(self, mano,puntaje=1):
        self._mano_jugador = mano
        #dificultad = 'Facil'
        Puntaje.__init__(self,puntaje)

    def getMano(self):
        return self._mano_jugador
   
    def setMano(self,mano):
        self._mano_jugador = mano

    def actualizarCasillaAtril(self,casilla):
        self._mano_jugador[casilla]=''

    def repartirFichas(self):
        for i in range(7):
            letra = choice(list(Atril.bolsa_fichas.keys()))
            if Atril.letras_bolsa != 0:
                while ((Atril.bolsa_fichas[letra]['cantidad']!= 0) and  #Atril.letras_bolsa
                       (Atril.bolsa_fichas[letra] == 0)):
                    letra = choice(list(Atril.bolsa_fichas.keys()))
                Atril.letras_bolsa -= 1
                Atril.bolsa_fichas[letra]['cantidad'] -= 1
            else:
                letra = ''
            self._mano_jugador.append(letra)

    def devolverFichas(self):
        for i in range(7):
            if self._mano_jugador[i]!='':
                Atril.bolsa_fichas[self._mano_jugador[i]]['cantidad'] += 1
                Atril.letras_bolsa+=1
        for i in reversed(range(7)):
            self._mano_jugador.remove(self._mano_jugador[i])
        self.repartirFichas()

    def bolsaVacia(self):
        for letra in Atril.bolsa_fichas:
            if Atril.bolsa_fichas[letra] != 0:
                return True
        return False


def Actualizar_Atril_Jugador(window, jugador):
    for i in range(7):
        window.Element(('Jugador',i)).Update(jugador.getMano()[i])
def Actualizar_Atril_Cpu(window,cpu):
    for i in range(7):
        window.Element(('Cpu',i)).Update(cpu.getMano()[i])
