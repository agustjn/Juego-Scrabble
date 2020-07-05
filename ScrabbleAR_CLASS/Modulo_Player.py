import random
class Jugador():
    bolsa_fichas = {'A': 9, 'E': 9, 'O': 8, 'S': 7, 'I': 6, 'U': 6, 'N': 5,
                        'R': 4, 'T': 4, 'C': 4, 'D': 4, 'G': 2, 'M': 3, 'B': 2,
                        'H': 2, 'V': 2, 'Y': 2, 'J': 2, 'K': 1, 'Ñ': 1, 'Q': 1,
                        'W': 2, 'X': 2, 'Z': 2, 'L': 4, 'P': 2, 'F': 2,
                        'RR': 1, 'LL': 1}

    def __init__(self):
            self._letras_atril=self.repartirFichas()
            self._puntos=0

    def getMano(self):
        return self._letras_atril  # RETORNA LA LISTA DEL ATRIL ACTUAL

    def getBolsa(self):
        return self.bolsa_fichas  #RETORNA UN DICCIONARIO DE LAS LETRAS Y CANTIDAD DE LETRAS EN LA BOLSA

    '''FUNCION PARCHE DE REPARTIR FICHAS
    def randomLetter(self):
        letter = random.choice(list(self.bolsa_fichas.items()))
        if ((bolsa_fichas[letter][0]==0) | letter[0] in self._letras_atril.keys()):
                while((self.bolsa_fichas[letter[1]] == 0) | (letter[0] in atrilIncompleto.keys())):  #MIENTRAS LA LETRA X = 0 | SI LA LETRA YA EXISTE
                    letter = random.choice(list(self.bolsa_fichas.keys()))       # random.choice(list(d.keys()))
        return letter'''

    def controlLetra(self,letra):
        if ((self.bolsa_fichas[letra] == 0) | (letra in self._letras_atril)):
            return False
        else:
            return True


    def repartirFichas(self):
           self._letras_atril=[]
           letter = random.choice(list(self.bolsa_fichas.items())) #letter = ('X',CANT) / #letter[1]=CANT / #letter[0]='X'
           if self.controlLetra(letter[0])==True:
               self._letras_atril.append(letter[0])
           else:
               while self.controlLetra(letter[0]) == False:
                   letter = random.choice(list(self.bolsa_fichas.items()))
               self._letras_atril.append(letter[0])
           for i in range(6):
               letter = random.choice(list(self.bolsa_fichas.items()))
               if self.controlLetra(letter[0])==True:
                   self._letras_atril.append(letter[0])
               else:
                   while self.controlLetra(letter[0]) == False:
                         letter = random.choice(list(self.bolsa_fichas.items()))
                   self._letras_atril.append(letter[0])
           return self._letras_atril



    def descontarLetra(self,letter):
        self.bolsa_fichas[letter]-= 1
