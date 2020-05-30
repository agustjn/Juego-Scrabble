class ScoreControl:
	puntos=0

	def __init__(self, puntaje_inicial):
			puntos=puntaje_inicial

	@property
	def get_puntos(self):
		return (self.puntos)

	def multiplicar(self, color):
		if color is 'green':
			self.colorGreen()
		elif color is 'yellow':
			self.colorYellow()
		elif color is 'blue':
			self.colorBlue()
		elif color is 'red':
			self.colorRed()

	def colorGreen(self):
		self.puntos*=4
	def colorYellow(self):
		self.puntos*=3
	def colorBlue(self):
		self.puntos*=2
	def colorRed(self):
		self.puntos-=1