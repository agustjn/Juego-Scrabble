from random import choice

class AtrilP:
	bolsa_fichas={'A':11,'E':11,'O':8,'S':7,'I':6,'U':6,'N':5,'L':4,'R':4,'T':4,
	              'C':4,'D':4,'G':2,'M':3,'B':2,'P':2,'F':2,'H':2,'V':2,'Y':1,
	              'J':2,'K':1,'LL':1,'Ñ':1,'Q':1,'RR':1,'W':1,'X':1,'Z':1}
	def __init__(self,mano,letras):
		self._mano_jugador=mano
		self._letras_juego=letras
	def repartirFichas(self):
		for i in range(7):
			letra=choice(self._letras_juego) #lista de letras de la bolsa
			while AtrilP.bolsa_fichas[letra]==0:
				letra=choice(self._letras_juego)
			self._mano_jugador.append(letra)
			AtrilP.bolsa_fichas[letra]-=1
