class Matriz():

    def __init__(self):
        self._matriz_tablero=self.generarTablero()


    def generarTablero(self):
       matriz_tablero = {(x, y):{'letra':''} for x in range(15) for y in range(15)}
       return matriz_tablero
       '''colores=self.cargarColor(difficult)
       for color,  casillas in colores:
           for casilla in casillas:
               window.Element(casilla).Update(button_color=('black', color))
               matriz_tablero[casilla]['color_casilla'] = color'''

    def actualizarMatriz(self,letter,pos):
       self._matriz_tablero[pos]['letra']=letter
