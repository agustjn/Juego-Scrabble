from pattern.es import verbs, tag, spelling, lexicon,parse,split
import string

def checkOrientation(list_of_positions):
        firstPosition=list_of_positions[0]
        lastPosition=list_of_positions[-1]
        firstCol=list_of_positions[0].split(',')[0]
        lastCol=list_of_positions[-1].split(',')[0]
        if firstCol == lastCol:
            return 'Vertical'
        else:
            return 'Horizontal'

def checkWord(list_of_positions,matriz):
         palabraAnalizada=''
         if (checkOrientation(list_of_positions) == 'Horizontal'):
             '''Recorrido de primer columna a ultima columna , la fila es constante'''  #lista=['1,4','2,4','3,4','4,4','5,4']
             filaEnComun=int(list_of_positions[0].split(',')[1])
             print('Fila en comun',filaEnComun)
             firstColumn=int(list_of_positions[0].split(',')[0])
             print('Primera Columna',firstColumn)
             lastColumn=int(list_of_positions[-1].split(',')[0])
             print('Ultima Columna',lastColumn)
             for i in range(firstColumn,lastColumn+1):
                 palabraAnalizada+=matriz[str(i)+','+str(filaEnComun)]['letra']
         else:
              '''Recorrido de primer fila a ultima fila, la columa es constante'''  #lista=['3,4','3,5','3,6','3,7','3,8']
              columnaEnComun=int(list_of_positions[0].split(',')[0])
              print('Columna en comun',columnaEnComun)
              firstRow=int(list_of_positions[0].split(',')[1])
              print('Primera fila',firstRow)
              lastRow=int(list_of_positions[-1].split(',')[1])
              print('Ultima fila',lastRow)
              for i in range(firstRow,lastRow+1):
                  palabraAnalizada+=matriz[str(columnaEnComun)+','+str(i)]['letra']
         return palabraAnalizada



def verifyWord(word):
    if not(word.lower() in spelling) or not(word.lower() in lexicon):
        print('La palabra {} no existe'.format(word))
    else:
        print('La palabra {} existe!'.format(word))

def Validar_Palabra_CPU(mano_cpu,nivel):
    if nivel=='Facil':
        todo=True
    elif nivel=='Medio':
        adj=True
        vb=True
        todo=False
    elif nivel=='Dificil':
        adj=True
        vb=False
        todo=False
    palabra_cpu=''
    ok=False
    for palabra in lexicon.keys():
        if (len(palabra)>=4)&(len(palabra)<=7)&(ord(palabra[0])>=97)&(ord(palabra[0])<=122) & (palabra in spelling.keys()):
            if todo:
                cont=0
                for letra in palabra:
                    if (palabra.count(letra) <= mano_cpu.count(letra.upper())):
                        cont+=1
                    if len(palabra)==cont:
                        palabra_cpu=palabra
                        ok=True
                        break
                if ok:
                    break
            else:
                datos_palabra=parse(palabra).split()
                for datos in datos_palabra:
                    for pos in datos:
                        if (((pos[1]=='JJ')&(adj))|((pos[1]=='VB')&(vb)))&(len(pos[0])>=4):
                            cont=0
                            for letra in pos[0]:
                                if (pos[0].count(letra) <= mano_cpu.count(letra.upper())):
                                    cont+=1
                                if len(pos[0])==cont:
                                    palabra_cpu=pos[0]
                                    ok=True
                                    break
                            if ok:
                                break
                        if ok:
                            break
                if ok:
                    break
    return palabra_cpu.upper()

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
