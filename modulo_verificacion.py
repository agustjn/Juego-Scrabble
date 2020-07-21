from pattern.es import verbs, tag, spelling, lexicon,parse,split
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
             filaEnComun=list_of_positions[0][1]
             print('Fila en comun',filaEnComun)
             firstColumn=list_of_positions[0][0]
             print('Primera Columna',firstColumn)
             lastColumn=list_of_positions[-1][0]
             print('Ultima Columna',lastColumn)
             for i in range(firstColumn,lastColumn+1):
                 palabraAnalizada+=matriz[(i,filaEnComun)]['letra']
         else:
              '''Recorrido de primer fila a ultima fila, la columa es constante'''  #lista=['3,4','3,5','3,6','3,7','3,8']
              columnaEnComun=list_of_positions[0][0]
              print('Columna en comun',columnaEnComun)
              firstRow=list_of_positions[0][1]
              print('Primera fila',firstRow)
              lastRow=list_of_positions[-1][1]
              print('Ultima fila',lastRow)
              for i in range(firstRow,lastRow+1):
                  palabraAnalizada+=matriz[(columnaEnComun,+i)]['letra']
         return palabraAnalizada



def verifyWord(word):
    if not(word.lower() in spelling) or not(word.lower() in lexicon):
        print('La palabra {} no existe'.format(word))
        return False
    else:
        print('La palabra {} existe!'.format(word))
        return True

def Validar_Palabra_CPU(mano_cpu,nivel):
    print(mano_cpu)
    if nivel=='FACIL':
        todo=True
    elif nivel=='MEDIO':
        adj=True
        vb=True
        todo=False
    elif nivel=='DIFICIL':
        adj=True
        vb=False
        todo=False
    palabra_cpu=''
    ok=False
    for palabra in lexicon.keys():
        if (len(palabra)>=3)&(len(palabra)<=7)&(ord(palabra[0])>=97)&(ord(palabra[0])<=122) & (palabra in spelling.keys()):
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
