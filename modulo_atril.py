from random import choice
from const import puntos_por_color

class Atril():#Puntaje
    ''' Esta clase se encarga de realizar todas las operaciones entre las manos
        de los jugadores y la bolsa de fichas '''
    '''bolsa_fichas = {'A': 9, 'E': 9, 'O': 8, 'S': 7, 'I': 6, 'U': 6, 'N': 5,
                    'R': 4, 'T': 4, 'C': 4, 'D': 4, 'G': 2, 'M': 3, 'B': 2,
                    'H': 2, 'V': 2, 'Y': 2, 'J': 2, 'K': 1, 'Ñ': 1, 'Q': 1,
                    'W': 2, 'X': 2, 'Z': 2, 'L': 4, 'P': 2, 'F': 2,
                    'RR': 1, 'LL': 1}

     letras_juego = ['A', 'E', 'O', 'S', 'I', 'U', 'N', 'L', 'Z',
                     'R', 'T', 'C', 'D', 'G', 'M', 'B', 'P', 'X',
                     'F', 'H', 'V', 'Y', 'J', 'K', 'Ñ', 'W', 'Q',
                     'RR', 'LL']'''
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


    letras_bolsa = 98

    def __init__(self, mano=[],puntos=0,dificultad=None):
        self._mano_jugador = mano
        self._puntos=puntos
        self._dificultad=dificultad
        #dificultad = 'Facil'
        #Puntaje.__init__(self,puntaje)
    #GEY Y SET MANO
    def getMano(self):
        return self._mano_jugador
    def setMano(self,mano):
        self._mano_jugador = mano
    #GEY Y SET PUNTOS
    def getPuntos(self):
        return self._puntos
    def setPuntos(self, puntaje):
        self._puntos = puntaje
    #SUMA DE PUNTOS SEGUN CASILLA Y NIVEL
    def sumar(self, color,puntaje_letra,player):
        if color is 'red':
            self._puntos +=puntaje_letra-int(puntos_por_color[self._dificultad][player]['red'][-1:])
        elif color is 'green':
            self._puntos+=puntaje_letra*int(puntos_por_color[self._dificultad][player]['green'][-1:])
        elif color is 'blue':
            self._puntos += puntaje_letra+int(puntos_por_color[self._dificultad][player]['blue'][-1:])
        elif color is 'yellow':
            self._puntos += puntaje_letra+int(puntos_por_color[self._dificultad][player]['yellow'][-1:])
        elif color is 'grey':
            self._puntos += puntaje_letra+int(puntos_por_color[self._dificultad][player]['grey'][-1:])

    def actualizarCasillaAtril(self,casilla): # actualiza la mano del jugador con un espacio en una casilla espeficifa
        self._mano_jugador[casilla]=''

    def repartirFichas(self):#repartidor de fichas siempre reparte de a 7
        for i in range(7):
            letra = choice(list(Atril.bolsa_fichas.keys()))
            if Atril.letras_bolsa != 0:
                while ((Atril.bolsa_fichas[letra]['cantidad']!= 0) and  #Atril.letras_bolsa
                       (Atril.bolsa_fichas[letra] == 0)):
                    letra = choice(list(Atril.bolsa_fichas.keys()))
                Atril.letras_bolsa -= 1
                Atril.bolsa_fichas[letra]['cantidad'] -= 1
            else:# en caso de que no haya mas letras en la bolsa te da un espacio en blanco
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

def Actualizar_Puntos(objeto,player,casillas,puntos_por_letra,window,historial,word,nivel):#Actualizador de puntos y historial de palabras
    suma_aux=0
    for i in range(len(casillas)):
        objeto.sumar(casillas[i],puntos_por_letra[i],player)
        if casillas[i]=='green':
            suma_aux+=puntos_por_letra[i]*int(puntos_por_color[nivel][player][casillas[i]][-1:])
        elif casillas[i]=='red':
            suma_aux+=puntos_por_letra[i]-int(puntos_por_color[nivel][player][casillas[i]][-1:])
        else:
            suma_aux+=puntos_por_letra[i]+int(puntos_por_color[nivel][player][casillas[i]][-1:])
    if player =='jugador':
        window.Element('Puntos_jugador').Update(objeto.getPuntos())
    else:
        window.Element('Puntos_cpu').Update(objeto.getPuntos())
    historial.append(word+'    '+str(suma_aux)+' puntos')
