from pattern.es import verbs, tag, spelling, lexicon
import string

def checkOrientation(list_of_positions):
        firstPosition=list_of_positions[0]
        lastPosition=list_of_positions[-1]
        firstCol=list_of_positions[0][0]
        lastCol=list_of_positions[-1][0]
        if firstCol == lastCol:
            return 'Vertical'
        else:
            return 'Horizontal'

def checkWord(list_of_positions,matriz):
         palabraAnalizada=''
         if (checkOrientation(list_of_positions) == 'Horizontal'):
             '''Recorrido de primer columna a ultima columna , la fila es constante'''  #lista=['1,4','2,4','3,4','4,4','5,4']
             filaEnComun=int(list_of_positions[0][2])
             firstColumn=int(list_of_positions[0][0])
             lastColumn=int(list_of_positions[-1][0])
             for i in range(firstColumn,lastColumn+1):
                 palabraAnalizada+=matriz[str(i)+','+str(filaEnComun)]['letra']
         else:
              '''Recorrido de primer fila a ultima fila, la columa es constante'''  #lista=['3,4','3,5','3,6','3,7','3,8']
              columnaEnComun=int(list_of_positions[0][0])
              firstRow=int(list_of_positions[0][2])
              lastRow=int(list_of_positions[-1][2])
              for i in range(firstRow,lastRow+1):
                  palabraAnalizada+=matriz[str(columnaEnComun)+','+str(i)]['letra']
         return palabraAnalizada



def verifyWord(word):
    if not(word.lower() in spelling) or not(word.lower() in lexicon):
        print('La palabra {} no existe'.format(word))
    else:
        print('La palabra {} existe!'.format(word))

'''def clasificar(palabra):
	t = tag(palabra, tokenize=True, encoding='utf-8')[0][1] # si fueran varias palabras devuelve una lista de pares (palabra, tag)
	print('  tag:',t)
	return t

def buscar_en_pattern(palabra):

	print('  Buscar "',palabra,'" en pattern', sep='')
	if not palabra.lower() in verbs:
		if not palabra.lower() in spelling:
			if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
				print('\n  No se encuentra en pattern.es')
				return '_Ninguna_'
			else:
				print('\n  La encontró en lexicon')
				return clasificar(palabra)
		else:
			print('\n  La encontró en spelling')
			return clasificar(palabra)
	else:
		print('\n  La encontró en verbs')
		return clasificar(palabra)

	print('\n?\n')'''
