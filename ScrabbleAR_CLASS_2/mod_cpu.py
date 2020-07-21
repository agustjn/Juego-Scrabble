from pattern.es import verbs, tag, spelling, lexicon, parse, split
from const import matriz
from random import randint

'''CONJUNTO DE FUNCIONES DEL BOT'''
def create_word(atril_cpu,nivel,var):
    letters=[]
    for letter in atril_cpu:
        letters.append(letter)
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
        if (len(palabra)>=3)and(len(palabra)<=7)and(ord(palabra[0])>=97)and(ord(palabra[0])<=122) and (palabra in spelling.keys()):
            if todo:
                cont=0
                for letra in palabra:
                    if (palabra.count(letra) <= letters.count(letra.upper())):
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
                        if (((pos[1]=='JJ') and (adj)) or ((pos[1]=='VB') and (vb))) and (len(pos[0])>=4):
                            cont=0
                            for letra in pos[0]:
                                if (pos[0].count(letra) <= letters.count(letra.upper())):
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
    var=palabra_cpu.upper()
    #return palabra_cpu.upper()

def verificar_espacio(window,casilla_cpu,palabra_cpu):
    columna=casilla_cpu[0]
    fila=casilla_cpu[1]
    horizontal = True
    vertical = True
    for i in range(len(palabra_cpu)):
        if (columna+i,fila) not in matriz:
            horizontal = False
            break
        else:
            if window.Element((columna+i,fila)).GetText()!='':
                horizontal = False
                break
    if horizontal:
        return 'Horizontal'
    else:

        for i in range(len(palabra_cpu)):
            if (columna,fila+i) not in matriz:
                vertical = False
                break
            else:
                if window.Element((columna,fila+i)).GetText()!='':
                    vertical = False
                    break
        if vertical:
            return 'Vertical'
    if not horizontal and not vertical:
        return 'No Valido'



'''def verificar_espacio(col,fila,orientacion,palabra,window):
    ok=True
    if orientacion=='Vertical':
        for i in range(len(palabra)):
             if self.window[(col,fila+i)] != '':        #COLUMNA SELECCIONADA + 0,1,2,3...'''





def colocar_palabra_bot(palabra,window):
    position=(randint(1,14),randint(1,14))
    result=verificar_espacio(window,position,palabra)
    while result == 'No valido':
        result=verificar_espacio(window,position,palabra)
