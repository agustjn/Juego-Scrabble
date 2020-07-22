from pattern.es import verbs, tag, spelling, lexicon, parse, split
from const import matriz
from random import randint

'''CONJUNTO DE FUNCIONES DEL BOT'''
def create_word(atril_cpu,nivel,parametros):
    letters=[]
    for letter in atril_cpu:
        letters.append(letter)
    if nivel=='FÁCIL':
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
        if (len(palabra)>=2)and(len(palabra)<=7)and(ord(palabra[0])>=97)and(ord(palabra[0])<=122) and (palabra in spelling.keys()):
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
    parametros._palabra_bot=palabra_cpu.upper()
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





def colocar_palabra_bot(palabra,window,parametros, calcular_palabra):
    position=(randint(1,14),randint(1,14))
    result=verificar_espacio(window,position,palabra)
    while result == 'No valido':
        result=verificar_espacio(window,position,palabra)
    Colocar_Letras(window,position,result,palabra,parametros)
    calcular_palabra(window, 'bot')

def Colocar_Letras(window,casilla_cpu,orientacion,palabra_cpu,parametros):
    columna=casilla_cpu[0]
    fila=casilla_cpu[1]
    lista_eliminados=[]# lista de las letras que fueron colocadas en el atril
    pos_eliminados=[] # lista con la posicion de las letras del atril que fueron colocadas
    contador_letras={}# contador de letras para sacar del atril
    for letra in palabra_cpu:
        if letra not in contador_letras:
            contador_letras[letra]=1
        else:
            contador_letras[letra]+=1

    keysAtril=[('bot',y)for y in range(7)]

    for key in keysAtril:
        if window.Element(key).GetText() in palabra_cpu:
            letra=window.Element(key).GetText()
            print('CONT_LETRAS: ',contador_letras,' - POS DEL DIC: ',contador_letras[letra])
            if lista_eliminados.count(letra)!=contador_letras[letra]:
                lista_eliminados.append(letra)
                pos_eliminados.append(key)
                window.Element(key).Update('')
    if orientacion=='Horizontal':
        for i in range(len(palabra_cpu)):
            window.Element((columna,fila)).Update(palabra_cpu[i])
            parametros.agregar_ficha_matriz((columna,fila),palabra_cpu[i])
            parametros.add_ficha_palabra({(columna, fila): palabra_cpu[i]})
            #matriz_tablero[(columna,fila)]['letra']=palabra_cpu[i]
            parametros.sacar_ficha_atril_bot(pos_eliminados[i])
            columna+=1
    else:
        for i in range(len(palabra_cpu)):
            window.Element((columna, fila)).Update(palabra_cpu[i])
            parametros.agregar_ficha_matriz((columna,fila),palabra_cpu[i])
            parametros.add_ficha_palabra({(columna, fila): palabra_cpu[i]})
            # matriz_tablero[(columna,fila)]['letra']=palabra_cpu[i]
            parametros.sacar_ficha_atril_bot(pos_eliminados[i])
            fila += 1
