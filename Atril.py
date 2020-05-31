from random import choice

class Atril():
	bolsa={'A':9, 'B':8, 'C':5, 'D':4, 'E':7, 'F':6, 'G':5, 'H':4, 'I':3,
			'J':4,'K':3, 'L':4, 'LL':1, 'M':2, 'N':1, 'Ñ':2, 'O':4, 'P':4,
			'Q':4, 'R':3, 'RR':3, 'S':3, 'T':2, 'U':2, 'V':2, 'W':2, 'X':1,
			'Y':1, 'Z':1}

	def __init__(self):

	@property
	def get_letras(self):
		letras=[]
		for i in range(7):
			letras.append(choice(bolsa.keys()))
		return letras

	def disminuir(self, letra):
		bolsa[letra]-=1 if bolsa[letra]!=0