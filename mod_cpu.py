from pattern.es import verbs, tag, spelling, lexicon, parse, split
from const import matriz
from random import randint, choice

'''CONJUNTO DE FUNCIONES DEL BOT'''

def create_word(atril_cpu,nivel,parametros):
    letters=[]
    palabra_aux=[]
    for letter in atril_cpu:
        letters.append(letter)
    aux=letters.copy()
    palabra_cpu=''
    ok=False
    for palabra in lexicon.keys():
        if (len(palabra)>=3)and(len(palabra)<=7)and(ord(palabra[0])>=97)and(ord(palabra[0])<=122) and (palabra in spelling.keys()):
            if nivel=='FÁCIL':
                for letra in palabra:
                    if letra.upper() in aux:
                        aux.remove(letra.upper())
                        palabra_aux.append(letra)
                        ok=True
                    else:
                        palabra_aux=[]
                        aux=letters.copy()
                        ok=False
                        break
                if ok:
                    palabra_cpu=str().join(palabra_aux)
            else:
                datos_palabra=parse(palabra).split('/')
                if datos_palabra[1]  =='JJ' or datos_palabra[1]=='VB':
                    for letra in palabra:
                        if letra.upper() in aux:
                            aux.remove(letra.upper())
                            palabra_aux.append(letra)
                            ok=True
                        else:
                            palabra_aux=[]
                            aux=letters.copy()
                            ok=False
                            break
                    if ok==True:
                        palabra_cpu=str().join(palabra_aux)
    parametros._palabra_bot=palabra_cpu.upper()

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


def colocar_palabra_bot(window,parametros,calcular_palabra,cambiar):
    palabra=parametros.get_palabra_bot()
    if not parametros.get_primer_turno():
        position=choice(matriz)
    else:
        position=(7,7)
        parametros.set_primer_turno(False)
    result=verificar_espacio(window,position,palabra)
    while result == 'No Valido':
        position=choice(matriz)
        result=verificar_espacio(window,position,palabra)
    if palabra!='':
        Colocar_Letras(window,position,result,palabra,parametros)
        calcular_palabra(window,'bot')
    else:
        cambiar(parametros.get_atril_bot(),window)

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
            if lista_eliminados.count(letra)!=contador_letras[letra]:
                lista_eliminados.append(letra)
                pos_eliminados.append(key)
                window.Element(key).Update('')
    if orientacion=='Horizontal':
        for i in range(len(palabra_cpu)):
            window.Element((columna,fila)).Update(palabra_cpu[i])
            parametros.agregar_ficha_matriz((columna,fila),palabra_cpu[i])
            parametros.add_ficha_palabra({(columna,fila):palabra_cpu[i]})
            parametros.sacar_ficha_atril_bot(pos_eliminados[i])
            columna+=1
    else:
        for i in range(len(palabra_cpu)):
            window.Element((columna,fila)).Update(palabra_cpu[i])
            parametros.agregar_ficha_matriz((columna,fila),palabra_cpu[i])
            parametros.add_ficha_palabra({(columna,fila):palabra_cpu[i]})
            parametros.sacar_ficha_atril_bot(pos_eliminados[i])
            fila+=1
