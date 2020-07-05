from pattern.es import verbs, tag, spelling, lexicon
import string
from Modulo_Puntos import Puntaje as scoreControl
class Matriz():

    def __init__(self):
        self._matriz_tablero=self.generarTablero()
        self._lista_letras=[]       #Letras ingresadas en el tablero en cada jugada
        self._positions=[]          #Posiciones ingresadas en el tablero en cada jugada


    def generarTablero(self):
       matriz_tablero = {(x, y):{'letra':'','color_casilla':''} for x in range(15) for y in range(15)}
       return matriz_tablero
       '''colores=self.cargarColor(difficult)
       for color,  casillas in colores:
           for casilla in casillas:
               window.Element(casilla).Update(button_color=('black', color))
               matriz_tablero[casilla]['color_casilla'] = color'''

    def actualizarMatriz(self,letter,pos):
       self._matriz_tablero[pos]['letra']=letter
       self._lista_letras.append(letter)
       self._positions.append(pos)


    def enviarPalabra(self):
        palabra=''
        for letter in self._lista_letras:
            palabra=palabra + letter
        resultado=self.verifyWord(palabra)
        if resultado==True:
            print('La palabra fue correcta!')
        else:
            print('La palabra fue incorrecta')
            resultado=False
        self._lista_letras=[]
        self._positions=[]
        return resultado


    ''' def devolverPuntaje(self):
    scoreControl._puntos=0
    for position in self._positions:        #por cada coordenada
        colorActual=self._matriz_tablero[position]['color']
        scoreControl.sumar(colorActual)
    return scoreControl.get_puntos'''

    def verifyWord(self,word):
        if not(word.lower() in spelling) or not(word.lower() in lexicon):
            return False
        else:
            return True

    def checkOrientation(self,list_of_positions):
            firstPosition=list_of_positions[0]
            lastPosition=list_of_positions[-1]
            firstCol=list_of_positions[0].split(',')[0]
            lastCol=list_of_positions[-1].split(',')[0]
            if firstCol == lastCol:
                return 'Vertical'
            else:
                return 'Horizontal'
